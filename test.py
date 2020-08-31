#!/usr/bin/python3
import sys
sys.path.append("/home/alacny/Programowanie/Python/Pandemic/lib")
import species as h
johny=h.Species()
johny.raiseInfection(100)
johny.setImmune()
johny.raiseInfection(10)
print(johny.getIllness())
