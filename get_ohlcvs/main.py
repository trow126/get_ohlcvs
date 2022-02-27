import ccxt
from datetime import datetime
import pandas as pd

def main():
    date_str = datetime.now().strftime('%Y%m%d%H')

    args = sys.argv
    # args = []
    # args.append('BTC/USDT')
    # args.append('binance')

    symbol = 'BTC/USDT'
    exchange = eval('ccxt.' + args[1] + '()')

    # 時間足
    timeframe_list = ['1m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
    
    for timeframe in timeframe_list:
        ohlcvs = exchange.fetch_ohlcv(symbol=symbol, timeframe=timeframe, limit=1500)
        df_ohlcvs = pd.DataFrame(ohlcvs, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df_ohlcvs['timestamp'] = pd.to_datetime(df_ohlcvs['timestamp'], unit='ms')
        df_ohlcvs.set_index('timestamp', inplace=True)
        df_ohlcvs.sort_index(inplace=True)

        data_file_path = './data/{}/{}_{}_ohlcvs_{}.pkl'.format(args[1], date_str, args[1], timeframe)
        df_ohlcvs.to_pickle(data_file_path)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
