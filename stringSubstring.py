string=input('Enter string')
string2=input('Enter the substring')
st=string2[0]
print('No of times substring',string2,'is repeated is',string.count(string2))
print('Starting indices are')
for i in range(0,len(string)-len(string2)+1):
    equal=1
    for j in range(0,len(string2)):
        if(string[i+j]==string2[j]):
            equal=0
            break
    if(equal!=1):
        print(i)
