from datetime import datetime


class Operation:
    def __init__(
            self,
            pk: int,
            date: str,
            state: str,
            operation_amount: dict,
            description: str,
            from_: str,
            to: str,
    ):
        self.pk = pk
        self.date = self.covert_date(date)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = self.covert_info_payment(from_)
        self.to = self.covert_info_payment(to)

    def covert_date(self, date: str):
        """

        :param date:
        :return:
        """
        iso_date = datetime.fromisoformat(date)
        return datetime.strftime(iso_date, "%d.%m.%Y")

    def covert_info_payment(self, info_payment: str) -> str:
        """

        :param info_payment:
        :return:
        """
        if info_payment:
            info_list = info_payment.split()
            if info_payment.startswith("Счет"):
                num_payment = info_list.pop()
                num_payment = f"**{num_payment[-4:]}"
                info_list.append(num_payment)
            else:
                info_list = ["sdfkjhgsdhj", "skdhjfbgsdjhgf"]
            return " ".join(info_list)
        return ""

    def __str__(self):
        return (f"{self.date} {self.description}\n"
                f"{self.from_} -> {self.to}\n"
                f"{self.operation_amount['amount']} {self.operation_amount['currency']['name']}")
