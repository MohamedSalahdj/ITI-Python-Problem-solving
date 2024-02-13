'''
Fill an array of 5 elements from the user, 
Sort it in descending and ascending orders then display the output.
'''
def task_two():
    print("--"*15, 'task-02', "--"*15)
    l = [int(input(f"Enter only number'{i+1}': ")) for i in range(5)]
    l.sort()
    print(f"sort it ascending {l}")
    l.sort(reverse=True)
    print(f"sort it descending {l}")

    print(l)
# task_two()


''' 
Write a program that generate a multiplication table from 1 to the
number passed
'''

"""
    [1]             1*1
    [2,4]          2*1, 2*2
    [3,6,9]        3*1, 3*2, 3*3

"""

def task_six(): 
    tables_lists = []
    number = input("Enter table number will stoped it: ")
    number =  int(number) if number.isdigit() else task_six()
    for i in range(1, number+1):
        table= []
        for j in range(1,i+1):
            table.append(i*j)
        tables_lists.append(table)
    return tables_lists
print(task_six())

