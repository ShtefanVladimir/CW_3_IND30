class Foo:
    data = []

    def __init__(self, name):
        self.name = name

    def get_name(self):
        self.set_data()
        return self.name

    @staticmethod
    def calculate_numbers(x, y):
        return x + y

    @classmethod
    def set_data(cls):
        cls.data.append("sdfsdfsdf")
        Foo("Vova")


Foo.set_data()

# foo = Foo("sdfasdfdsf")
# foo.get_name()
# foo.calculate_numbers(1, 2)
