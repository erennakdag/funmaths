from flask import render_template, redirect, request, session
from random import randint
import math


actual_answer = []


def add(correct=-1):
    
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    actual_answer.append((num1 + num2, '/addition'))
    return render_template("operations_layout.html", title="Addition", correct=correct, operator="+", color='aquamarine', num1=num1, num2=num2, operation='add')


def subt(correct=-1):
    
    num2 = randint(0, 100)
    num1 = randint(num2, 100)
    actual_answer.append((num1 - num2, '/subtraction'))
    return render_template("operations_layout.html", title="Addition", correct=correct, operator="-", color='yellow', num1=num1, num2=num2, operation='subt')


def mult(correct=-1):
    num1 = randint(0, 50)
    num2 = randint(0, 20)
    actual_answer.append((num1 * num2, '/multiplication'))
    return render_template("operations_layout.html", title="Multiplication", correct=correct, operator="×", color='red', num1=num1, num2=num2, operation='mult')


def divd(correct=-1):
    num1 = randint(0, 100)
    num2 = randint(1, 20)
    actual_answer.append((num1 // num2, '/division'))
    return render_template("operations_layout.html", title="Division", correct=correct, operator="÷", color='mediumpurple', num1=num1, num2=num2, operation='divd')
