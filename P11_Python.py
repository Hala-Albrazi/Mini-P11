print("Welcome to Multiplication table:")
NU = int(input("Please enter a number \n"))
print(f"Here is the multiplication table for number {NU}")
for i in range (1,11):
    result = NU * i
    print(f"{NU} x {i} = {result}")