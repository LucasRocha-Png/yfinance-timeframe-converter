from checker import checker, basic_check
from format import format_data

def convert(data, timeframe_input, timeframe_output, check=True):

    basic_check(data)

    data = format_data(data)

    if check == True:
        checker(data, timeframe_input, timeframe_output)
    



if __name__ == "__main__":
    from utils import download_dataframe
    import time

    # Downloads an database
    df = download_dataframe("AAPL", "1d")


    start = time.time()
    
    for i in range(1):
        convert(df, "1d", "1mo")

    end = time.time()
    print(f"Total running:", round(end - start, 10))
