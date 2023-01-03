
def exception_message(message: str) -> None:
    """
    Raises a excepetion message
    """

    print(message)
    print("\n\n")
    raise Exception(message)


def renames_timeframe(timeframe: str) -> str:
    """
    Renames timeframe from 60m to 1h
    """

    if timeframe == "60m":
        return "1h"

    return timeframe    