import mymodule1
import mymodule2
x = (mymodule2.myage - mymodule1.myage) == (mymodule2.year - mymodule1.year)
print(x)
print("my name is", __name__)
if __name__ == "__main__":
    print("this won't run if I'm imported")