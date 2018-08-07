import numpy as np 
import matplotlib.pyplot as plt 
import os
import time 

#files = os.listdir("/home/mark/Dropbox/Stanford_ASL/Experiment_Data_Mark/Experiments") # returns list
'''
files = ['E2_COL_60s-02-11_08-58-20.npz', 'Experiment2-02-11_08-53-21.npz', 'Experiment-02-11_08-51-25.npz', 'Experiment2_COL_30s-07-05_16-47-25.npz', 'E1_COL_45s-02-11_08-52-13.npz', 
'E1_NOCOL_45s-02-11_09-38-00.npz', 'E2_NOCOL_45s-02-11_08-49-05.npz', 'E2_COL_45s-02-11_08-31-43.npz', 'Experiment2_COL_30s-02-11_09-41-22.npz', 
'E1_NOCOL_60s-02-11_09-28-26.npz', 'E1_NOCOL_45s-02-11_09-33-28.npz', 'Experiment-02-11_08-44-45.npz', 'Experiment2_NOCOL_30s-02-11_09-29-15.npz', 'E2_COL_60s-02-11_09-05-29.npz', 
'E1_COL_45s-02-11_08-45-04.npz', 'E1_NOCOL_60s-02-11_09-23-32.npz', 'E1_COL_45s-02-11_09-07-20.npz', 'Experiment-07-04_15-11-15.npz', 'E2_COL_45s-02-11_08-43-03.npz', 
'Experiment2-02-11_08-57-00.npz', 'Experiment2_NOCOL_30s-07-05_17-01-50.npz', 'Experiment-02-11_08-52-29.npz',
'Experiment2_NOCOL_45s-02-11_09-17-41.npz', 'E2_COL_60s-02-11_08-50-17.npz', 'E2_NOCOL_45s-02-11_08-55-06.npz', 'E1_COL_60s-02-11_09-12-09.npz', 'Experiment-07-04_15-22-50.npz', 
'Experiment2_COL_45s_-02-11_09-08-13.npz', 'E1_COL_60s-02-11_09-17-01.npz', 'E2_NOCOL_60s-02-11_08-40-48.npz', 'Experiment-02-11_09-18-12.npz', 'Experiment2_COL_30s-07-05_16-42-28.npz']
'''
files = ['E2_COL_60s-02-11_08-58-20.npz', 'Experiment2-02-11_08-53-21.npz', 'Experiment-02-11_08-51-25.npz', 'Experiment2_COL_30s-07-05_16-47-25.npz', 'E1_COL_45s-02-11_08-52-13.npz', 
'E1_NOCOL_45s-02-11_09-38-00.npz', 'E2_NOCOL_45s-02-11_08-49-05.npz', 'E2_COL_45s-02-11_08-31-43.npz', 'Experiment2_COL_30s-02-11_09-41-22.npz', 
'E1_NOCOL_60s-02-11_09-28-26.npz', 'E1_NOCOL_45s-02-11_09-33-28.npz', 'Experiment-02-11_08-44-45.npz', 'Experiment2_NOCOL_30s-02-11_09-29-15.npz', 'E2_COL_60s-02-11_09-05-29.npz', 
'E1_COL_45s-02-11_08-45-04.npz', 'E1_NOCOL_60s-02-11_09-23-32.npz', 'E1_COL_45s-02-11_09-07-20.npz', 'Experiment-07-04_15-11-15.npz', 'E2_COL_45s-02-11_08-43-03.npz', 
'Experiment2-02-11_08-57-00.npz', 'Experiment2_NOCOL_30s-07-05_17-01-50.npz', 'Experiment-02-11_08-52-29.npz',
'Experiment2_NOCOL_45s-02-11_09-17-41.npz', 'E2_COL_60s-02-11_08-50-17.npz', 'E2_NOCOL_45s-02-11_08-55-06.npz', 'E1_COL_60s-02-11_09-12-09.npz', 'Experiment-07-04_15-22-50.npz', 
'Experiment2_COL_45s_-02-11_09-08-13.npz', 'E1_COL_60s-02-11_09-17-01.npz', 'E2_NOCOL_60s-02-11_08-40-48.npz', 'Experiment-02-11_09-18-12.npz', 'Experiment2_COL_30s-07-05_16-42-28.npz']
good_files = ["E2_COL_60s-02-11_08-50-17.npz", 'E2_NOCOL_60s-02-11_08-40-48.npz', 'E2_COL_45s-02-11_08-43-03.npz', 'E2_NOCOL_45s-02-11_08-55-06.npz', 'E2_NOCOL_45s-02-11_08-49-05.npz']
 # 'E2_COL_60s-02-11_08-58-20.npz'

