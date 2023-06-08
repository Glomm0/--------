import random
import math
class Particle:
    #Coefficents
    a1=0
    a2=0
    w=0
    best_swarm_position=[]
    def __init__(self):
        self.position=[]
        self.speed=[]
        self.best_position=[]
    def set_position(self,position):
        self.position=position
    def set_speed(self,speed):
        self.speed=speed
    def add_vectors(self,vector1,vector2):
        temp=[]
        for i in range(len(vector1)):
            znach=vector1[i]+vector2[i] 
            if znach>1:
                znach=1
            if znach<0:
                znach=0
            temp.append(znach)
        return temp
    def sub_vectors(self,vector1,vector2): 
        temp=[]
        for i in range(len(vector1)):
            temp.append(vector1[i]-vector2[i] )
        return temp
    def mult_number_by_vector(self,number,vector):
        temp=[]
        for i in range(len(vector)):
            temp.append(vector[i]*number)
        return temp
    def move(self):
        temp=[]
        for i in range(len(self.speed)):
            S=1/(1+pow(math.e,-self.speed[i]))
            if(random.random()<S):
                temp.append(1)
            else:
                temp.append(0)
            
        self.position=temp
    def change_speed(self):
        r1=random.random()
        r2=random.random()
        
        self.speed=self.add_vectors(self.add_vectors(self.mult_number_by_vector(self.a1*r1,self.sub_vectors(self.best_position,self.position)),
                                                    self.mult_number_by_vector(self.a2*r2,self.sub_vectors(self.best_swarm_position,self.position))),
                                    self.mult_number_by_vector(self.w,self.speed))
        
    def round_speed(self):
        temp=[]
        for i in range(len(self.speed)):
            temp.append(round(self.speed[i]))
        self.speed=temp
    def and_bit_with_number(number,vector):
        temp=[]
        for i in range(len(vector)):
            temp.append(number^vector[i])
        return temp
    def change_speed_binary(self):
        
        W=0
        temp=[]
        for i in self.speed:
            c1=(1 if random.random()<1/(1+pow(math.e,-self.a1)) else 0)
            c2=(1 if random.random()<1/(1+pow(math.e,-self.a2)) else 0)
            W=(1 if random.random()<1/(1+pow(math.e,-self.w)) else 0)
            temp.append(W&self.speed[i]|c1&(Particle.best_swarm_position[i]^self.position[i])|c2&(self.best_position[i]^self.position[i]))
        self.speed=temp
    def move_binary(self):
        temp=[]
        for i in self.speed:
            temp.append(self.speed[i]^self.position[i])
        self.position=temp
#####Testing
# p=Particle()
# p.set_position([0,0,0,0])
# p.set_speed([0.6,0,-0.6,0.8])
# p.round_speed()
# print(p.speed)