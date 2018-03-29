print('Enter friends names:')
l=[]
for i in range(0,3):
    l.append(input())
m=[]
for i in range(0,3):
    print('Enter'+l[i])
    dict={}
    dict[l[i]]=0
    for j in range(0,3):
        if(i!=j):
            print('Enter score for '+l[j])
            k=input()
            dict[l[j]]=int(k)
    m.append(dict)
n=[]
print(m)
for i in range(0,3):
    sum=0
    for j in range(0,3):
        sum=sum+m[j][l[i]]
    n.append(sum)
print('Max rating is',max(n))
print('Name:',l[n.index(max(n))])
