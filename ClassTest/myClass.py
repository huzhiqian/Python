

class TestClass:
    data = []

    def __init__(self):
        print("构造函数")

    def test_fun(self):
        print("TestFun")
        self.data.append("1")
