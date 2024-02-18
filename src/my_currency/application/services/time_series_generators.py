"""Time series generators module."""

from typing import List

import pandas as pd

from my_currency.application.interfaces import ITimeSeriesGenerator


class DailyTimeSeriesGenerator(ITimeSeriesGenerator):
    """Daily TimeSeriesGenerator class."""

    @staticmethod
    def generate(start_date: str, end_date: str) -> List[str]:
        """Generate a daily time series form a start date to an end date."""
        date_range = pd.date_range(start=start_date, end=end_date, freq="D")

        return [date.strftime("%Y-%m-%d") for date in date_range]
