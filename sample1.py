
print("hello")

class MyClass:

    def __init__(self):
        self.name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

class MyClass2(MyClass):
    def world(self):
        print("World")

a = MyClass()
a.setName("Tanaka")
print(a.getName())


b = MyClass2()
b.setName("Hoge")
print(b.world())
print(b.name)

