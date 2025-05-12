import os
from datetime import datetime, timedelta
import pandas as pdaaaaaaaaaaaaaaaa
from binance.client import Client

# Carregue suas credenciais de API Binance (env vars ou substitua direto)
API_KEY = os.getenv()
API_SECRET = os.getenv()

# Inicializa cliente
client = Client(API_KEY, API_SECRET)

def fetch_ohlcv(symbol='BTCUSDT', interval='1h', lookback_days=60):
    '''Busca OHLCV dos últimos lookback_days dias.'''
    end = datetime.utcnow()
    start = end - timedelta(days=lookback_days)
    klines = client.get_klines(
        symbol=symbol,
        interval=interval,
        start_str=start.strftime('%d %b %Y %H:%M:%S'),
        end_str=end.strftime('%d %b %Y %H:%M:%S')
    )
    cols = ['timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'qav', 'num_trades', 'taker_base', 'taker_quote', 'ignore']
    df = pd.DataFrame(klines, columns=cols)
    # Converte e seleciona colunas relevantes
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df[['open','high','low','close','volume']] = df[['open','high','low','close','volume']].astype(float)
    return df[['timestamp','open','high','low','close','volume']]


def calculate_candle_averages(df):
    '''Calcula o preço médio de cada candle.'''
    df = df.copy()
    df['avg_price'] = df[['open','high','low','close']].mean(axis=1)
    return df


def predict_next_avg(df, window=None):
    '''Usa média simples dos avg_price dos últimos window candles.
       Se window == None, usa todo o período.
    '''
    if window:
        values = df['avg_price'].iloc[-window:]
    else:
        values = df['avg_price']
    return values.mean()


if __name__ == '__main__':
    # Parâmetros
    symbol = 'BTCUSDT'
    interval = '1h'
    lookback_days = 60  # últimos 2 meses ~ 60 dias
    moving_window = 24  # ou defina um número de candles, ex: 24 para últimas 24h

    # Busca dados
    df = fetch_ohlcv(symbol, interval, lookback_days)
    df = calculate_candle_averages(df)

    # Predição da próxima vela
    next_avg = predict_next_avg(df, moving_window)
    print(f"Predição preço médio próxima vela (base últimos {lookback_days} dias): {next_avg:.2f}")

    # Exibição das últimas 5 candles e médias
    print(df[['timestamp','open','close','avg_price']].tail())
