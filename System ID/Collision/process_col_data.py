import numpy as np 
import matplotlib.pyplot as plt 

plt.close('all')

# Options 
plot_wheel_vel = True 
start_time = 10
stop_time = 100

#file_name = "sys_id_col_gen_1.npz"
file_name = "sys_id_col_gen_2.npz"
data = np.load(file_name)
x_hist = data['state_history']          
#ut_hist = data['thruster_cmd_history']
#uc = ut_hist
#xw_hist = data['wheel_vel_history']       # rad/s
#uwc_hist = data['wheel_vel_cmd_history']  # RPM
t_hist  = data['time_history']

plt.figure(1) 
plt.plot(t_hist, x_hist[1])
plt.plot(t_hist, x_hist[1],'.')


plt.figure(2)
plt.subplot(311)
plt.plot(t_hist, x_hist[3])
plt.subplot(312)
plt.plot(t_hist, x_hist[4])
plt.subplot(313)
plt.plot(t_hist, x_hist[5])
plt.subplot(311)
plt.plot(t_hist, x_hist[3],'.')
plt.subplot(312)
plt.plot(t_hist, x_hist[4],'.')
plt.subplot(313)
plt.plot(t_hist, x_hist[5],'.')

#col_times = [44.3, 73, 106.2, 114.6, 134.2, 151.4, 171.7, 194.8, 212.8, 227.6, 247.4, 264.31, 280, 294.8, 309.4]
col_times = [32.68,55.52,74.72,90.81,105.35,138.57,158.6,175.3,192.1]
for i  in col_times: 
	plt.subplot(311)
	plt.plot([i, i], [-10,10])
	plt.subplot(312)
	plt.plot([i, i], [-10,10])
	plt.subplot(313)
	plt.plot([i, i], [-10,10])


plt.subplot(311)
plt.grid()
plt.axis([0, 325,-0.2,0.2])
plt.ylabel("X-Velocity")
plt.subplot(312)
plt.grid()
plt.axis([0, 325,-0.25,0.15])
plt.ylabel("Y-Velocity")
plt.subplot(313)
plt.grid()
plt.axis([0, 325,-1.8,1])
plt.ylabel("OMG-Velocity")
plt.show()



'''
if plot_wheel_vel : 
	plt.figure(1) 
	plt.subplot(211)
	plt.plot(t_hist,np.multiply(30./np.pi,xw_hist), color = "blue")
	plt.plot(t_hist,uwc_hist, color = "red")
	#plt.axis([start_time,stop_time,0,380])

	plt.subplot(212)
	plt.plot(t_hist-1,x_hist[5]-2.3, color = "blue")

	plt.figure(2) 
	plt.plot(t_hist,xw_hist/(x_hist[5]-2.3), color = "blue")
''' 