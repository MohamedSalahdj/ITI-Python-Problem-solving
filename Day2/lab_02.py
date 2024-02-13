'''
Fill an array of 5 elements from the user, 
Sort it in descending and ascending orders then display the output.
'''
def task_one():
    print("--"*15, 'task-02', "--"*15)
    l = [int(input(f"Enter only number'{i+1}': ")) for i in range(5)]
    l.sort()
    print(f"sort it ascending {l}")
    l.sort(reverse=True)
    print(f"sort it descending {l}")

    print(l)
# task_one()


''' 
Write a program that generate a multiplication table from 1 to the
number passed
'''

"""
    [1]             1*1
    [2,4]          2*1, 2*2
    [3,6,9]        3*1, 3*2, 3*3

"""

def task_two(): 
    tables_lists = []
    number = input("Enter table number will stoped it: ")
    number =  int(number) if number.isdigit() else task_two()
    for i in range(1, number+1):
        table= []
        for j in range(1,i+1):
            table.append(i*j)
        tables_lists.append(table)
    return tables_lists
# print(task_two())


'''
Write a function that accepts two arguments (length, start) to
generate an array of a specific length filled with integer numbers
increased by one from start.
'''

def task_three(length, start):
    array_of_integer = [ number for number in range(start, start+length)]
    return array_of_integer

# print(task_three(3,7))


"""write a function that takes a number as an argument and if the
number divisible by 3 return "Fizz" and if it is divisible by 5 return
"buzz" and if is is divisible by both return "FizzBuzz"""

def task_four(number):
    return "FizzBuzz" if number % 3 == 0 and  number % 5 ==0 else "Fizz" if number % 3 ==0 else 'buzz' if number % 5 == 0 else "not divisiable by '5' or '3'"

# print(task_four(2))


"""
    Write a function which has an input of a string from user then it
    will return the same string reversed.
"""

def task_five():
    string = input("Enter string ")

    return string[::-1]

# print(task_five())


import re

"""
    Ask the user for his name then confirm that he has entered his
    name(not an empty string/integers). then proceed to ask him for
    his email and print all this data (Bonus) check if it is a valid email
    or not
"""
def task_six():
    name = input("Enter your name: ")
    if name.isalpha() and not name.isspace():
        print("\tname vaild")
    else:
        print("Your name is not vaild\n")
        task_six()

    email = input("Enter your email: ") 
    return f"name: {name} \nemail: {email}"

# print(task_six())


"""
    Write a function that takes a string and prints the
    longest alphabetical ordered substring occurred For example, if
    the string is 'abdulrahman' then the output is: Longest substring in
    alphabetical order is: abdu
"""

def task_seven(string):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dict = {}
    word = ''
    for i in range(len(string)-1):
        if letters.index(string[i]) < letters.index(string[i+1]):
            word+=string[i]
        else:
            word+=string[i]
            dict[len(word)] = word
            word=''
    keys = list(dict.keys())
    return dict[max(keys)]
print(task_seven('abdulrahman'))