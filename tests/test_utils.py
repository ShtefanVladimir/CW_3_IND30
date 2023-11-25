from src.models import Operation
from src.utils import get_instances, get_executed_operations, sort_operations_by_date


def test_get_instances():
    operation_dict = [
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
    operations = get_instances(operation_dict)
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operation)
    assert len(operations) == 1
    assert operations[0].pk == 854048120


def test_get_executed_operations(operation_instance):
    operations = get_executed_operations(operation_instance)
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operation)
    assert len(operations) == 1
    assert operations[0].state == "EXECUTED"


def test_sort_operations_by_date(operation_instance):
    operations = sort_operations_by_date(operation_instance)
    assert isinstance(operations, list)
    assert isinstance(operations[0], Operation)
    assert len(operations) == 2
    assert operations[0].date > operations[1].date
