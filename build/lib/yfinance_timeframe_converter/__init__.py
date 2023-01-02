from .timeframe_converter import timeframe_converter

VERSION = (1, 0, 0)

__author__ = 'Lucas Rocha'
__email__ = 'lucasrocha.png@gmail.com'
__version__ = '.'.join(map(str, VERSION))
__description__ = 'Converts the timeframe of the YFinance DataFrame passed.'

__all__ = ('timeframe_converter')
