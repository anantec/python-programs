a= int(input("Enter the first number\n"))
b= int(input("Enter the second number\n"))

print(f'the value of a is {a} and b is {b}\n')

temp = a
a=b
b=temp

print(f'after swapping the value of a is {a} and b is {b}')