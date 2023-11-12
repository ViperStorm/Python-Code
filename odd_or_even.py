import time

def oddOrEven():
    Choicenumber = input("Enter a number to see if it is odd or even: ")
    try:
        Choicenumber = int(Choicenumber)
        if Choicenumber % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd")
    except:
        print("You entered an invalid input " , Choicenumber , ". you will be terminated")
        for i in range(5, 0, -1):
            print(str(i) + "...")
            time.sleep(1)

oddOrEven()
