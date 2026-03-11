#write a code that reads 10 numbers
#inserts the odd and even number in 2 different lists.
#When finished, print the 2 lists
odd_numbers = []
even_numbers = []
for i in range(10):
    num = int(input("Enter number:"))
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

