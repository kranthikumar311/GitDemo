from pythonBasics.OopsDemo import Calculator


class ChildImpl(Calculator):
    num2 = 2000

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompleteData())
