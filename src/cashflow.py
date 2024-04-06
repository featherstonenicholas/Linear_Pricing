import numpy as np
#define parameters
cashflow=[0,10,10,10,10] #cashflow to value
r=0.01 #risk free rate per time period

# Value the cashflow
def flowvalue(cashflow,r):
    n=len(cashflow)
    disc=(1+r)**-np.arange(n) #create discout array
    current_value=np.sum(cashflow*disc) #discount cashflow
    return current_value
print(flowvalue(cashflow,r))


