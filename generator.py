import random

con = "|"
start = "("
end = ")"
##############
def checking(index,var_vector,number_of_desuncts):
    temp=[0 for i in range(number_of_desuncts)] #значения каждого дизьюнкта по умолчанию 
    for i,znach in enumerate(var_vector):
        for j in index[(i+1)]:
            if j>0:
                temp[j]+=int(znach)
            else:
                temp[j]+=int(znach)^1
    ans=list(map(lambda x:1 if x>0 else 0,temp))
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
########## Функции из main

def getSign():
    return random.randint(0, 1)

def addCon(formula, n):
    var = ["x" + str(i) for i in range(1, n+1)]
    var1 = ["-x" + str(i) for i in range(1, n+1)]
    var.extend(var1)
    func = formula + ","
    freq = dict.fromkeys(var, 0)
    cons = formula.replace(",", " ").replace("(", " ").replace(")", " ").split(" ")

    for c in cons:
        if len(c) > 0:
            vars = c.split("|")
            for v in vars:
                freq.update([(v, freq.get(v) + 1)])
    
    func += start
        

    k = 0
    t = 0
    s = []
    for i in range(n*2):
        s.append(random.randint(1, 2*n * (n-1) * (n-2)))

    freq = sorted(freq.items(), key=lambda x:x[1])

    freq = dict(freq)

    t = list(freq.items())[0][1]

    v1 = list(freq.items())[0][0]

    func += v1 + "|"

    t += 1

    freq.update([(v1, t)])

    exclude = []
    
    ex1, ex2 = 0, 0

    

    ex1 = var.index(v1)

    if ex1 <= (n*2 - 1) / 2:
        ex2 = ex1 + n
    else:
        ex2 = ex1 - n
    

    exclude.append(var[ex1])
    exclude.append(var[ex2])

    

    e1 = s[k]
    e2 = s[k+1]
    k += 2

    t_temp = t + 2
    b = []

    for key in freq.keys():
        if key not in exclude and key not in exclude and freq.get(key) <= t:
            b.append(key)

    while len(b) == 0:
        t_temp += 1
        for key in freq.keys():
            if key not in exclude and key not in exclude and freq.get(key) <= t:
                b.append(key)

    v2 = b[e1 % len(b)]

    func += v2 + "|"

    ex1 = var.index(v2)

    if ex1 <= (n*2 - 1) / 2:
        ex2 = ex1 + n
    else:
        ex2 = ex1 - n
    

    exclude.append(var[ex1])
    exclude.append(var[ex2])

    
    t_temp = t + 2

    b = []

    for key in freq.keys():
        if key not in exclude and key not in exclude and freq.get(key) <= t:
            b.append(key)

    while len(b) == 0:
        t_temp += 1
        for key in freq.keys():
            if key not in exclude and key not in exclude and freq.get(key) <= t:
                b.append(key)

    v3 = b[e2 % len(b)]
    func += v3 + end


    return(func)


def generateKNF(n):
    var = ["x" + str(i) for i in range(1, n+1)]
    var1 = ["-x" + str(i) for i in range(1, n+1)]
    var.extend(var1)
    func = ""
    freq = dict.fromkeys(var, 0)


    for c in range(n):
        func += start
        

        k = 0
        t = 0
        s = []
        for i in range(n*2):
            s.append(random.randint(1, 2*n * (n-1) * (n-2)))

        freq = sorted(freq.items(), key=lambda x:x[1])

        freq = dict(freq)

        t = list(freq.items())[0][1]

        v1 = list(freq.items())[0][0]

        func += v1 + "|"

        t += 1

        freq.update([(v1, t)])

        exclude = []
        
        ex1, ex2 = 0, 0

        

        ex1 = var.index(v1)

        if ex1 <= (n*2 - 1) / 2:
            ex2 = ex1 + n
        else:
            ex2 = ex1 - n
        

        exclude.append(var[ex1])
        exclude.append(var[ex2])

        

        e1 = s[k]
        e2 = s[k+1]
        k += 2

        t_temp = t + 2
        b = []

        for key in freq.keys():
            if key not in exclude and key not in exclude and freq.get(key) <= t:
                b.append(key)

        while len(b) == 0:
            t_temp += 1
            for key in freq.keys():
                if key not in exclude and key not in exclude and freq.get(key) <= t:
                    b.append(key)

        v2 = b[e1 % len(b)]

        func += v2 + "|"

        ex1 = var.index(v2)

        if ex1 <= (n*2 - 1) / 2:
            ex2 = ex1 + n
        else:
            ex2 = ex1 - n
        

        exclude.append(var[ex1])
        exclude.append(var[ex2])

        
        t_temp = t + 2

        b = []

        for key in freq.keys():
            if key not in exclude and key not in exclude and freq.get(key) <= t:
                b.append(key)

        while len(b) == 0:
            t_temp += 1
            for key in freq.keys():
                if key not in exclude and key not in exclude and freq.get(key) <= t:
                    b.append(key)

        v3 = b[e2 % len(b)]
        func += v3 + end + ","


    return(func[:-1:])

    # for i in range(len(var)):
    #     pos = []
    #     ind = set()
    #     ind.add(i)
    #     if getSign():
    #         pos.append(var[i])
    #     else:
    #         pos.append("-" + var[i])

    #     for p in range(2):
    #         j = random.randint(0, n-1)
    #         while(j in ind):
    #             j = random.randint(0, n-1)

    #         ind.add(j)
    #         if getSign():
    #             pos.append(var[j])
    #         else:
    #             pos.append("-" + var[j])

    #     func += start + pos[0] + "|" + pos[1] + "|" + pos[2] + end + ","
    # return func[:-1:]

