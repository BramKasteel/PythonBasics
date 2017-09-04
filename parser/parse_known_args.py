#From https://docs.python.org/2/library/argparse.html#example
#A small extension, now able to handle more arguments.
#Could be useful in case of multiple scripts.

import argparse

#First step in using argparse is creating an ArgumentParser object
parser = argparse.ArgumentParser(description='Process some integers.')
#The ArgumentParser object will hold all the information necessary to parse
#the command line into Python data types.

#Filling an ArgumentParser with information about program arguments is done
#by making calls to the add_argument() method.
#The information on how to take the strings is stored, it will be used when
#parse_args() is called.
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')


#Arguments are passed through the parse_args() method. It inspects the command
#line and invokes the appropriate action.
args, unparsed = parser.parse_known_args()
print args.accumulate(args.integers)
print parser.parse_known_args(['1','2','45','--sum'])
print parser.parse_known_args(['1','2','45','--sum','SomeOther1','NextArg'])
#Note that
#print parser.parse_known_args(['1','2','SomeOther1'])
#does not work, because the interpreter wants to see SomeOther1 as an int, not
#as an extra variable
