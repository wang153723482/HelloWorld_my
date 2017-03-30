s = set()

s.add('a')
s.add('a')

print s

from collections import defaultdict

l = [1, 2, 3, 4, 5]
s = defaultdict(int)
for a in l:
    s['x'] += a
    pass
print s
