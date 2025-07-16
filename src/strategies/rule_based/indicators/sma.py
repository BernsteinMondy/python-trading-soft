import pandas as pd


class SMAIndicator:
    @staticmethod
    def calculate(series, period, shift):
        """
        Calculates SMA with moving possibility.
        """

        if not isinstance(series, pd.Series):
            raise TypeError('series must be a pandas.Series')
        if period < 1:
            raise ValueError('period must be >= 1')
        if shift < 0:
            raise ValueError('shift must be >= 0')

        sma = series.rolling(window=period, min_periods=period).mean()
        return sma.shift(shift)
