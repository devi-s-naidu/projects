print("choice 1 to find sum and average of squares")
print("choice 2 to find sum and average of cubes")
userinput = int(input("enter your choice:"))
if userinput == 1:
 sum = 0
 square = 0
 print("please enter 10 numbers")
 for i in range(1, 11):
    num = int(input("number %d="%i))
    square = (num*num)
    sum = sum+square
    avg = sum/10
    print("square=", square)
    print("sum=", sum)
    print("average=", avg)
if userinput == 2:
 sum=0
 cube=0
 print("please enter 10 numbers")
 for i in range(1, 11):
    num = int(input("number %d="%i))
    cube = (num*num*num)
    sum = sum+cube
    avg = sum/10
    print("cube=", cube)
    print("sum=", sum)
    print("average=", avg)