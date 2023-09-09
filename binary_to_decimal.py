binaryno=input("enter the binary no : ")
mylist=[i for i in binaryno]
length=len(mylist)


bnarylist=[0]*length
j=0
for i in binaryno:
    bnarylist[j]=int(i)
    j+=1





bnary=0
length=len(bnarylist)

for j in range(length):
    # print((length-1)-j)
    bnary+=(2**j)*bnarylist[(length-1)-j]
print("binary to decimal : ",bnary)
