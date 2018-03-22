#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 15:31:53 2018

@author: jayneel
00 -> sink node
01 -> next city node.

"""

time=0
total=0     
itera=0
time=0
nnodes=0
class road:
    def __init__(self):
        self.capacity=0
        self.target=0
        self.pile=10
        self.overallcap=0
        self.timer=30
        self.lrate=0
        self.dierate=0
        self.entryrate=0#no=total*ratio
class node:
    def __init__(self):
        self.number=0 #node #
        self.nroads=0# number of roads on the node
        self.rarray=[]
        self.rarray.append(road())
        self.ftime=30# fixed time for that node
        self.maxvehicles=10
        
def ratio(currnode):
    #input of format: current node,road 
    #return ratio in n tuple(no of roads)4
    return 0
def total():
    total=0
    for i in range(1,nnodes+1):
        x=network[i]
        for j in range(1,x.nroads+1):
            total+=x.rarray[j].pile
    return total
def display():
    global itera
    for i in range(1,nnodes+1):
        x=network[i]
        for j in range(1,x.nroads+1):
            print("on node"+str(i)+" ;road "+str(j)+": the pileup is"+str(x.rarray[j].pile)+"total is "+str(total() ))
            i=i
      
def logic():
    global time,itera
    for i in range(1,nnodes+1):
        x=network[i]
        #print("in node #"+str(i) )
        #roadwise
        for j in range(1,x.nroads+1):
            #print("sending from road"+str(j))
            y=x.rarray
            volatj=y[j].pile
            tar=[]
            tar.append(0)
            pilenext=[]
            pilenext.append(0)
            tpile=0
            for k in range(1,x.nroads+1):
                
                tar.append(y[k].target);
                t=network[int(y[k].target/10)].rarray[int(y[k].target%10)].pile
                #print(t)
                pilenext.append(t)
                tpile=tpile+t
                #print(tpile)
            #print(str(i)+str(j)+":"+str(tpile)+"::"+str(tar)+"::"+str(pilenext)) 
            #print(pilenext)
            for k in range(1,x.nroads+1):
                #print("sending via road"+str(k))
                z=network[int(y[k].target/10)].rarray[int(y[k].target%10)]
                if tpile>0:
                    c=pilenext[k]/tpile
                    #print(c)
                    #print(tpile)
                    tosend=0
                    if c > 0:
                        tosend=int(c*volatj)
                    #print(tosend)
                    if tosend > z.capacity:
                        tosend=z.capacity
                    #print(tosend)    
                    if tosend > y[j].lrate*y[j].timer:
                        tosend=y[j].lrate*y[j].timer
                        #print(tosend)     
                    remove=int(tosend*y[k].dierate)
                    add=int(tosend*y[k].entryrate)
                    if tosend>0:
                        if network[i].rarray[j].pile > tosend:
                            network[int(y[k].target/10)].rarray[int(y[k].target%10)].pile+=add
                            network[i].rarray[j].pile=network[i].rarray[j].pile-remove
                            s=str(itera)+"::"+str(i)+"::"+str(j)+"::::::"+str(i)+"::"+str(k)+"::::::"+str(int(y[k].target/10))+"::"+str(int(y[k].target%10))+"---"+str(tosend)+"_____"+str(total())
                            #print(tosend)
                            #print(s)
 


#get network from user.
#create network   
nnodes=3
#nnodes=int(input("Number of nodes") )#number of nodes
network=[] #create a network array to add nodes.
network.append(node())
for i in range(1,nnodes+1):
    #print("in node"+str(i))
    network.append(node())
    x=3
    x#=int(input("number of roads in node"+str(i)))
    network[i].nroads=x
    network[i].number=i
    for j in range(1,x+1): #open road nodes.
        network[i].rarray.append(road())
        #print(network[i].rarray[j])
        #network[i].rarray[j].target=13
        #network[i].rarray[j].target=input("next target of road"+str(j))
        network[i].rarray[j].pile=100#input("pile up initial")
        if j%2==0:
            network[i].rarray[j].timer=100#input("Timer")#timer it stays on for
        else:
            network[i].rarray[j].timer=50#input("Timer")#timer it stays on for
        network[i].rarray[j].capacity=100#input("Capacity of road "+str(10*i+j))  
        network[i].rarray[j].lrate=2#input("Leaving rate of road")
        network[i].rarray[j].entryrate=0.001
        network[i].rarray[j].dierate=0.2
network[0].rarray[0].capacity=100#by default capacity of road connecting to next city is 100.

network[1].rarray[1].target=0
network[1].rarray[2].target=0
network[1].rarray[3].target=31
network[2].rarray[1].target=0
network[2].rarray[2].target=0
network[2].rarray[3].target=32
network[3].rarray[1].target=13
network[3].rarray[2].target=23
network[3].rarray[3].target=0
network[0].rarray[0].target=0
#network[0].rarray[1].target=0
#network[0].rarray[2].target=0
#network[0].rarray[3].target=0
#network[0].rarray[0].pile=0

itera=0
display()
while total()>5:
    if itera >13:
        break
    logic()
    itera=itera+1
    #print(str(itera)+"::"+str(total()))

display()    
print(itera)   
print(network[0].rarray[0].pile)
#print(network[0].rarray[1].pile)