'''
check if india is in dictionary
use the in-built method purely.
do NOT use any if-else statement
then check if singapore is in the dictionary

helpers:
f'{var} not in dictionary'
'''

capitals={
            "usa":"washington dc",
            "india":"new delhi",
            "china":"beijing",
            "russia":"moscow"
}

var='singapore'

value=capitals.get(var, f'{var} not in dictionary')

print(value)