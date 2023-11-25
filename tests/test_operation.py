from datetime import datetime

from src.models import Operation


def test_operation_covert_date():
    operation = Operation(
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
    assert operation.covert_date("2018-08-14T05:42:30.104666") == "14.08.2018"
