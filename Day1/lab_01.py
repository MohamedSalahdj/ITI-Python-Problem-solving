'''
Write a program that counts up the number of vowels [a, e, i, o,
u] contained in the string.
'''
def task_one():
    print("--"*15, 'task-01', "--"*15)
    l = ['a','e','i','o','u']
    #first_solution
    print(len(l))
    #second solution
    count = 0
    for i in l:
        count+=1
    print(count)


'''
Fill an array of 5 elements from the user, Sort it in descending
and ascending orders then display the output.
'''

def task_two():
    print("--"*15, 'task-02', "--"*15)
    l = [int(input(f"Enter only number'{i+1}': ")) for i in range(5)]
    l.sort()
    print(f"sort it ascending {l}")
    l.sort(reverse=True)
    print(f"sort it descending {l}")

    print(l)
task_two()


'''
Write a program that prints the number of times the string 'iti'
occurs in anystring.
'''
def task_three():
    print("--"*15, 'task-03', "--"*15)
    count = 0
    word='iti'
    string = 'iti ipsum dolor sit amet consectetur adipisicing elit. Temporibus possimus quia provident animi labore, illo, inventore aspernatur doloribus saepe, deleniti quisquam iti accusamus quae? Officiis quas nemo iti viti consequatur'
    string_list = string.split()
    for item in string_list:
        if item == word:
            count+=1
    print(f"number of 'iti' in string = {count}")

task_three()

'''
Write a program that remove all vowels from the input word and
generate a brief version of it.
'''
def task_four():
    print("--"*15, 'task-04', "--"*15)
    vowels_charcter = ['a','e','i','o','u']
    word = input("Enter word you want remove vowels from it: ")
    new_word = ''
    for i in word:
        if i  not in vowels_charcter:
            new_word+=i

    return new_word

print(task_four())


'''
Write a program that prints the locations of "i" character in any
string you added.
'''
def task_five():
    print("--"*15, 'task-05', "--"*15)
    word= 'ziad'
    for i in range(len(word)):
        if word[i] == 'i':
            print(i)

task_five()


'''
Write a program that generate a multiplication table from 1 to the
number passed.
'''
def task_six():
    print("--"*15, 'task-06', "--"*15)
    no_of_rows = int(input("Enter number of rows: "))
    for i in range(1, no_of_rows+1):
        space = ' ' * (no_of_rows - i)
        star = '*' *i
        print(space,star)

task_six()