import generator
import random
import matplotlib
import matplotlib.pyplot as plt
from particle import Particle
def checking(index,var_vector,number_of_desuncts):
    temp=[0 for i in range(0,number_of_desuncts)] #значения каждого дизьюнкта по умолчанию 
    for i,znach in enumerate(var_vector):
        for j in index[(i+1)]:
            if j>0:
                temp[j-1]+=int(znach)
            else:
                temp[(-1*j)-1]+=int(znach)^1
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
                index[znach]=[-1*(i+1) if num[0]=='-' else (i+1)]
            else:
                index[znach].append(-1*(i+1) if num[0]=='-' else (i+1))
    return index

def run():
    global results,NUMBER_OF_VARIABLES,NUMBER_OF_ITERATIONS,ex
#Different means to generate functions

    # ex=generator.generateRandomKNF(NUMBER_OF_VARIABLES)
    # ex,max_true=generator.generate_full_ranodm_KNF(NUMBER_OF_VARIABLES)
    # ex=generator.generate_without_checking(NUMBER_OF_VARIABLES)
    # ex="(x1|-x8|x5),(x2|x3|x20),(x3|-x20|-x17),(x4|x11|x3),(x5|x1|-x19),(x6|x10|x14),(x7|x6|-x2),(x8|-x9|-x20),(x9|-x8|-x1),(x10|-x6|-x1),(x11|x1|x20),(x12|-x19|x9),(x13|-x6|-x4),(x14|x20|-x8),(x15|-x7|-x17),(x16|x10|-x2),(x17|x19|x11),(x18|x7|x12),(x19|-x14|x20),(x20|-x19|-x2),(-x3|-x10|-x5),(-x11|-x10|-x18),(-x12|-x16|-x14),(-x13|-x9|-x16)"
    # print(ex)

    index=generator.setIndex(ex)
    n=len(ex.split(','))
    particles=[Particle() for i in range(20)]
    for i in particles: #Initializing 
        temp=[ random.randint(0,1) for j in range(NUMBER_OF_VARIABLES)]
        temp2=[ random.randint(0,1) for j in range(NUMBER_OF_VARIABLES)]
        i.set_position(temp)
        i.set_speed(temp2)
        checking_res=checking(index,temp,n)
        if checking_res>checking(index,i.best_position,n):
            i.best_position=temp
        if checking_res>checking(index,Particle.best_swarm_position,n):
            Particle.best_swarm_position=temp

    for o in range(NUMBER_OF_ITERATIONS):#looping till answer or to maximum number of iterations
        for i in particles:
            i.move()
            # i.move_binary()
            checking_res=checking(index,i.position,n)
            if checking_res>checking(index,i.best_position,n):
                i.best_position=i.position
            if checking_res>=checking(index,Particle.best_swarm_position,n):
                Particle.best_swarm_position=i.position
                
                if checking_res==n:
                    #print(Particle.best_swarm_position,checking(index,Particle.best_swarm_position,n))
                    print(checking(index,Particle.best_swarm_position,n))
                    print("Total desuncts: ",n)
                    return 0
        for i in particles:
            i.change_speed()
            # i.change_speed_binary()
        results.append([o,checking(index,Particle.best_swarm_position,n)])
    print(checking(index,Particle.best_swarm_position,n))
    print("Total desuncts: ",n)
    
    Particle.best_swarm_position=[]
    





if __name__=="__main__":
    with open("examples.txt","r") as file:
        iters=[500] #number of iterations may be a list if several iteration numbers are necessary
        data=file.read().split(",\n")

        #Parameters
        Particle.a1=1.8  #Particle best position
        Particle.a2=1.6  #Swarm best position
        Particle.w=0.8   #Inertia
        for j in iters:
            for i,ex in enumerate(data):
               
                results=[]
                NUMBER_OF_VARIABLES=max(setIndex(ex).keys())
                NUMBER_OF_ITERATIONS=j
                run()
                x=[i[0] for i in results]
                y=[i[1]/len(ex.split(',')) for i in results]
                plt.subplot((len(data))*100+1*10+i+1)
                plt.title("number of all desuncts:"+str(len(ex.split(','))))
                plt.ylabel("MAXIMUM True")
                plt.xlabel("NUMBER OF ITERATIONS")
                plt.grid(True)
                plt.axis([0,len(x),0,1])
                plt.plot(x,y)
                
                    # print(results)
        matplotlib.pyplot.subplots_adjust( hspace=0.8)
        plt.show()
        
            
            