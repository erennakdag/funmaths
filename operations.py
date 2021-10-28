from flask import render_template
from random import randint


compare = []


def add(iscorrect=-1):
    
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    compare.append((num1 + num2, '/addition'))
    return render_template("operations.html", title="Addition", iscorrect=iscorrect, operator="+", color='aquamarine', num1=num1, num2=num2, operation='add')


def subt(iscorrect=-1):
    
    num2 = randint(0, 100)
    num1 = randint(num2, 100)
    compare.append((num1 - num2, '/subtraction'))
    return render_template("operations.html", title="Addition", iscorrect=iscorrect, operator="-", color='yellow', num1=num1, num2=num2, operation='subt')


def mult(iscorrect=-1):
    num1 = randint(0, 50)
    num2 = randint(0, 20)
    compare.append((num1 * num2, '/multiplication'))
    return render_template("operations.html", title="Multiplication", iscorrect=iscorrect, operator="×", color='red', num1=num1, num2=num2, operation='mult')


def divd(iscorrect=-1):
    num1 = randint(0, 100)
    num2 = randint(1, 15)
    compare.append(num1 % num2)
    compare.append((num1 // num2, '/division'))
    return render_template("divd.html", title="Division", iscorrect=iscorrect, operator="÷", color='mediumpurple', num1=num1, num2=num2, operation='divd')
