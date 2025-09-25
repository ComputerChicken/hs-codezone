l = input().split(",")
nl = []
for i, v1 in enumerate(l):
    notDuplicate = True
    for j, v2 in enumerate(l):
        if i != j and v1 == v2:
            notDuplicate = False
    if notDuplicate: nl.append(v1)
print(",".join([str(i) for i in nl]))