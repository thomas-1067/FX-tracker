
import pytest
from project import CurrencyConverter
import datetime

# Test get_supported_currencies function
def test_get_supported_currencies():
    converter = CurrencyConverter()
    supported_currencies = converter.get_supported_currencies()
    assert supported_currencies is not None, "Supported currencies should not be None."
    assert isinstance(supported_currencies, dict), "Supported currencies should be a dictionary."
    assert 'USD' in supported_currencies, "USD should be in the list of supported currencies."
    assert 'GBP' in supported_currencies, "GBP should be in the list of supported currencies."

def test_get_valid_amount():
    converter = CurrencyConverter()

    # Test valid amounts
    assert converter.get_valid_amount(100) == 100, "Should accept a positive numeric amount."
    assert converter.get_valid_amount(200.5) == 200.5, "Should accept a positive numeric amount."
    assert converter.get_valid_amount(4.574) == 4.574, "Should accept a positive numeric amount."

    # Test invalid amounts
    assert converter.get_valid_amount(-1) == 1, "Should set invalid amount to 1."
    assert converter.get_valid_amount(0) == 1, "Should set invalid amount to 1."
    assert converter.get_valid_amount("abc") == 1, "Should set invalid amount to 1."
    assert converter.get_valid_amount("") == 1, "Should set invalid amount to 1.""Should set invalid amount to 1."


# Test get_day_rate function
def test_get_day_rate():
    base_currency = 'USD'
    target_currency = 'EUR'
    valid_date = "2020-01-01"
    invalid_date = "1999-12-31"

    converter = CurrencyConverter()
    rate = converter.get_day_rate(base_currency, target_currency, valid_date)
    assert rate is not None, "Rate should not be None for a valid date and currencies."
    assert isinstance(rate, (float, int)), "Rate should be a numeric value."

    invalid_rate = converter.get_day_rate(base_currency, target_currency, invalid_date)
    assert invalid_rate is None or isinstance(invalid_rate, (float, int)), "Rate should be None or a numeric value for an invalid date."
