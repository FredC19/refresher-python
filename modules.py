def generate_full_name(first_name,last_name):
    return first_name + ' ' + last_name

#Modules are just files imported into anoter file so it
#can use that files functions/ variables.

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive


#Basketball 3 point randomness
makes=0
miss=0
attempts = 100
for x in range(attempts):
    shot = randint(1,10)
    if shot <= 4:
        makes+=1
    else:
        miss +=1
print (f"Makes:{makes} Misses:{miss}")