import random

# print( random.choice('abcde12345') )
# print( random.choice(['web','app','pad']) )

def random_char(y):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for x in range(y))

# print(random_char(10))

def main():
    f = open('data.csv','w')
    for i in range(10000):
        f.write( random_char(10)+'\n' )
        pass
    pass
    f.close()


if __name__ == '__main__':
    main()



