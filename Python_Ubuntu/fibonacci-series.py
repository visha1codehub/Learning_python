try:
   nterms = int(input("Enter the terms:"))

   num1 = 0
   num2 = 1
   nextnum = 0
   count = 0

   if nterms <= 0:
    print("Zero is not allowed, please enter a valid number >= 1 !")
   else:
    print("Fibonacci sequence:")
   while count < nterms:
      print(nextnum)
      nextnum = num1 + num2
      num1 = num2
      num2 = nextnum

      count += 1
except ValueError:
   print("Not a valid number, please enter a valid number !")

