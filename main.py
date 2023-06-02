import generator
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



NUMBER_OF_VARIABLES=6
ex=generator.generateRandomKNF(NUMBER_OF_VARIABLES)
print(ex)
