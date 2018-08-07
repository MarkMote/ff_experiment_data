import numpy as np 
import matplotlib.pyplot as plt 

# Get data 
file_name = "E1_COL_45s-02-11_08-45-04.npz"
data = np.load(file_name)
x_hist = data['state_history']
ut_hist = data['thruster_cmd_history']
uc = ut_hist
uw_hist = data['wheel_vel_cmd_history']
t_hist  = data['time_history']

start_time = 1 
stop_time = 220 
Nsteps =  t_hist.__len__()
print t_hist 


# Show traj 
plt.figure(0)
plt.plot(x_hist[0,:], x_hist[1,:],'.')
plt.axis([0, 3.6576, 0, 2.7432])
plt.xlabel('X position (meters)')
plt.ylabel('Y position (meters)')


# Show thrust
u_mag = np.zeros(Nsteps) 
for i in range(Nsteps):
	u_mag[i] = np.sum()
	

#plt.figure(1)
#plt.plot(t_hist, uc)

plt.show()

'''
# Show y position 
plt.figure(1)
plt.subplot(211)
plt.plot(t_hist, x_hist[1,:],'.')
plt.xlabel('Time (s)')
plt.ylabel('Y position (meters)')
plt.axis([start_time,stop_time,0,1])
plt.subplot(212)
plt.plot(t_hist, x_hist[4,:],'.')
plt.xlabel('Time (s)')
plt.ylabel('Y velocity (m/s)')
plt.axis([start_time,stop_time,-0.4,0.25])
plt.show()


thrust_max = 0.2
plt.figure(3)

for i in range(uw_hist.__len__() - 1  ) : 
	T = np.array([[np.cos(x_hist[2,i]), np.sin(x_hist[2,i]) ],[np.sin(x_hist[2,i]), np.cos(x_hist[2,i])]])	
	Fx_body = (np.double(uc[2,i]+uc[5,i]-uc[1,i]-uc[6,i]))*thrust_max 
	Fy_body = (np.double(uc[4,i]+uc[7,i]-uc[0,i]-uc[3,i]))*thrust_max 
	Fmag = np.linalg.norm([np.array([Fx_body, Fy_body])])
	Fx_tb = T[0][0]*Fx_body + T[0][1]*Fy_body 
	Fy_tb = T[1][0]*Fx_body + T[1][1]*Fy_body 
	ax_tb = (x_hist[3, i+1] - x_hist[3, i])/(t_hist[i+1]-t_hist[i])
	ay_tb = (x_hist[4, i+1] - x_hist[4, i])/(t_hist[i+1]-t_hist[i])
	amag = np.linalg.norm([np.array([ax_tb, ay_tb])])
	plt.subplot(211)
	# print Fx_tb
	plt.plot(float(t_hist[i]), float(Fmag),'.',color="red")
	plt.plot(float(t_hist[i]), float(18.5*amag),'.',color="blue")
	plt.ylabel('||Force||, ||Accel||*18.5 ')
	plt.xlabel('Time (s)')

	plt.subplot(212)
	plt.plot(float(t_hist[i]), float(Fmag/amag),'.',color="red")
	plt.ylabel('||Force/Accel||')
	plt.xlabel('Time (s)')


plt.subplot(211)
plt.axis([start_time,stop_time,-0.05,0.48])
plt.subplot(212)
plt.axis([start_time,stop_time,-0.5,22])
plt.show()
'''