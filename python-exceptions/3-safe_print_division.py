#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print ("zero devision error ")
    except Exception as e:
        return print(e)
    finally:
        print("we got here")
