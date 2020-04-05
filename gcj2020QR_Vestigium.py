n = int(input())
for c in range(1, n+1):
    size=int(input())
    trace = 0
    badrows = 0
    badcols = 0
    cols = [set() for a in range(size)]
    for x in range(size):
        rows = [int(b) for b in input().split()]
        if len(set(rows)) < size:
            badrows += 1
        trace += rows[x]
        for k in range(size):
            cols[k].add(rows[k])
    for d in range(size):
        if len(cols[d]) < size:
            badcols += 1
    print("Case #{}:".format(c), trace, badrows, badcols)


