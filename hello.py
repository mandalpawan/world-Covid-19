ls3 = []
ls2 = []
ls = [1,2,3,4,5]
count = 0
while(count<len(ls)-1):
    ls2.append(ls[count])
    ls3.append(ls[count+1])
    print(count)
    count+=1

print(ls2)

print('----------')
print(ls3)
