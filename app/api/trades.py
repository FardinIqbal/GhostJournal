from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.trade import Trade
from app.schemas.trade import TradeOut, TradeCreate

router = APIRouter()

@router.get('/trades', response_model=List[TradeOut])
def list_trades(db: Session = Depends(get_db)):
    return db.query(Trade).all()

@router.get('/trades/{trade_id}', response_model=TradeOut)
def get_trade(trade_id: str, db: Session = Depends(get_db)):
    trade = db.query(Trade).get(trade_id)
    if not trade:
        raise HTTPException(status_code=404, detail='Trade not found')
    return trade

@router.post('/trades', response_model=TradeOut)
def create_trade(trade_in: TradeCreate, db: Session = Depends(get_db)):
    trade = Trade(**trade_in.dict())
    db.add(trade)
    db.commit()
    db.refresh(trade)
    return trade
