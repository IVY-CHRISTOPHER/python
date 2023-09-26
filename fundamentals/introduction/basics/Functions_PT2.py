x = 3
def countdown(x):
    my_list=[]
    if x <= 0:
        print(str(0) + " done")
    elif x > 0:
        for x in range(x,-1,-1):
            my_list.append(x)
        return my_list
my_list=countdown(x)
print(my_list)

def print_and_return(a,b):
        print(a)
        return b
print_and_return(1, 2)

def first_plus_length(x):
    my_list=[]
    my_list=x
    x = my_list[0] + len(my_list)
    print(x)
first_plus_length([5,8,7,6])

# WIP ----------------------------------
def values_greater_than_second(a):
    my_list = []
    my_list = a
    if len(a) <= int(2):
        print("False")
    elif len(a) > int(2):
        print(len(my_list))
        print(my_list)
values_greater_than_second([1,2,3,4])
# WIP -----------------------------------

def length_and_value(a,b):
    my_list = []
    a == len(my_list)
    my_list == b
    print(my_list)
length_and_value(5, 1)