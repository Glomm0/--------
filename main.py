import generator
def checking(index,var_vector):
    temp=[0 for i in range(len(var_vector))] #значения каждого дизьюнкта по умолчанию 
    # В индексе хранится n записей, а в векторе кол-во разрядов равно кол-ву скобок в функции
    # Т.к. скобок может быть больше чем пременных, следующий цикл не работает
    for i,znach in enumerate(var_vector):
        for j in index[(i+1)]:
            if j>0:
                temp[j]+=int(znach)
            else:
                temp[j]+=int(znach)^1
    ans=list(map(lambda x:1 if x>0 else 0,temp))
    # print(ans)
    return ans.count(1)

def setIndex(func):
    index={}
    temp_data=func.split(',')
    for i,skobka in enumerate(temp_data):
        skobka=skobka[1:-1:]
        for num in skobka.split("|"):
            znach=int(num[num.index('x')+1:])
            if(znach not in index.keys()):
                index[znach]=[-1*i if num[0]=='-' else i]
            else:
                index[znach].append(-1*i if num[0]=='-' else i)
    return index



NUMBER_OF_VARIABLES=10
example=generator.generateKNF(NUMBER_OF_VARIABLES) #Функция для проверки

index = setIndex(example)
# print("{:0>10}".format(bin(1)[2:]))

#Тупой перебор       
# with open("output.txt","w") as fle:
#     fle.write("")

count = []
rate = []
# for i,znach in enumerate(("{:0>" + f"{10}" + "}").format(bin(1)[2:])):
#     print(index[i+1])

#цикл, который достраивает формулу, добавляя скобки, пока она разрешима
#проблема с методом checking
while True:
    n = len(example.split(","))
    index = setIndex(example)#хранит информацию о том, в каких скобках есть та или иная переменная
    for i in range(pow(2, n)):
        # print("{:0>10}".format(bin(i)[2:]))#Подумать над работой с бинарными данными
        # print (checking(index,"{:0>10}".format(bin(i)[2:])))
        count.append(checking(index, ("{:0>" + f"{n}" + "}").format(bin(i)[2:])))
        # print(("{:0>" + f"{n}" + "}"))
        # with open("output.txt","a") as fle:
        #     fle.write(str(checking(index,"{:0>10}".format(bin(i)[2:])))+"\n")


    for c in count:
        if c == NUMBER_OF_VARIABLES:
            rate.append(1)
        else:
            rate.append(0)

    if rate.count(1) > 0:
        example = generator.addCon(example, NUMBER_OF_VARIABLES)
    else:
        break



print(rate.count(1))
print("Percent of true answers: ", rate.count(1) / len(rate))
print(example)
