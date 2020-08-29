#!/usr/bin/python3

import sys
import os
sys.path.append("/home/alacny/Programowanie/Python/Pandemic/lib")
import species as h
import world as w

# Initial number of persons
maxP=10000
# Range of infection
rInf=10

# Max time of the simulation
tMax = 10000

# Creating persons
person=[]
for i in range(0,maxP):
   person.append(h.Species())

# Initial infection
person[0].raiseInfection(1)
person[0].goToXY(0,0)

outF = open("pandemic.out","w")
outNInf = open("infected.out","w")

# Number of infected species
nInf=1
# Main loop
for t in range(0,tMax):
# Moving persons
    x=list()
    y=list()
    for p in person:
        p.moveRandomly(dx=50,dy=50)
        x.append(p.getX())
        y.append(p.getY())
    dr=0


# Calculate encounters and infecting
    for i in range(0, len(person)):
        for j in range(i,len(person)):
            dr=((person[i].getX()-person[j].getX())**2+(person[i].getY()-person[j].getY())**2)**(0.5)
            if(dr<rInf): 
                # Infection took place!
                # Only a sound person catches infection from an infected person
                if (person[i].getIllness()==0 and person[j].getIllness()!=0):
                    person[i].raiseInfection(1)
                    nInf+=nInf
                elif (person[i].getIllness()!=0 and person[j].getIllness()==0):
                    person[j].raiseInfection(1)
                    nInf+=nInf

        print(t,person[i].getX(),person[i].getY(), person[i].getIllness(),file=outF)
    print(t,nInf,file=outNInf)
    print("\n",file=outF)
outF.close()
outNInf.close()