# Get data 
for i in range(good_files.__len__()):
	file_name = good_files[i]
	data = np.load(file_name)
	x_hist = data['state_history']
	ut_hist = data['thruster_cmd_history']
	uc = ut_hist
	uw_hist = data['wheel_vel_cmd_history']
	t_hist  = data['time_history']

	start_time = 1 
	stop_time = 220 
	Nsteps =  t_hist.__len__()

	# Show thrust
	u_mag = np.zeros(Nsteps) 
	for i in range(Nsteps):
		u_mag[i] = np.sum(np.abs(uc[:,i]))
		if u_mag[i]>8:
			u_mag[i]=8
	


###################


###################
	'''
	j_E2_COL_45s = True 
	if file_name[0:10] == "E2_COL_45s" and (j_E2_COL_45s):
#		if file_name == "E2_COL_60s-02-11_08-58-20.npz"
		print file_name
		start_time =70
		stop_time = 64+85
		j_E2_COL_45s = False
		E2_COL_45s = sum(u_mag[start_time:stop_time])
		plt.figure(1)
		plt.plot(t_hist[start_time:stop_time],u_mag[start_time:stop_time],'.')
		fig = plt.figure(2) 
		plt.plot(x_hist[0,start_time:stop_time],x_hist[1,start_time:stop_time],'b.')
		#plt.plot(x_hist[0,start_time:stop_time],x_hist[1,start_time:stop_time],'b--')
		plt.figure(33)
		plt.plot(t_hist,x_hist[1,:])
		plt.plot(t_hist[start_time],x_hist[1,start_time],'o')
		plt.plot(t_hist[stop_time],x_hist[1,stop_time],'o')
		print "E2_COL_45s = "+str(E2_COL_45s) 
	
	if file_name == "E2_NOCOL_45s-02-11_08-49-05.npz": #file_name[0:12] == "E2_NOCOL_45s":
		if file_name == "E2_NOCOL_45s-02-11_08-49-05.npz":
			print file_name
			start_time = 67
			stop_time = start_time + 85
		if file_name == "E2_NOCOL_45s-02-11_08-55-06.npz":
			print file_name
			start_time = 52
			stop_time = start_time + 85
		E2_NOCOL_45s = sum(u_mag[start_time:stop_time])
		print "E2_NOCOL_45s = "+str(E2_NOCOL_45s) 
		plt.figure(1)
		plt.plot(t_hist[start_time:stop_time],u_mag[start_time:stop_time],'g.')
		qwer = 69
		plt.plot(t_hist[qwer],u_mag[qwer],'go')
		plt.figure(2) 
		#plt.plot(x_hist[0,start_time:stop_time],x_hist[1,start_time:stop_time],'g')
		plt.plot(x_hist[0,start_time:stop_time],x_hist[1,start_time:stop_time],'g.')
		plt.figure(33)
		plt.plot(t_hist,x_hist[1,:])
		plt.plot(t_hist[start_time],x_hist[1,start_time],'o')
		plt.plot(t_hist[stop_time],x_hist[1,stop_time],'o')
	'''

###################
	
	if file_name ==  "E2_COL_60s-02-11_08-50-17.npz":   #file_name[0:10] == "E2_COL_60s":
		print file_name
		start_time = 64
		stop_time = 64+110
		j_E2_COL_60s = False
		E2_COL_60s = sum(u_mag[start_time:stop_time])
		plt.figure(1)
		plt.plot(t_hist[start_time:stop_time],u_mag[start_time:stop_time],'.')
		plt.figure(2) 
		plt.plot(x_hist[0,start_time:stop_time],x_hist[1,start_time:stop_time],'.')
		plt.figure(33)
		plt.plot(t_hist,x_hist[1,:])
		plt.plot(t_hist[start_time],x_hist[1,start_time],'o')
		plt.plot(t_hist[stop_time],x_hist[1,stop_time],'o')
		print "E2_COL_60s = "+str(E2_COL_60s) 
		
	if file_name[0:12] == "E2_NOCOL_60s":
		print file_name
		start_time = 69
		stop_time = start_time + 110
		E2_NOCOL_60s = sum(u_mag[start_time:stop_time])
		print "E2_NOCOL_60s = "+str(E2_NOCOL_60s) 
		plt.figure(1)
		plt.plot(t_hist[start_time:Nsteps],u_mag[start_time:Nsteps],'.')
		qwer = 69
		plt.xlabel('Time Step')
		plt.ylabel('Thrust Magnitude')
		plt.plot(t_hist[qwer],u_mag[qwer],'go')
		plt.figure(2) 
		plt.plot(x_hist[0,start_time:Nsteps],x_hist[1,start_time:Nsteps],'.')
		plt.figure(33)
		plt.plot(t_hist,x_hist[1,:])
		plt.plot(t_hist[start_time],x_hist[1,start_time],'o')
		plt.plot(t_hist[stop_time],x_hist[1,stop_time],'o')
	

