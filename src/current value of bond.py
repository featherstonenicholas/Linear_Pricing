import numpy as np
#define variables
r=0.0225 #risk free rate
F=100 #face value of bond
T=6
c=0 #coupon rate

#define discount function
def disc(t,T,r):
    d=(1+r)**(t-T)
    return d


#define current value at 0 of bond maturity at time T

def bond_value(F,r,T,c):
    coupon=np.hstack([0,c*F*np.ones(T)]) #generate payment array for coupons
    
    coupon = coupon*disc(0,np.arange(T+1),r) #discount coupons
        
    value=F*disc(0,T,r)+np.sum(coupon)
    return value
print(bond_value(F,r,T,c))