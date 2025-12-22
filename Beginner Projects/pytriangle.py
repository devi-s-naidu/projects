lastnumber = int(input("enter the last number"))
for row in range(1, lastnumber):
    for column in range(1, row+1):
        print(column, end='')
    print("")