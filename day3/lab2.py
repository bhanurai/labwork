# WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction,
# more than 60% –> first, more than 40% –> pass, less than 40% –> fail 

a=int(input('enter your mark of maths'))
b=int(input('enter your mark of physics'))
c=int(input('enter your mark of chemistry'))
d=int(input('enter your mark of biology'))
e=(a+b+c+d)/400*100
if e>70:
    print('distinction')
elif e>60:
    print("first")
elif e>=40:
    print('pass')
else :
    print('fail')
