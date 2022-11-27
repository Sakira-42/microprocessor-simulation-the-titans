# Microprocessor simulation
# supports a small set of simulated operations
# prints the output for each operation
import sys

from ops import *

# You need to update the process function to actually handle the operations. To
# start, it just prints out each line of the input.
def process(line):
    Operation = str(line).split()[0]
    args = str(line).split()[1:]
    if all(arg.replace("-","").isnumeric() for arg in args):
        if Operation == 'noop':
            if len(args)==0:
                print(noop())
            else:
                print(invalid(line))

        elif Operation == 'add':
            if len(args)== 2:
                print(add(args[0],args[1]))
            else:
                print(invalid(line))

        elif Operation == 'mul':
            if len(args)== 2:
                print(mul(args[0],args[1]))
            else:
                print(invalid(line))

        elif Operation == 'gt':
            if len(args)== 2:
                print(gt(args[0],args[1]))
            else:
                print(invalid(line))

        elif Operation == 'or':
            if len(args)== 2:
                print(logical_or(args[0],args[1]))
            else:
                print(invalid(line))

        elif Operation == 'nand':
            if len(args)== 2:
                print(nand(args[0],args[1]))
            else:
                print(invalid(line))

        elif Operation == 'min':
            if len(args)>= 2:
                print(minimum(args))
            else:
                print(invalid(line))
        elif Operation == 'shift':
            if len(args)== 2 and int(args[0])>0 and int(args[1])>0:
                print(shift(args[0],args[1]))
            else:
                print(invalid(line))
        else:
            print(invalid(line))
    else: print(invalid(line))


    


# The run function is provided, you don't need to change it.
# It reads all the lines from a file, then calls the process function
#   for each line 
def run(filename):
    with open(filename, 'r') as file:
        for operation in file.readlines():
            process(operation.strip())

# This code will call the run function with a filename, if it's provided on the 
# command line. It would pass samples/sample2.txt with this invocation:
# python3 main.py samples/sample2.txt
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py [path/to/sample]")
    else:
        run(sys.argv[1])
