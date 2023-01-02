from .timeframe_converter import timeframe_converter
from .available_timeframes import yfinance_available_timeframes, converter_available_timeframes, available_convertions

VERSION = (1, 0, 1)

__author__ = 'Lucas Rocha'
__email__ = 'lucasrocha.png@gmail.com'
__version__ = '.'.join(map(str, VERSION))
__description__ = 'Converts the timeframe of the YFinance DataFrame passed.'

__all__ = ('timeframe_converter', "yfinance_available_timeframes", "converter_available_timeframes", "available_convertions")
