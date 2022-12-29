def main():
    """
    downloads each timeframe to check the format 
    """
    
    from pandas_datareader import data as pdr
    import yfinance as yf
    import pandas as pd    
    import os
    
    archive_folder = os.path.dirname(__file__)

    print("\n")
    print("-"*10)
    
    ticket = "AAPL"
    yf.pdr_override()
    intervals = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    periods = ["7d", "60d", "60d", "60d", "60d", "60d", "60d", "730d", "max", "max", "max" , "max", "max"]

    for period, interval in zip(periods, intervals):
        df = pdr.get_data_yahoo(ticket, period = period, group_by = 'ticker', interval = interval, threads = True, progress = False)
        print(f"{interval} downloaded!")
        df.to_csv(f"{archive_folder}/output/{interval}.csv")
    
    
    
if __name__ == "__main__":
    main()