print("hello,I am a chatbot")
print("how may i help you\n")
print("hit 1 to apply voter ID")
print("hit 2 for modify voter ID")
#accepting our request
userinput = int(input("enter your choice:"))
#using nested if to process the user input
if userinput == 1:
    inputneeded = int(input("enter the age of the candidate"))
    if (inputneeded >= 18):
      print("enter your details")
    else:
      print("not eligible for voting")
else:
  print("provide details for modification")
print("thank you for accepting our service ,we will get back to you soon")