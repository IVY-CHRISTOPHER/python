
# Prints 1 - 150
for i in range(151):
    print(i)

# prints 5 - 1000 in multiples of 5
for i in range(0, 1005, 5):
    print(i)

# prints 1-100 where 5 = Coding and 10 = Coding Dojo
for i in range(1, 101):
    if i % 10 == 0:
        print('Coding Dojo')
    elif i % 5 == 0:
        print('Coding')
    else:
        print(i)

#prints all odd numbers of 500000 added together
x = 0
for i in range(1, 500001, 2):
    x += i
print(x)

# Prints 2018 - 0 by 4s
for i in range(2018, 0, -4):
    print(i)

# Prints lownum - highnum only showing mult.
lownum = 3
highnum = 255
mult = 5

for i in range(lownum,highnum, + 1):
    if i % mult == 0:
        print(i)