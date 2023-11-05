import time as t

double = lambda x: x * 2

def doubleArray(x):
    y = x.copy()
    for i in range(len(y)):
        y[i] = double(y[i])
    return y 

numbers = []

while True:
    try:
        global elements
        elements = int(input("Enter how many elements are going to be in the list: "))
        break
    except ValueError:
        print("\nInvalid input. Please enter an integer.")

try:
    for i in range(elements):
        global num
        num = int(input(f"Enter element {i + 1}: "))
        numbers.append(num)
        print(f"The numbers are: {numbers}")
    print(f"Doubled Array - {doubleArray(numbers)}")

except ValueError:
    print("You have entered an invalid input")
    for i in range(5, 0, -1):
        print(i, "...")
        t.sleep(1)
