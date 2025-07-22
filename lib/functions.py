#!/usr/bin/env python3

def greet_programmer():
    """
    Takes no arguments and outputs "Hello, programmer!" to the terminal.
    """
    print("Hello, programmer!")


def greet(name):
    """
    Takes one argument (name) and outputs "Hello, name!" to the terminal.
    """
    print(f"Hello, {name}!")


def greet_with_default(name="programmer"):
    """
    Takes one argument (name) with a default value of "programmer".
    Outputs "Hello, name!" to the terminal.
    If no argument is passed, outputs "Hello, programmer!".
    """
    print(f"Hello, {name}!")


def add(num1, num2):
    """
    Takes two numbers as arguments and returns their sum.
    """
    return num1 + num2


def halve(number):
    """
    Takes one number as an argument and returns that number divided by two.
    """
    return number / 2
