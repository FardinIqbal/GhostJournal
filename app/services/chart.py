import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from typing import List, Tuple

import os

from app.core.config import settings

CHART_DIR = os.path.join('charts')
os.makedirs(CHART_DIR, exist_ok=True)


def generate_chart(trade_id: str, candles: List[Tuple[datetime, float]]):
    times = [c[0] for c in candles]
    prices = [c[1] for c in candles]
    plt.figure()
    plt.plot(times, prices)
    plt.title(f'Trade {trade_id}')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    path = os.path.join(CHART_DIR, f'trade_{trade_id}.png')
    plt.savefig(path)
    plt.close()
    return path
