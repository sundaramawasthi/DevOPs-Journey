
class myclass():
    def method1(self):
        print("this is method 1")

    def method2(self, String):
        print("method 2" + String)


class anotherclass(myclass):
    def method1(self):
        myclass. method1(self)
        print("anotherclass method 1")

    def method2(self, someString):
        print("another method 2")


def main():
    c = myclass()
    c.method1()
    c.method2("give a string vallue ")

    c2 = anotherclass()
    c2.method1()
    c2.method2("String")


if __name__ == "__main__":
    main()
