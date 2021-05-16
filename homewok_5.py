try:
    my_f = open('111.txt', 'r', encoding = 'utf-8' )
    my_f = my_f.read()
    my_f = my_f.lower()
    my_f = my_f.replace(' ', '')
    the_count = my_f.count('the')
    if_count = my_f.count("if")
    e_count = my_f.count("e")
    print('good, done')
except IOError:
    if_count = 0
    the_count = 0
    e_count = 0
    print("sorry, File have not founded ")
my_f1 = open("statistics.txt", "w")
my_f1.write("count_'the' = " + str(the_count) +'\n')
my_f1.write("Count_'if' = " + str(if_count) + '\n')
my_f1.write("Count_'e'= " + str(e_count))

my_f1.close()
