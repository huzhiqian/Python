import myClass


print(__name__)

if __name__ == "__main__":
    print("1")
    my_obj = myClass.TestClass()
    my_obj.test_fun()
    print(my_obj.data)
    my_obj.data.append("2")
    print(my_obj.data)

