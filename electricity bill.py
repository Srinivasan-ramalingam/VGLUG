units = int(input("Enter units consumed: "))
connection_type = input("Enter connection type: ")

if connection_type == "Non-Commercial":

    if units <= 200:
        bill = 0

    elif units <= 500:
        bill = (units - 200) * 4

    elif units <= 2000:
        bill = units * 8

    else:
        bill = units * 10

elif connection_type == "Commercial":

    if units <= 500:
        bill = units * 6

    elif units <= 1000:
        bill = units * 9

    elif units <= 5000:
        bill = units * 12

    else:
        bill = units * 15

else:
    bill = 0
    print("Invalid connection type")

print("Total Bill: ₹", bill)