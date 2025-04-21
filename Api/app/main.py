import os
import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from modules.data_loader import load_data
from modules.signals import generate_bollinger_signals

app = FastAPI(title="BIST Nükleer API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/historical")
async def historical(ticker: str, start: str = os.getenv("START_DATE"), end: str = None):
    """Return historical OHLCV data for a ticker."""
    df = load_data(ticker, start, end)
    return {"ticker": ticker, "data": df.reset_index().rename(columns={'index':'date'}).to_dict("records")}

@app.websocket("/ws")
async def websocket_signals(ws: WebSocket):
    """WebSocket endpoint for real-time Bollinger signals."""
    await ws.accept()
    tickers = ["THYAO.IS", "GARAN.IS", "AKBNK.IS"]
    while True:
        out = []
        for t in tickers:
            df = load_data(t, os.getenv("START_DATE"))
            sig_df = generate_bollinger_signals(df, {'bb_period': 20, 'std_dev': 2})
            latest = sig_df.iloc[-1]
            out.append({"ticker": t, "signal": int(latest["Signal"]), "price": float(latest["Close"])})
        await ws.send_json({"signals": out})
        await asyncio.sleep(1)
