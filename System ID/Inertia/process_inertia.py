import numpy as np 
import matplotlib.pyplot as plt 

plt.close('all')

# Options 
plot_wheel_vel = True 
start_time = 10
stop_time = 100

file_name = "SYSID_inertia_1.npz"
data = np.load(file_name)
x_hist = data['state_history']          
ut_hist = data['thruster_cmd_history']
uc = ut_hist
xw_hist = data['wheel_vel_history']       # rad/s
uwc_hist = data['wheel_vel_cmd_history']  # RPM
t_hist  = data['time_history']

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


# Get data 
file_name = "SYS_ID_1.npz"
data = np.load(file_name)
x_hist = data['state_history']          
ut_hist = data['thruster_cmd_history']
uc = ut_hist
xw_hist = data['wheel_vel_history']       # rad/s
uwc_hist = data['wheel_vel_cmd_history']  # RPM
t_hist  = data['time_history']

if plot_wheel_vel : 
	plt.figure(1) 
	plt.subplot(211)
	plt.plot(t_hist,np.multiply(30./np.pi,xw_hist), color = "blue")
	plt.plot(t_hist,uwc_hist, color = "red")
	#plt.axis([start_time,stop_time,0,380])

	plt.subplot(212)
	plt.plot(t_hist-1,x_hist[5], color = "red")
	#plt.plot(t_hist,x_hist[5],'.')
	#plt.plot(t_hist,x_hist[3]+np.multiply(0.155,x_hist[5]),'.')
	#plt.axis([start_time,stop_time,-0.05,0.48])

	plt.figure(2) 
	plt.plot(t_hist,xw_hist/x_hist[5], color = "red")

# Get data 
file_name = "SYS_ID_2.npz"
data = np.load(file_name)
x_hist = data['state_history']
ut_hist = data['thruster_cmd_history']
uc = ut_hist
xw_hist = data['wheel_vel_history']
uwc_hist = data['wheel_vel_cmd_history']
t_hist  = data['time_history']

if plot_wheel_vel : 
	plt.figure(1) 
	plt.subplot(211)
	plt.plot(t_hist,np.multiply(30./np.pi,xw_hist), color = "blue")
	#plt.axis([start_time,stop_time,0,380])

	plt.subplot(212)
	plt.plot(t_hist-1,x_hist[5]-2.65, color = "green")

	plt.figure(2) 
	plt.plot(t_hist,xw_hist/(x_hist[5]-2.65), color = "green")
	plt.grid()

	
# Get data 
file_name = "SYS_ID_3.npz"
data = np.load(file_name)
x_hist = data['state_history']
ut_hist = data['thruster_cmd_history']
uc = ut_hist
xw_hist = data['wheel_vel_history']     
uwc_hist = data['wheel_vel_cmd_history']
t_hist  = data['time_history']

if plot_wheel_vel : 
	plt.figure(1) 
	plt.subplot(211)
	plt.plot(t_hist,np.multiply(30./np.pi,xw_hist), color = "blue")
	plt.axis([start_time,stop_time,0,380])

	plt.subplot(212)
	plt.plot(t_hist-1,x_hist[5], color = "cyan")
	plt.axis([start_time,stop_time,-5.25,0.5])

	plt.figure(2) 
	#plt.plot(t_hist,xw_hist/x_hist[5], color = "cyan")
	plt.axis([65,stop_time,-10,0])



	# Wrap it up 	plt.figure(2) 
	plt.figure(1)
	plt.plot(t_hist,xw_hist/x_hist[5])
	plt.subplot(211)
	plt.plot([start_time,stop_time],[200,200],'c--')
	plt.plot([start_time,stop_time],[200-140,200-140],'r--')
	plt.plot([start_time,stop_time],[200+140,200+140],'r--')
	yr = 110
	plt.plot([start_time,stop_time],[200-yr,200-yr],'g--')
	plt.plot([start_time,stop_time],[200+yr,200+yr],'g--')
	plt.plot([26, 26],[-1000,1000],'k--')
	plt.plot([81, 81],[-1000,1000],'k--')
	plt.xlabel('Time (s)')
	plt.ylabel('Wheel Velocity (RPM)')
	plt.title("Inertia System ID")

	plt.subplot(212)
	plt.xlabel('Time (s)')
	plt.ylabel('Body Rotation Rate (rad/s)')
	plt.plot([26, 26],[-10,10],'k--')
	plt.plot([81, 81],[-10,10],'k--')
	#plt.show()

	plt.figure(2) 
	plt.xlabel('Time (s)')
	plt.ylabel('Angular Velocity Ratio (Omg_w/Omg_b)')
	plt.plot([start_time, stop_time],[-7,-7],'k--')
	plt.plot([start_time, stop_time],[-7.5,-7.5],'k--')

	

	plt.show()





# pm 110 
# pm 140

