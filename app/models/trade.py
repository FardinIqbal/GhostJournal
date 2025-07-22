import uuid
from sqlalchemy import Column, String, Float, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base

class Trade(Base):
    __tablename__ = 'trades'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    symbol = Column(String, nullable=False)
    direction = Column(String, nullable=False)
    entry_price = Column(Float)
    exit_price = Column(Float)
    quantity = Column(Float)
    entry_time = Column(TIMESTAMP)
    exit_time = Column(TIMESTAMP)
    pnl = Column(Float)
    chart_url = Column(String)
    tags = Column(String)
    notes = Column(String)
