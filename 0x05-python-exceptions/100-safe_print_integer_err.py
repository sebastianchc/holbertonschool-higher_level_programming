#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}" .format(value))
        return True
    except Exception as Errors:
        print("Exception: {}" .format(Errors), file=sys.stderr)
        return False
