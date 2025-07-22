import alpaca_trade_api as tradeapi
from datetime import timedelta
from app.core.config import settings

api = tradeapi.REST(settings.alpaca_api_key, settings.alpaca_secret_key, base_url=settings.alpaca_base_url)


def fetch_filled_orders(since):
    orders = api.list_orders(status='filled', after=since.isoformat())
    return orders


def fetch_candles(symbol: str, start, end):
    barset = api.get_barset(symbol, '1Min', start=start.isoformat(), end=end.isoformat())
    bars = barset[symbol]
    return [(bar.t.to_pydatetime(), bar.c) for bar in bars]
