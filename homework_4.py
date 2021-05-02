#1
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = [list1[0] + list2[0], list1[1] + list2[1], list1[2] + list2[2], list1[3] + list2[3]]
print(list3)

#2
a = [5, 6, 56]
for i in range(len(a)):
    print('index =', i, '= value = ',  a[i], '=', a[i]**2)

#3
sum = 0
my_list = [10, 5, 17, 20, 23]
for i in range(0, len(list1)):
    sum = sum + my_list[i]
print("Sum of my_list's elements = ", sum)

#4
a = [10, 30, 5, 5, 6, 6]
b = []
for i in a:
    if i not in b:
        b.append(i)
print('remove duplicate = ', b)

#5
list_1 = [15, 25, 100, 20, 65, 12, 25]

list_out = []
for i in list_1:
    if i not in list_out:
        list_out.append(i)

for i in list_out:
    print("Unique element of the list = ", i)
