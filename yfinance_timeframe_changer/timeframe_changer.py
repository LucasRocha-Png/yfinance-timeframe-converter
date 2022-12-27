from checker import checker, basic_check
from format import convert_row

def convert(data, timeframe_input, timeframe_output, check=True):

    basic_check(data)


    index = convert_row(data.index.to_list(), "string")
    values = convert_row(data.index.to_list(), "float")
    columns = convert_row(data.columns(), "string")

    if check == True:
        checker(data, timeframe_input, timeframe_output)
    pass


if __name__ == "__main__":
    from utils import download_data
    import time

    # Downloads an database
    df = download_data()


    start = time.time()
    convert(df, "1d", "1mo")
    end = time.time()
    print(f"Total running:", round(end - start, 10))
