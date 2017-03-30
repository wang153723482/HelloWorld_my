import random

print random.choice('abcde12345')
print random.choice(['web','app','pad'])


def random_char(y):
    return ''.join(random.choice('abcde12345') for x in range(y))



print  random_char(5)



