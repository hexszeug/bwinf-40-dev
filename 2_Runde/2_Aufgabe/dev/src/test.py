import random

for j in range(100):
    ds = [len(set([random.randint(1, 9) for x in range(9)])) for i in range(10000)]

    print(max(ds), min(ds), sum(ds) / len(ds), ":", *[ds.count(i) for i in range(1, 10)])