userbill=int(input("Enter your bill"))
userpaid=int(input("How much did you pay?"))
due=0

def bill(x,y):
    if x>y:
        due=x-y
        print("The shop has to return ",due)
    else:
        due=y-x
        print("You still have to pay ",due)

bill(userpaid,userbill)

