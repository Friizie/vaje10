from random import *
from string import *

# Kristijan Pucoski

def get_random_string(length):
    letters = ascii_uppercase
    result_str = "".join(choice(letters) for i in range(length))  # generate new random strings
    return result_str


def gen_file(file_name,line_length,letter_length):                 # example {"file.txt",10,10}
    f = open(file_name, "w+")
    for i in range(line_length):
        f.write(get_random_string(letter_length))                  # writing {number} of random chars to a file
        f.write("\n")
    f.close()


gen_file("randstrings.txt",10,10)
# ----------------------------------------------------------------------------------------------------------------------
#Kliment Markoski

def print_file(f):
    file= open(f,'r')       #opens a file and prints to terminal
    for line in file:
        print(line)

print_file("randstrings.txt")
