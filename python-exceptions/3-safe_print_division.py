#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except Exception:
        return None
    finally:
        try:
            print("Inside result: {}".format(result))
        except Exception:
            print("Inside result: None")
