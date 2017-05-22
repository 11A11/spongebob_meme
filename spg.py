import random
import string
import sys



inp = raw_input("Enter the text  ")
lt = len(inp)
for x in range(lt):
    if(inp[x].isalpha()):
        y=random.randint(0,50)
        if (y%2 is 0):
            sys.stdout.write(inp[x].upper())
        else:
            sys.stdout.write(inp[x].lower())
    else:
        sys.stdout.write(inp[x])


    
