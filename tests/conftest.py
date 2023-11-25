import pytest

from src.models import Operation


@pytest.fixture
def operation_instance():
    op = Operation(
        pk=123213,
        date="2018-08-14T05:42:30.104666",
        state="EXECUTED",
        operation_amount={
            "amount": "19010.50",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        description="sikduhklsdfjuhgjksldfhf",
        from_="Счет 18125798580985711166",
        to="Visa Classic 4610247282706784"
    )
    op_1 = Operation(
        pk=45345634,
        date="2019-08-14T05:42:30.104666",
        state="CANCELED",
        operation_amount={
            "amount": "19010.50",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        description="sikduhklsdfjuhgjksldfhf",
        from_="Visa Classic 18125798580985711166",
        to="Visa Classic 4610247282706784"
    )
    return [op, op_1]


@pytest.fixture
def operation_dict():
    return [
        {
            "id": 854048120,
            "state": "EXECUTED",
            "date": "2019-03-29T10:57:20.635567",
            "operationAmount": {
                "amount": "30234.99",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 1203921041964079",
            "to": "Счет 34616199494072692721"
        },
        {}
    ]