#Будем юзать ее чтобы генерировать уже функцию для работы   
global_rate=[] 
def generateRandomKNF(NUMBER_OF_VARIABLES):
    example=generateKNF(NUMBER_OF_VARIABLES) #Функция для проверки

    index = setIndex(example)

    #Тупой перебор       
    # with open("output.txt","w") as fle:
    #     fle.write("")


    # for i,znach in enumerate(("{:0>" + f"{10}" + "}").format(bin(1)[2:])):
    #     print(index[i+1])

    #цикл, который достраивает формулу, добавляя скобки, пока она разрешима
    #Делаем неразрешимую функцию (Для проверки работы алгоритма)
    counter=0
    for k in range(NUMBER_OF_VARIABLES//4):
        counter+=1
        count = []
        rate = []

        n = len(example.split(","))
        index = setIndex(example)#хранит информацию о том, в каких скобках есть та или иная переменная
        
        for i in range(pow(2, NUMBER_OF_VARIABLES)):
            # print("{:0>10}".format(bin(i)[2:]))#Подумать над работой с бинарными данными
            # print (("{:0>" + f"{NUMBER_OF_VARIABLES}" + "}").format(bin(i)[2:]))
            count.append(checking(index, ("{:0>" + f"{NUMBER_OF_VARIABLES}" + "}").format(bin(i)[2:]),n))#
            # print(("{:0>" + f"{n}" + "}"))
            # with open("output.txt","a") as fle:
            #     fle.write(str(checking(index,"{:0>10}".format(bin(i)[2:])))+"\n")
        for c in count:
            if c == n:
                rate.append(1)
                
            else:
                rate.append(0)
                
        if rate.count(1) > 0 and k !=NUMBER_OF_VARIABLES//4-1:
        
            example = addCon(example, NUMBER_OF_VARIABLES)
        else:
            break


    print("true desuncts: ",max(count) ," number of operations to find function:",counter )
    print("Percent of true answers: ", rate.count(1) / len(rate))
    return(example)

def generate_full_ranodm_KNF(NUMBER_OF_VARIABLES):
    example=generateKNF(NUMBER_OF_VARIABLES) #Функция для проверки

    index = setIndex(example)

    #Тупой перебор       
    # with open("output.txt","w") as fle:
    #     fle.write("")


    # for i,znach in enumerate(("{:0>" + f"{10}" + "}").format(bin(1)[2:])):
    #     print(index[i+1])

    #цикл, который достраивает формулу, добавляя скобки, пока она разрешима
    #Делаем неразрешимую функцию (Для проверки работы алгоритма)
    counter=0
    for k in range(NUMBER_OF_VARIABLES//4):
        counter+=1
        count = []
        rate = []

        n = len(example.split(","))
        index = setIndex(example)#хранит информацию о том, в каких скобках есть та или иная переменная
        
        for i in range(pow(2, NUMBER_OF_VARIABLES)):
            # print("{:0>10}".format(bin(i)[2:]))#Подумать над работой с бинарными данными
            # print (("{:0>" + f"{NUMBER_OF_VARIABLES}" + "}").format(bin(i)[2:]))
            count.append(checking(index, ("{:0>" + f"{NUMBER_OF_VARIABLES}" + "}").format(bin(i)[2:]),n))#
            # print(("{:0>" + f"{n}" + "}"))
            # with open("output.txt","a") as fle:
            #     fle.write(str(checking(index,"{:0>10}".format(bin(i)[2:])))+"\n")
        for c in count:
            if c == n:
                rate.append(1)
                
            else:
                rate.append(0)
                
        if k !=NUMBER_OF_VARIABLES//4-1:
            example = addCon(example, NUMBER_OF_VARIABLES)
        

    print("true desuncts: ",max(count) ," number of operations to find function:",counter )
    print("Percent of true answers: ", rate.count(1) / len(rate))
    return(example,max(count))
def generate_without_checking(NUMBER_OF_VARIABLES):
    example=generateKNF(NUMBER_OF_VARIABLES) #Функция для проверки

    index = setIndex(example)

    #Тупой перебор       
    # with open("output.txt","w") as fle:
    #     fle.write("")


    # for i,znach in enumerate(("{:0>" + f"{10}" + "}").format(bin(1)[2:])):
    #     print(index[i+1])

    #цикл, который достраивает формулу, добавляя скобки, пока она разрешима
    #Делаем неразрешимую функцию (Для проверки работы алгоритма)
    counter=0
    for k in range(random.randint(NUMBER_OF_VARIABLES//4,NUMBER_OF_VARIABLES//3)):
        counter+=1
        
        if k !=NUMBER_OF_VARIABLES//4-1:
            example = addCon(example, NUMBER_OF_VARIABLES)
        

    # print(" number of operations to find function:",counter )
    
    return(example)
def generate_into_file():
    with open("examples.txt",'w') as file:
        #Write number of variable to generate_without_checking_function
        # file.write(generate_without_checking(300)+",\n")
        # file.write(generate_without_checking(400)+",\n")
        file.write(generateKNF(500)+",\n")
        file.write(generate_without_checking(400))
# generate_into_file()