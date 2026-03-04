import random

password=[]

letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

numbers=["1","2","3","4","5","6","7","8","9","0"]
x=0
y=0
abc=""

a=random.randint(8,16)



for i in range(1,a):
    b=random.randint(1,2)
    c=random.randint(1,2)
    if b==1:
        if c==1:
            x=random.randint(0, 25)
            y=(letters[x]).upper()
            password.append(y)
        else:
            x=random.randint(0, 25)
            y=letters[x]
            password.append(y)
    else:
        x=random.randint(0,9)
        y=numbers[x]
        password.append(y)

for i in password:
    abc=i+abc

print(abc)
            
            


