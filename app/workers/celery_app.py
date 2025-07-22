from celery import Celery
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from app.core.config import settings
from app.services import alpaca, chart
from app.db.session import SessionLocal
from app.models import Trade

celery_app = Celery('tasks', broker=settings.redis_url)

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(300.0, ingest_trades.s(), name='ingest every 5 mins')

@celery_app.task
def ingest_trades():
    db: Session = SessionLocal()
    since = datetime.utcnow() - timedelta(minutes=30)
    orders = alpaca.fetch_filled_orders(since)
    for order in orders:
        if db.query(Trade).filter_by(id=order.id).first():
            continue
        trade = Trade(
            id=order.id,
            symbol=order.symbol,
            direction='buy' if order.side == 'buy' else 'sell',
            entry_price=float(order.filled_avg_price or 0),
            quantity=float(order.qty or 0),
            entry_time=order.filled_at,
        )
        candles = alpaca.fetch_candles(order.symbol, order.filled_at - timedelta(minutes=15), order.filled_at + timedelta(minutes=15))
        chart_path = chart.generate_chart(order.id, candles)
        trade.chart_url = chart_path
        db.add(trade)
    db.commit()
    db.close()
