# find mod programming with math module
import math

dividing=int(input("Enter the dividing: "))

divisive=int(input("Enter the divisive: "))

def remainder():
    
    mod=int(math.fmod(dividing,divisive))
    section=dividing//divisive
    print(dividing,"divided by",divisive,"is",section,"and  remainder",mod)

remainder()
