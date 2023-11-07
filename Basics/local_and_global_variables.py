global1 = 'Global 1'


def my_func():
    global global1
    global1 = "name 2"


if __name__ == '__main__':
    print(global1)
    my_func()
    print(global1)
