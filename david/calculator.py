from typing import Callable
import math

def add(a: int, b: int) -> float:
    return float(a + b)

def subtract(a: int, b: int) -> float:
    return float(a - b)

def multiply(a: int, b: int) -> float:
    return float(a * b)

def divide(a: int, b: int) -> float:
    if (b == 0):
        raise ValueError('Error: Division by zero.')
    return float(a / b)

# def to_float(user_input: str, none_zero: bool = False) -> float:
def to_int(user_input: str) -> int:
    val = user_input.strip().lower()

    constants = {
        'e': math.e,
        'pi': math.pi,
        'tau': math.tau,
    }

    try:
        if val in constants:
            return int(constants[val])
        return int(val)
    except:
        raise ValueError('Invalid number input.')

def to_operater(user_input: str) -> Callable[[float, float], float]:
    val = user_input.strip().lower()

    constants = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    try:
        return constants[val]
    except:
        raise ValueError('Invalid operator.')

def main():
    try:
        a = to_int(input('Enter expression: '))
        b = to_int(input('Enter Second Number: '))
        o = to_operater(input('Enter Operator (Allowed Type: +-*/): '))
        print(f'Result: <{o(a, b)}>')
    except ValueError as error:
        print(error)

if __name__ == '__main__':
    main()
