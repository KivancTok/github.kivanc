# Links
[GitHub](https://github.com/KivancTok) - [Youtube](https://youtube.com/user/atakanntok)
# Pyhton Examples
## Basic
A script that prints `Hello world!` into your python console:
```py
print("Hello world!")
```

Find the reamainder if it's `0` or `1` and show it:
```py
i = 0
print(i%2)
```
## Complicated
Calculator:
```py
import math
print("Calculator 2.9")
print("Start of Main Calculator")

print("Multiplication")
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
print("Addition")
n4 = int(input("Number 1: "))
n5 = int(input("Number 2: "))
n6 = int(input("Number 3: "))
print(f'Multiplication: {n1*n2*n3}, Addition: {n4+n5+n6}')

print("End Of Main Calculator")
print("Start of Secondary Calculator")

print("Division")
n7 = int(input("Number 1: "))
n8 = int(input("Number 2: "))
n9 = int(input("Number 3: "))
print("Subtraction")
n10 = int(input("Number 1: "))
n11 = int(input("Number 2: "))
n12 = int(input("Number 3: "))
print(f'Division: {n7/n8/n9}, Subtraction:, {n10-n11-n12}')

print("End Of Secondary Calculator")
print("Start of Trinary Calculator")

print("... Power Of ...")
n13 = int(input("Number 1: "))
n14 = int(input("Number 2: "))
print("Square Root Of ...")
n15 = int(input("Number to divide to its square root: "))
print('Factorial Of...')
n16 = int(input('Number to factorize: '))
print(f'Powered Number: {n13**n14}, Square Root: {math.sqrt(n15)}, Factorial: {math.factorial(n16)})
```
