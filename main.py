# Calculator in python

# Taking integers as input
x = int(input("Enter first Integer: "))
y = int(input("Enter second Integer: "))

# Add, Sub, Mul or Div?
op = ["Type '1' for addition ", "Type '2' for subtraction ", "Type '3' for multiplication", "Type '4' for division "]
for item in op:
    print(item)

choice = int(input("Enter choice(1/2/3/4): "))

# Answer of calculation
if choice == 1:
    print(f"Answer is {x + y}")

elif choice == 2:
    print(f"Answer is {x - y}")

elif choice == 3:
    print(f"Answer is {x * y}")

elif choice == 4:
    print(f"Answer is {x / y}")

# if not valid raise value error
else:
    print("Invalid Input! Try again")

# end..
