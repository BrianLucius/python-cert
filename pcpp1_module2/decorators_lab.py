from datetime import datetime

def timestamper(function):
    def wrapper(*args):
        date_now = datetime.now()
        print("Current timestamp:", date_now.strftime('%Y-%m-%d %H:%M:%S.%f'))
        # print("Current timestamp:", date_now.isoformat(sep=' ', timespec='milliseconds'))
        function(*args)
        print()
    return wrapper

@timestamper
def adder(num1, num2):
    print("{} plus {} equals {}".format(num1, num2, num1+num2))

@timestamper
def multr(num1, num2):
    print("{} times {} equals {}".format(num1, num2, num1*num2))

adder(5, 3)
multr(4, 7)