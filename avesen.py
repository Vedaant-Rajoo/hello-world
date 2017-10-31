sen=raw_input('')
nsen=sen.split()
rsen=nsen[::-1]
a=[]
for i in rsen:
    j=i[::-1]
    if j in rsen:
        a.append(j)
if a==[]:
    print -1
else:
    for k in a:
        print k

