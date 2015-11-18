import time
import bisect

a = []
with open('2sum.txt', 'r') as f:
    for line in f:
        a.append(int(line.strip()))
a.sort()

ret = set()
for x in a:
    lower = bisect.bisect_left(a, -10000 - x)
    upper = bisect.bisect_right(a, 10000 - x)
    for y in a[lower:upper]:
        if x != y and x + y not in ret:
            ret.add(x + y)

print len(ret)            