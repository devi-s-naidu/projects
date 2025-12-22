#creating a quiz
print("hello, welcome to quiz mania!")
name=input("provide your name : ")
one=input("who is the president of India?\n a)Droupadi murmu\n(b)Dr.Rajendra Prasad\n(c)pratibha Devisingh patil\n(d)A P J Abdul kalam")
two=input("how many districts are there in karnataka?\n(a)31\n(b)30\n(c)29\n(d)28")
three=input("what is the capital of India?\n(a)New Delhi\n(b)Bangalore\n(c)Tamil nadu\n(d)Odisha")
firstanswer=['a','(a)','Droupadi murmu']
secondanswer=['a','(a)','31']
thirdanswer=['a','(a)','New Delhi']
print("")
if one in firstanswer:
    print("1.Correct")
else:
    print("1.Incorrect")
if two in secondanswer:
    print("2.Correct")
else:
    print("2.Incorrect")
if three in thirdanswer:
    print("3.Correct")
else:
    print("3.Incorrect")
    print("")

print("Thank you "+name+" for playing this quiz!")
