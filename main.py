
def checking(index,var_vector):
    temp=[0,0,0,0,0] #значения каждого дизьюнкта по умолчанию
    for i,znach in enumerate(var_vector):
        for j in index[str(i+1)]:
            if j>0:
                temp[j]+=int(znach)
            else:
                temp[j]+=int(znach)^1
    ans=list(map(lambda x:1 if x>0 else 0,temp))
    print(ans)
    return ans.count(1)


index={}
example="(x1|-x2|x3),(-x1|-x2|x4),(x5|-x4|x3),(-x1|-x2|-x3),(-x1|-x2|-x5)"
temp_data=example.split(',')
for i,skobka in enumerate(temp_data):
    skobka=skobka[1:-1:]
    for num in skobka.split("|"):
        znach=num[num.index('x')+1]
        if(znach not in index.keys()):
            index[znach]=[-1*i if num[0]=='-' else i]
        else:
            index[znach].append(-1*i if num[0]=='-' else i)
        
for i in range(pow(2,5)):
    print("{:0>5}".format(bin(i)[2:]))#Подумать над работой с бинарными данными
    print (checking(index,"{:0>5}".format(bin(i)[2:])))
