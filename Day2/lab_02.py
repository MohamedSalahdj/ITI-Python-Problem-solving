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
    if number.isdigit():
        number = int(number) 
    else:
        task_two()
        # number = ''
        # return tables_lists
    for i in range(1, number+1):
        table= []
        for j in range(1,i+1):
            table.append(i*j)
        tables_lists.append(table)
    return tables_lists
print(task_two())


'''
    Write a function that accepts two arguments (length, start) to
    generate an array of a specific length filled with integer numbers
    increased by one from start.
'''

def task_three(length, start):
    array_of_integer = [ number for number in range(start, start+length)]
    return array_of_integer

# print(task_three(3,7))


"""
    write a function that takes a number as an argument and if the
    number divisible by 3 return "Fizz" and if it is divisible by 5 return
    "buzz" and if is is divisible by both return "FizzBuzz
"""

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
def is_email_vaild(email):
    email_pattern = r'^[\w\.-]+@[a-zA-Z]+\.[a-zA-Z]{3,}$'
    return f"\t--- Your mail '{email}' is vaild" if re.match(email_pattern, email) is not None else f"\t---- Your email '{email}' is not vaild"

def task_six():
    name = input("Enter your name: ")
    if name.isalpha() and not name.isspace():
        print("\tname vaild")
    else:
        print("Your name is not vaild\n")
        task_six()
    email = input("Enter your email: ") 
    print(is_email_vaild(email))
    return f"This your data entered\nname: {name} \nemail: {email}"

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
# print(task_seven('abdulrahman'))


"""
    Write a program which repeatedly reads numbers until the user
    enters “done”.
        ○ Once “done” is entered, print out the total, count, and
        average of the numbers.

        ○If the user enters anything other than a number, detect their
        mistake, print an error message and skip to the next number.
"""

def task_eight():
    count = 0
    total = 0
    while True:
        number = input("Enter a number ")
        if number == "done":
            print(f"total= {total} count={count} avg={total/count}")
            break
        elif number.isdigit():
            number =  int(number)
            count+=1
            total+=number
        else:
            print("Enter vaild number")
# task_eight()

"""
Word guessing game (hangman)

    ○  A list of words will be hardcoded in your program, out of
     which the interpreter will

    ○ choose 1 random word.

    ○ The user first must input their names

    ○ Ask the user to guess any alphabet. If the random word
    contains that alphabet, it

    ○ will be shown as the output(with correct placement)

    ○ Else the program will ask you to guess another alphabet.

    ○ Give 7 turns maximum to guess the complete word.
"""

def task_nine():
    array_of_word = ['uml', 'oop', 'python', 'julia', 'flask']
    name = input("Enter your name: ")
    print(f"Welcome {name}")
    number = input(f"Choose Randome Word from '1' to {len(array_of_word)}: ")
    if number.isdigit():
        geted_word_position =  int(number)  
    else:
        print("Enter vaild input")
        task_nine()
    geted_word_position-=1
    if geted_word_position >= 0 and geted_word_position < len(array_of_word):
        print(f"\t------ you choose word contain '{len(array_of_word[geted_word_position])}' character ------")
        print("you have '7' attempt to guess word every once enter single letter")
    else:
        print("Your input not correct")
        task_nine()
    i = 0
    j = 0
    word_guessed_length = len(array_of_word[geted_word_position])
    word = ''
    while i < 7 and word_guessed_length !=0:
        print(word_guessed_length)
        letter = input("Enter letter ").lower()
        if array_of_word[geted_word_position][j] == letter :
            print('Yes your guess correct :)))')
            word+= letter
            j+=1
            word_guessed_length-=1
        else:
            print(f'\t ----- guess not correct  again\n The rest \'{7-(i+1)}\' attempt ----')
            
        i+=1
    return f"You win your guess correct '{word.capitalize()}'" if word == array_of_word[geted_word_position] else 'try in next ---'

# print(task_nine())







