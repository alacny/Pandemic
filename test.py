#!/usr/bin/python3
import sys
sys.path.append("/home/alacny/Programowanie/Python/Pandemic/lib")
import species as h
johny=[h.Species(), h.Species(), h.Species(), h.Species(), h.Species(), \
        h.Species(), h.Species(), h.Species(), h.Species(), h.Species()]
for i in range(0,10):
    johny[i].setPOfInf(70)
#    johny[i].setImmune()
    johny[i].setInfection()
    print(johny[i].getIllness())
