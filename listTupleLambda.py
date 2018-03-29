alist=[]
tup=()
while(tup!="end"):
    print("Type numbers to sort them and type 'end' to execute")
    tup=input("Enter the number:")
    alist.append(tup)
    new_list=alist[:-1]
    result=sorted(new_list,key=lambda x:x[-1])
print(result)
