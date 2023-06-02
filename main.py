import generator
def checking(index,var_vector):
    temp=[0 for i in range(max(index.keys()))] #значения каждого дизьюнкта по умолчанию 
    for i,znach in enumerate(var_vector):
        for j in index[i+1]:
            if j>0:
                temp[j]+=int(znach)
            else:
                temp[j]+=int(znach)^1
    ans=list(map(lambda x:1 if x>0 else 0,temp))
    print(ans)
    return ans.count(1)


index={}#хранит информацию о том, в каких скобках есть та или иная переменная
NUMBER_OF_VARIABLES=10
example=generator.generateKNF(NUMBER_OF_VARIABLES) #Функция для проверки


temp_data=example.split(',')
for i,skobka in enumerate(temp_data):
    skobka=skobka[1:-1:]
    for num in skobka.split("|"):
        znach=int(num[num.index('x')+1:])
        if(znach not in index.keys()):
            index[znach]=[-1*i if num[0]=='-' else i]
        else:
            index[znach].append(-1*i if num[0]=='-' else i)
#Тупой перебор       
with open("output.txt","w") as fle:
    fle.write("")
for i in range(pow(2,NUMBER_OF_VARIABLES)):
    #print("{:0>10}".format(bin(i)[2:]))#Подумать над работой с бинарными данными
    #print (checking(index,"{:0>10}".format(bin(i)[2:])))
    with open("output.txt","a") as fle:
        fle.write(str(checking(index,"{:0>10}".format(bin(i)[2:])))+"\n")
print(example)
