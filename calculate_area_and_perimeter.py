import time

play = input("Do you want to play? - (y/n)").lower().strip()
if play != "y":
    print("Guess you're not playing.")
    quit()

def calculateAreaofRectangle(length, width):
    return length * width

def calculatePerimeterofRectangle(length, width):
    return 2 * (length + width)

def length():
    global length
    length = float(input("Enter your length number: "))

def width():
    global width
    width = float(input("Enter your width number: "))

def game_over():
    print("Invalid choice")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Ya been BOOTED!!!")

choice1 = input("Enter your choice, area/perimeter (enter a or p): ").lower().strip()

while True:
    if choice1 == "a":
        print("\nOk!")
        length()
        width()
        print("The area of your rectangle is ", calculateAreaofRectangle(length, width))
        break
    elif choice1 == "p":
            print("Ok!")
            length()
            width()
            print("The Perimeter of your rectangle is ", calculatePerimeterofRectangle(length, width))
            break
    else:
        game_over()
        break