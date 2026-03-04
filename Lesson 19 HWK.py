prime=[]
even=[]
odd=[]
lowerrange=int(input("Enter the lower range."))
upperrange=int(input("Enter the upper range."))

isitprime=True

for i in range(lowerrange,upperrange+1):
    for x in range(2,i):
        if i/x==i//x:
            isitprime=False
            break
    else:
        prime.append(i)

if 1 in prime:
    prime.remove(1)

print(prime)

for i in prime:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("The even prime numbers in your boundaries are:",even)
print("The odd prime numbers in your boundaries are:",odd)