dict1={"a":1,"b":2,"c":2,"d":2,"e":5}

k=2
x=0

for key in dict1:
    if dict1[key]==k:
        x=x+1

print(x)