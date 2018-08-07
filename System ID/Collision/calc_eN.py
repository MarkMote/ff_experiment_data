import numpy as np 
import math 
import matplotlib.pyplot as plt 

# Get data 
file_name = "sys_id_col_gen_3.npz"
data = np.load(file_name)
x_hist = data['state_history']
ut_hist = data['thruster_history']
uc = ut_hist
uw_hist = data['wheel_vel_history']
t_hist  = data['time_history']


# Data with zero tangential velocity 
colVel = np.array([[-0.11, 0.05],[-0.08, 0.04],[-0.06, 0.03],[-0.1, 0.04],[-0.11, 0.08],
	[-0.13, 0.05],[-0.14, 0.07],[-0.18, 0.08],[-0.15, 0.04],[-0.25, 0.1],[-0.20, 0.10],
	[-0.087, 0.043],[-0.066, 0.037],[-0.106,0.056],[-0.097,0.053],[-0.062,0.035],
	[-0.038,0.021],[-0.12,0.0614]])

plt.figure(0)
plt.plot(-colVel[:,0],colVel[:,1],'x')
xmax = 0.27
ymax = 0.12 
eN = np.divide(colVel[:,1],colVel[:,0])
print np.mean(eN)



plt.axis([0,xmax,0,ymax])
plt.show()



