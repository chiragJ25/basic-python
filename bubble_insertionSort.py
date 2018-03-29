def bubble_sort(l):
    for i in range(1,len(l)):
        for j in range(0,len(l)-i):
            if(l[j]>l[j+1]):
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t
    print(l)
def insertion_sort(l):
    for i in range(1,len(l)):
        current_value=l[i]
        position=i
    while position>0 and l[position-1]>current_value:
        l[position]=l[position-i]
        position=position-1
    l[position]=current_value
    print(l)
l=[]
r=0
while True:
    n=input("enter the nos")
    if(n=="end"):
        break
    else:
        l.append(int(n))
bubble_sort(l)
insertion_sort(l)
    
        
