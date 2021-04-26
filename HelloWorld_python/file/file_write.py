import time

for i in range(1, 20):
    f = open('z:/test.log', 'ab')
    f.write('aaaaazzz====' + str(i) + '\n\r')
    f.flush()
    f.close()
    time.sleep(1)
