# -*- coding: cp1254 -*-

import math

def vucutYuzeyAlani(boy, agirlik):
    yanit = 0.20247 * math.pow(boy/100.0, 0.725) * math.pow(agirlik, 0.425)
    return round(yanit,2)

def yagsizVucutAgirligi(erkekKadin, boy):
    if erkekKadin == "ERKEK":
        yagsizAg = (0.73 * boy) - 59.42
    else:
        yagsizAg = (0.65 * boy) - 50.74
    return round(yagsizAg,1)

def idealVucutAgirligi(erkekKadin, boy):
    if (erkekKadin == "ERKEK"):
        idealAg = 50 + (2.3 * (cmInchCevir(boy) - 60))
    else:
        idealAg = 45.5 + (2.3 * (cmInchCevir(boy) - 60))
    return round(idealAg,1)    

def bodyMassIndex(boy, agirlik):
    bmi = (agirlik/2.205) / ((boy/39.37) ** 2)
    return round(bmi,2)

def cmInchCevir(cm):
    return cm / 2.54

print "Ideal vücut ağirliği: ",  idealVucutAgirligi("ERKEK", 176)
print "Yüzey alanı: ", vucutYuzeyAlani(176, 67)
print "BMI: ", bodyMassIndex(176, 67)
print "Yağsız vücut ağırlığı: ", yagsizVucutAgirligi("ERKEK", 176)                                                   
