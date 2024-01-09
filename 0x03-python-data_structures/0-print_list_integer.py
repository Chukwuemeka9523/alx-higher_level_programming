#!/usr/bin/python3
# --------------------------
# This python program:
# prints all integers of a list
#
# (c) 2024 Chukwuemeka, Umuahia, Abia State, Nigeria
# email emyperere@yahoo.com
# --------------------------

def print_list_integer(my_list=[]):
    """ This function prints all the integers of a list """
   # Iterate through the items in the list
    for num_of_int in my_list:
        print("{:d}".format(num_of_int))
