x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


# Problem 1
print('----Problem 1-----')
print(x[1])

print(x[1][0])

x[1][0] = 15

print(x[1])

# Problem 2
print('----Problem 2-----')
print(sports_directory['basketball'])

print(sports_directory['basketball'][1])

sports_directory['basketball'][1] = 'Bryant'

print(sports_directory['basketball'])

# Problem 3
print('----Problem 3-----')

sports_directory['soccer'][0] = 'Andres'

print(sports_directory['soccer'])

# Problem 4
print('----Problem 4-----')

print(z)

print(z[0]['y'])

z[0]['y'] = 30

print(z)
print('----------')
print('Next Questions')

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(dict):
    for i in range(0, len(dict)):
        for key,val in dict[i].items():
            print(f'{key}  {val}')

iterateDictionary(students)

def iterateDictionary2(input,dict):
    for i in range(0, len(dict)):
        for key,val in dict[i].items():
            if key == input:
                print(val)

print('---------')
print('First Names')
print('--------')
iterateDictionary2('first_name',students)
print('--------')
print('Last Names')
print('---------')
iterateDictionary2('last_name', students)

print('---------')
print('---------')
print('---------')
print('---------')
print('---------')

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printinfo(list):
    for key,val in list.items():
        print(f'{len(key)} {key}')
        print('---------')
        for i in range(0, len(val)):
            print(val[i])

printinfo(dojo)

