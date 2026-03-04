result=int(input("Enter baby age"))



try:
   
    odd=result/2

    if result>10:
        print("The baby is older than 10")
    else:
        print("The baby is younger than 10")

except ValueError:
    print("Please enter a numerical value")
except ZeroDivisionError:
    print("A number cannot be divisible by 0")

finally:
    print("hi hello and hi")