#print("***** *****\n****   ****\n***     ***\n**       **\n*         *")

character=input("Enter a character for the downwards pyramid.")
rows=int(input("Enter a number for how many rows in the pyramid."))
spaces=0
numberofcharacters=0
numberofspaces=1

for i in range(0,rows):
    numberofcharacters=rows-spaces
    print(character * numberofcharacters,)
    spaces=spaces+1
    numberofspaces=numberofspaces+2

    

