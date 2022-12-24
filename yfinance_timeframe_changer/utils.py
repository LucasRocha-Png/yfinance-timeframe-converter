from pandas_datareader import data as pdr
import yfinance as yf

def download_dataframe(ticket, timeframe):
    """
    Downloads a yfinance dataframe for tests.
    """

    
    intervals = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    periods = ["7d", "60d", "60d", "60d", "60d", "60d", "60d", "730d", "max", "max", "max" , "max", "max"]
    
    if timeframe not in intervals:
        exception_message("Timeframe do not exists!")
    
    period = periods[intervals.index(timeframe)]
    
    yf.pdr_override()
    df = pdr.get_data_yahoo(ticket, period = period, group_by = 'ticker', interval = timeframe, threads = True, progress = False)
    
    return df
    
    
def exception_message(message):
    """
    Makes a exception message
    """    
    
    from colorama import Fore

    print("\n")
    print(f"{Fore.RED}ERROR!{Fore.RESET}")
    print(message)
    print("\n")
    raise Exception(message)
    
if __name__ == "__main__": 
    print(download_dataframe("AAPL", "1d"))