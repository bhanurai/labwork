#Write a Python program to sum three given integers. However, if two or more values are equal sum will be zero.

a=10
b=15
c=20
if a==b or a==c:
    print('0')
else:
    print(f"sum of three number is {a+b+c}")