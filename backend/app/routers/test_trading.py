import pytest
from unittest.mock import patch, MagicMock
import pandas as pd

from trading import get_current_price


def test_get_price(mocker):
    mock_ticker = MagicMock()
    mock_ticker.fast_info = {"last_price": 150.0}
    mocker.patch("yfinance.Ticker", return_value=mock_ticker)

    price = get_current_price("AAPL")
    assert price == 150.0  # we know exactly what to expect