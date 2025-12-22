#simple calculator
select = input("select the operations from 1,2,3,4:")
num_1 = int(input("enter first number:"))
num_2 = int(input("enter second number:"))
if select == '1':
    print("addition=", num_1, "+", num_2, "=", num_1 + num_2)
elif select == '2':
    print("difference=", num_1, "-", num_2, "=", num_1 - num_2)
elif select == '3':
    print("product=", num_1, "*", num_2, "=", num_1 * num_2)
elif select == '4':
    print("division=", num_1, "/", num_2, "=", num_1 / num_2)
else:
    print("invalid input")