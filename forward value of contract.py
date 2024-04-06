import numpy as np
#define variables
r=0.0225 #risk free rate
S_0=206 #current value of contract
T=3
c=0.25 #carry cost

#define discount function
def disc(t,T,r):
    d=(1+r)**(t-T)
    return d

#define forward value at 0 of forward maturity at time T

def Forward(S_0,r,T,c):
    carry=c*np.ones(T) #generate payment array for carry cost
    
    carry = carry*(1+r)**(-np.arange(T)) #discount carry
   
    F=(S_0+np.sum(carry))/disc(0,T,r)
    return F


#define forward value at t of forward maturity at time T set at t=0

def forward_t(S_0,r,T,t):
    f_t=(Forward(S_0,r,T-t,c)-Forward(S_0,r,T,c))*disc(t,T,r)
    return f_t
print(Forward(S_0,r,T,0))


