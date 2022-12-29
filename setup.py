from setuptools import setup, find_packages

DESCRIPTION = "Converts YFinance's tables in other timeframe in an faster way"
with open("README.md", "r") as rdm:
    LONG_DESCRIPTION = rdm.read()

# Setting up
setup(
    name="yfinance_timeframe_converter",
    version='0.0.1',
    author="Lucas Rocha", 
    author_email="lucasrocha.png@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=["yfinance_timeframe_changer"],
    install_requires=['yfinance>=0.1.63', 'pandas>=1.3.3', 'pandas-datareader>=0.10.0', 'colorama>=0.4.4'],
    keywords=['python', 'yfinance', 'changer', 'yahoo', 'finance'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)