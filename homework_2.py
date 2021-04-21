#1
def is_palindrome (string):
    reserve_str = string[::-1]
    if reserve_str == string:
        print('the string is palindrome')
    else:
        print('the string is not palindrom')
result = is_palindrome('gis')
print(result)

#2
# V = 4/3⋅πR3
def V_sphere (R, pi = 3.14):
    V = 4 / 3 * pi * R**3
    return V
print('the volume of a sphere =', V_sphere(5))

#3
def show_employee_basic_data (name, age):
    print(name, age)

show_employee_basic_data ("Lusine", 26)

#4
def show_employee(name, surname, salary = 9000):
    print(name,  surname, salary)

show_employee("lusine", "Yeghiyan")
show_employee("vahag", 'avetisyan', 5000)

#5
def show_whole_employee_info ():
    show_employee_basic_data('lusine', 25)
    show_employee('armen', 'avetisyan', 500000)
show_whole_employee_info()