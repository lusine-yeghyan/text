#1
number = '12345'
number = int(number)
print(12345 // 10000)
print(12345 // 1000 % 10)
print(12345 // 100 % 10)
print(12345 // 10 % 10)
print(12345 % 10)


# #2 count
string = input('enter string: ')
count = len(string)
print(count)

#3 prime or not

number = int(input("Enter int number: "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime")
            break
    else:
        print(number, "is a prime")
else:
    print(number, "is not a prime")

#4
for i in range (1, 6, 1):
    print(i + "." + " 000")

#5
number1 = float (input('enter number_1: '))
number2 = float (input('enter number_2: '))
number3 = float (input('enter number_3: '))
if number1 + number2 == number3 or number1 + number3 == number2 or number2 + number3 == number1:
    print('yes')
else:
    print('no')


#6
x = 14
sum = 0
for i in range(1, x + 1, 1):
    sum += i
print("Sum of numbers = ", sum)


