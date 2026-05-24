import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from fastapi import HTTPException

from trading import get_current_price, search_ticker


def test_get_price(mocker):
    mock_ticker = MagicMock()
    mock_ticker.fast_info = {"last_price": 150.0}
    mocker.patch("yfinance.Ticker", return_value=mock_ticker)

    price = get_current_price("AAPL")
    assert price == 150.0

def test_get_current_price_invalid_ticker(mocker):
    mock_ticker = MagicMock()
    mock_ticker.fast_info.__getitem__.side_effect = AttributeError
    mocker.patch("yfinance.Ticker", return_value=mock_ticker)
    with pytest.raises(HTTPException) as e:
        get_current_price("FAKE_TICKER")
    assert e.value.status_code == 404

def test_search_ticker(mocker):
    mock_search = MagicMock()
    mock_search.quotes = [
        {"symbol": "AAPL", "shortname": "Apple Inc."},
        {"symbol": "AAPL.BA", "shortname": "Apple Inc. BA"}
    ]
    mocker.patch("yfinance.Search", return_value=mock_search)

    result = search_ticker("apple")
    assert result == mock_search.quotes
    assert result[0]["symbol"] == "AAPL"