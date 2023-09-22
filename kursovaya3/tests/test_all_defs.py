import pytest
from datetime import datetime
import json

from utils.all_defs import sort_executed, mask_account, mask_card, print_operations


@pytest.fixture
def data():
    return [
        {
            "id": "1",
            "state": "EXECUTED",
            "date": "2022-01-01T12:00:00.000000",
            "description": "Test operation 1",
            "from": "Maestro 1234567890123456",
            "to": "Счет 9876543210987654",
            "operationAmount": {
                "amount": 1000,
                "currency": {
                    "name": "USD"
                }
            }
        },
        {
            "id": "2",
            "state": "EXECUTED",
            "date": "2022-01-02T12:00:00.000000",
            "description": "Test operation 2",
            "from": "MasterCard 1111222233334444",
            "to": "Счет 5555666677778888",
            "operationAmount": {
                "amount": 2000,
                "currency": {
                    "name": "EUR"
                }
            }
        },
        {
            "id": "3",
            "state": "IN_PROGRESS",
            "date": "2022-01-03T12:00:00.000000",
            "description": "Test operation 3",
            "from": "",
            "to": "",
            "operationAmount": {
                "amount": 3000,
                "currency": {
                    "name": "RUB"
                }
            }
        }
    ]

def test_sort_executed(data):
    expected_result = [
        {
            "id": "2",
            "state": "EXECUTED",
            "date": "2022-01-02T12:00:00.000000",
            "description": "Test operation 2",
            "from": "MasterCard 1111222233334444",
            "to": "Счет 5555666677778888",
            "operationAmount": {
                "amount": 2000,
                "currency": {
                    "name": "EUR"
                }
            }
        },
        {
            "id": "1",
            "state": "EXECUTED",
            "date": "2022-01-01T12:00:00.000000",
            "description": "Test operation 1",
            "from": "Maestro 1234567890123456",
            "to": "Счет 9876543210987654",
            "operationAmount": {
                "amount": 1000,
                "currency": {
                    "name": "USD"
                }
            }
        }
    ]
    result = sort_executed(data)
    assert result == expected_result

def test_mask_card():
    card_number = 'Maestro 1234567890123456'
    expected_result = 'Maestro 12** **** 3456'
    result = mask_card(card_number)
    assert result == expected_result

def test_mask_account():
    account_number = 'Счет 9876543210987654'
    expected_result = 'Счет **7654'
    result = mask_account(account_number)
    assert result == expected_result