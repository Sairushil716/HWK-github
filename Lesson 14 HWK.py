
userint=input("Please enter the shut-down password.")
def shutdown(x):
    if x=="1234":
        print("Shutiing down...")
    else:
        print("That is not the password. Try again.")
        userint=input("Please enter the shut-down password.")
        shutdown(userint)


shutdown(userint)

