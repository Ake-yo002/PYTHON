#A basic calculator program
#Start by prompting the user to enter the numbers and operation

n=float(input("Enter the first number:"))
m=float(input("Enter the second number:"))
s=input("Enter the mathematical operation:")

#Check the operation, compute and print the results
if s == "+":
    z=n+m
    print(f"{n} + {m} ={z}")
elif s == "-":
    z=n-m
    print(f"{n} - {m} ={z}")
elif s == "/":
    z=n/m
    print(f"{n} / {m} ={z}")
elif s == "*":
    z=n*m
    print(f"{n} * {m} ={z}")
else:
    print("Error!!")