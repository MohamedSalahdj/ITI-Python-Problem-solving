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
    array_of_integer = [ number for number in range(start, length+1)]
    return array_of_integer

print(task_three(10, 2))



