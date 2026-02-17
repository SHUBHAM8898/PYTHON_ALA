print("Simple Calculator")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("1.Add 2.Sub 3.Mul 4.Div")
choice = int(input("Choose option: "))
if choice == 1:
result = a + b
elif choice == 2
result = a - b
elif choice == 3:
result = a * b
elif choice == 4:
result = a / b
else:
print("Invalid choice")
print("Result:", result)
if result > 0:
print("Positive result")
else:
print("Negative result")
