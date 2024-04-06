import numpy as np
#define variables
A=10 #payment per time period
r=0.01 #risk free rate per time period
first=1 #first payemnt in advance (0) or in arrears (1)

#define value of perpetuity
def perpetuity(A,r,first):
    value = ((1+r)**(1-first))/r*A
    return value
print(perpetuity(A,r,first))