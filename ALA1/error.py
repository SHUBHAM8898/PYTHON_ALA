print("Simple Calculator")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("1.Add 2.Sub 3.Mul 4.Div")
choice = int(input("Choose option: "))

if choice == 1:
result = a + b   # Error: No indentation
elif choice == 2  # Error: Missing colon :
result = a - b   # Error: No indentation
elif choice == 3:
result = a * b   # Error: No indentation
elif choice == 4:
result = a / b   # Error: No indentation
else:
print("Invalid choice")   # Error: No indentation

print("Result:", result)

if result > 0:
print("Positive result")   # Error: No indentation
else:
print("Negative result")   # Error: No indentation
