# 1
def count_of_characters(string):
    count = 0
    for any_num in string:
        if any_num != ' ':
            count += 1
    return count


print(count_of_characters('salvador dali'))


def count_string(str):
    count = 0
    for i in range(0, len(str)):
        if (str[i] != ' '):
            count = count + 1
    return count


print(count_string('mandala'))


# 2
def char_string(str, char):
    count = 0
    for i in range(len(str)):
        if (str[i] == char):
            count = count + i
    return count


print(char_string('dali', 'l'))


# 3
def factorial(x):
    p = 1
    for i in range(1, x + 1):
        p = p * i
    return p


print('x! = ', factorial(3))


# 4
def odd_or_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def number_by3(number):
    if odd_or_even(number) == True:
        return number ** 3
    else:
        return 'enter even number'


print('even number **3 =', number_by3(4))
