def noop():
    return ""

def add(num1,num2):
    num1=int(num1)
    num2=int(num2)
    return num1+num2

def mul(first_num,second_num):
    first_num=int(first_num)
    second_num=int(second_num)
    return first_num*second_num

def gt(num1, num2):
    num1=int(num1)
    num2=int(num2)
    if num1>num2:
        return 1
    else:
        return 0

def logical_or(num1,num2):
    num1=int(num1)
    num2=int(num2)
    if num1 == 0 and num2 == 0:
        return 0
    else:
        return 1

def nand(first_num,second_num):
    first_num=int(first_num)
    second_num=int(second_num)
    if first_num == 0 or second_num == 0:
        return 1
    else: 
        return 0

def minimum(list_of_arguments):
    new_list = [int(i) for i in list_of_arguments]
    return min(new_list)

def shift(number,moves):
    number=int(number)
    moves=int(moves)
    return number << moves

def invalid(line):
    return f"invalid operation {line}"