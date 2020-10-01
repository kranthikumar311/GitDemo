from pythonBasics.OopsDemo import Calculator


class ChildImpl(Calculator):
    num2 = 2000
    num3 = 3000
    num4 = 4000
    num5 = 5000

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompleteData())
