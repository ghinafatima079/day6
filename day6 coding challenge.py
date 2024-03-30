# Python Program to Find the Square Root
sq=int(input("Enter a number:"))
sq_root=sq**0.5
print(f"The square root of {sq} is {sq_root}.")

# Python Program to Find the Largest Among Three Numbers
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))
if num1>num2 and num1>num3:
    largest=num1
elif num2>num1 and num2>num3:
    largest=num2
else:
    largest=num3
print(f"The latgest among the three numbers is {largest}")

# Python Program to Solve Quadratic Equation
print("A quadratic equation is of the form ax^2 + bx + c")
a=int(input("Enter coefficient a:"))
b=int(input("Enter coefficient b:"))
c=int(input("Enter coefficient c:"))
d=(b**2)-(4*a*c)
if d==0:
    print("print the roots are real and equal")
    print(f"The roots of the quadratic equation are {-b/(2*a)} and {-b/(2*a)}.")
elif d>0:
    print("print the roots are real and distinct")
    r1=(-b+(d**0.5))/(2*a)
    r2=(-b-(d**0.5))/(2*a)
    print(f"The roots of the quadratic equation are {r1} and {r2}.")
else:
    print("print the roots are imaginary")

# Python Program to Convert Celsius To Fahrenheit
fahrenheit=float(input("Enter the temperature in fahrenheit:"))
celcius=(fahrenheit*1.8)+32
print(f"The temperature in celcius is {celcius}.")