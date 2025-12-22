# lets start import the module
import math


# let's give a class name whatever you want i am going to give same name to this file

class Calc(object):

    def add(self, num1, num2):
        answer = num1 + num2
        print("Sum=", answer)

    def sub(self, num1, num2):
        answer = num1 - num2
        print("Difference=", answer)

    def mul(self, num1, num2):
        answer = num1 * num2
        print("mul=", answer)

    def div(self, num1, num2):
        answer = num1 / num2
        print("Division=", answer)

    def sinrad(self, num):
        answer = math.sin(num)
        # this method sin() returns the sine of x in radians.
        # print(sin(4))
        # it will print -0.75680..
        print("sin(%f) =% f" % (num, answer))

    def cosrad(self, num):
        answer = math.cos(num)
        print("cosine(%f)=%f" % (num, answer))
        # %f will input convert to a float value and its returns a float value

    def tanrad(self, num):
        answer = math.tan(num)
        print("tan(%f)=%f" % (num, answer))

    def secrad(self, num):
        answer = 1 / (math.sin(num))
        print("sec(%f)=%f" % (num, answer))

    def cotrad(self, num):
        answer = 1 / (math.sin(num))
        print("cot(%f)=%f" % (num, answer))

    def sindeg(self, num):
        answer = math.sin(math.radians(num))
        print("sin(%f) in Degree=%f" % (num, answer))

    def cosdeg(self, num):
        answer = math.cos(math.radians(num))
        print("cos(%f) in Degree=%f" % (num, answer))

    def tandeg(self, num):
        answer = math.tan(math.radians(num))
        print("tan(%f) in Degree=%f" % (num, answer))

    def cosecdeg(self, num):
        answer = 1 / math.sin(math.radians(num))
        print("cosec(%f) in Degree=%f" % (num, answer))

    def secdeg(self, num):
        answer = 1 / math.cos(math.radians(num))
        print("sec(%f) in Degree=%f" % (num, answer))

    def cotdeg(self, num):
        answer = 1 / math.tan(math.radians(num))
        print("cot(%f) in Degree=%f" % (num, answer))

    def ln(self, num):
        answer = math.log(num)
        print("ln(%f)=%f" % (num, answer))

    def logten(self, num):
        answer = math.log10(num)
        print("log10(%f)=%f" % (num, answer))

    def logbasex(self, num):
        answer = math.log(num, 'x')
        print("log base(%f)(%f)=%f" % ('x', num, answer))

    def squareroot(self, num):
        answer = math.sqrt(num)
        print("square root(%f)=%f" % (num, answer))

    def pie(self):
        print('pi=', math.pi)

    def powerof(self, num, raiseby):
        answer = math.power(num, raiseby)
        print("%f^(%f)=%f" % (num, raiseby, answer))

        # now we have completed all the fuctions and lets call those by input


'from Calc' 'import Calc'

cal = Calc()
print('welcome to my calculator')
print('here is the list of choice:')
print('-' * 20)
print("1: Addition \t\t 12 : Sine in degrees")
print("2: Subtraction \t\t 13 : Cosine in degrees")
print("3: Multiplication \t\t 14 : Tan in degrees")
print("4: Division \t\t 15 : Co secant in degrees")
print("5: Sine in radians\t 16 : Secant in degrees")
print("6: Cosine in radians\t 17 : Cot in degrees")
print("7: Tangent in radians\t 18 : Natural log")
print("8: Co secant in radians\t 19 : Base 10 log")
print("9: Secant in radians\t 20 : Log base 'x'")
print("10: Cotangent in radians\t 21 : square root")
print("11: pi \t\t 22 : Power of")
print('-' * 20)
choice = ""
while True:
    try:
        choice = int(input('Enter a number of choice:'))
    except:
        print("Enter a valid number:")
    if choice == 1:
            n1 = float(input("Enter the first number to add:"))
            n2 = float(input("Enter the second number to add:"))
            cal.add(n1, n2)
    if choice == 2:
            n1 = float(input("Enter the first number to subtract:"))
            n2 = float(input("Enter the second number to subtract:"))
            cal.sub(n1, n2)
    if choice == 3:
            n1 = float(input("Enter the first number to multiply:"))
            n2 = float(input("Enter the second number to multiply:"))
            cal.mul(n1, n2)
    if choice == 4:
            n1 = float(input("Enter the first number to divide:"))
            n2 = float(input("Enter the second number to divide:"))
            cal.div(n1, n2)
    if choice == 5:
            n = float(input("Enter to find its Sine in radians:"))
            cal.sinrad(n)
    if choice == 6:
            n = float(input("Enter to find its Cosine in radians:"))
            cal.cosrad(n)
    if choice == 7:
            n = float(input("Enter to find its Tangent in radians:"))
            cal.tanrad(n)
    if choice == 8:
            n = float(input("Enter to find its Co secant in radians:"))
            cal.cosecrad(n)
    if choice == 9:
            n = float(input("Enter to find its Secant in radians:"))
            cal.secrad(n)
    if choice == 10:
            n = float(input("Enter to find its Cotangent in radians:"))
            cal.cotrad(n)
    if choice == 11:
            cal.pie()
    elif choice == 12:
            n = float(input("Enter to find its Sine in degrees:"))
            cal.sindeg(n)
    elif choice == 13:
            n = float(input("Enter to find its Cosine in degrees:"))
            cal.cosdeg(n)
    elif choice == 14:
            n = float(input("Enter to find its Tangent in degrees:"))
            cal.tandeg(n)
    elif choice == 15:
            n = float(input("Enter to find its Co secant in degrees:"))
            cal.cosecdeg(n)
    elif choice == 16:
            n = float(input("Enter to find its Secant in degrees:"))
            cal.secdeg(n)
    elif choice == 17:
            n = float(input("Enter to find its Cotangent in degrees:"))
            cal.cotdeg(n)
    elif choice == 18:
            n = float(input("Enter to find its natural log:"))
            cal.ln(n)
    elif choice == 19:
            n = float(input("Enter to find its Base 10 log:"))
            cal.logbasex(n)
    elif choice == 20:
            n1 = float(input("Enter a base value:"))
            n2 = float(input("Enter a number to find its log to the given log value:"))
            cal.logbasex(n1, n2)
    elif choice == 21:
            n = float(input("Enter to find its Square root:"))
            cal.squareroot(n)
    elif choice == 22:
            n1 = float(input("Enter a number:"))
            n2 = float(input("Enter its power:"))
            cal.powerof(n1, n2)
else:
    print("WARNING:Please enter a valid input")
