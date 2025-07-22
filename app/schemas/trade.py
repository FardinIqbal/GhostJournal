from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class TradeBase(BaseModel):
    symbol: str
    direction: str
    entry_price: Optional[float]
    exit_price: Optional[float]
    quantity: Optional[float]
    entry_time: Optional[datetime]
    exit_time: Optional[datetime]
    pnl: Optional[float]
    chart_url: Optional[str]
    tags: Optional[List[str]]
    notes: Optional[str]

class TradeCreate(TradeBase):
    pass

class TradeOut(TradeBase):
    id: str

    class Config:
        orm_mode = True
