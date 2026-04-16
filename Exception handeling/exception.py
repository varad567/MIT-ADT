try : 
    A = int(input("Enter a number : "))
   
    T = A/2

except ZeroDivisionError :
    print("You cannot divide by zero")

except ValueError :
    print("You must enter a number")

else :
    print("The half of the number is : ", T)

finally :
   pass
