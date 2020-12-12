num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))
print("Prime numbers between", num1, "and", num2, "are:")

for num in range(num1, num2):

   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break2

       else:
           print(num)