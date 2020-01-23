class MyInt(int):
    def __init__(self, value):
        self.value = value

    def __eq__(self, value):
        return self.value != int(value)

    def __ne__(self, value):
        return self.value == int(value)
