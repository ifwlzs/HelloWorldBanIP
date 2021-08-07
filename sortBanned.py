l=[]
path="banned.txt"
with open(path, 'r') as f:
    l.append(f.readlines())
l=l[0]
for i in range(0, len(l)):
    l[i] = l[i].strip("\n")

l=list(set(l))
l.sort()
print(l)
with open(path, 'w') as f:
    for i in l:
        f.write(i+"\n")
        f.flush()
    f.close()