
class myclass():
    def method1(self):
        print("this is method 1")

    def method2(self, String):
        print("method 2" + String)


def main():
    c = myclass()
    c.method1()
    c.method2("give a string vallue ")


if __name__ == "__main__":
    main()