###################

'''
	if file_name[0:10] == "E2_COL_45s":
		E2_COL_45s = sum(u_mag)
		print "E2_COL_45s = "+str(E2_COL_45s) 
		plt.plot(t_hist,u_mag,'rx')
	if file_name[0:12] == "E2_NOCOL_45s":
		E2_NOCOL_45s = sum(u_mag)
		print "E2_NOCOL_45s = "+str(E2_NOCOL_45s)
		plt.plot(t_hist,u_mag,'rx')

'''


fig = plt.figure(2)

actual_bounds = [0.110, 0.110, 3.453, 2.52] # [0.110, 0.103, 3.453, 2.52]
robot_radius = 0.15
epsilon = 0.032
R = robot_radius
R  = 0.61 + robot_radius # Exp 1 
Ry = 0.55 + epsilon							# 0.3 + self.robot_radius
Rx = robot_radius + 0.14 - epsilon
boundary = [actual_bounds[0]-robot_radius, actual_bounds[1]-robot_radius,actual_bounds[2]+robot_radius, actual_bounds[3]+robot_radius ]
avoid_box = np.array([[boundary[2]/2-R], [boundary[3]/2-2*R], [boundary[2]/2+R], [boundary[3]] ])
avoid_box = np.array([[boundary[2]/2-Rx-0.075], [boundary[1]+Ry], [boundary[2]/2+Rx], [boundary[3] - robot_radius ] ])
plt.plot([avoid_box[0],avoid_box[2],avoid_box[2],avoid_box[0],avoid_box[0]],[avoid_box[1],avoid_box[1],avoid_box[3],avoid_box[3],avoid_box[1]],'k--')

R  = 0.61 # Exp 1 
Ry = 0.55 + robot_radius +epsilon										# 0.3 + self.robot_radius
Rx = 0.14 - epsilon
avoid_box = np.array([[boundary[2]/2-Rx-0.075], [boundary[1]+Ry], [boundary[2]/2+Rx], [boundary[3]-robot_radius] ])
plt.plot([avoid_box[0],avoid_box[2],avoid_box[2],avoid_box[0],avoid_box[0]],[avoid_box[1],avoid_box[1],avoid_box[3],avoid_box[3],avoid_box[1]],'k')

#avoid_box = np.array([[boundary[2]/2-2*R], [boundary[3]/2-3*R], [boundary[2]/2+2*R], [boundary[3]] ])
#plt.plot([avoid_box[0],avoid_box[2],avoid_box[2],avoid_box[0],avoid_box[0]],[avoid_box[1],avoid_box[1],avoid_box[3],avoid_box[3],avoid_box[1]])

plt.plot([actual_bounds[0],actual_bounds[2],actual_bounds[2],actual_bounds[0],actual_bounds[0]],[actual_bounds[1],actual_bounds[1],actual_bounds[3],actual_bounds[3],actual_bounds[1]],'k')

e2 = 0.02
plt.axis([actual_bounds[0]-e2, actual_bounds[2]+e2, actual_bounds[1]-e2, actual_bounds[3]+e2,])

plt.xlabel('x position ($s_x$) [m]')
plt.ylabel('y position ($s_y$) [m]')
fig.savefig('traj_comp.eps', format='eps', dpi=300)

#plt.grid()

plt.show()


#E2_COL_60s-02-11_08-50-17.npz
E2_COL_60s = 141.643666361
#E2_NOCOL_60s-02-11_08-40-48.npz
E2_NOCOL_60s = 175.619843412
#E2_COL_45s-02-11_08-43-03.npz
E2_COL_45s = 196.275594891
#E2_NOCOL_45s-02-11_08-55-06.npz
E2_NOCOL_45s = 236.776619584
#E2_NOCOL_45s-02-11_08-49-05.npz
E2_NOCOL_45s = 262.46890665
