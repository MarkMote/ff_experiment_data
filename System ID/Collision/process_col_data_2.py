import numpy as np 
import matplotlib.pyplot as plt 

plt.close('all')

# Options 
plot_wheel_vel = True 
start_time = 10
stop_time = 100

#file_name = "sys_id_col_gen_1.npz"
file_name = "sys_id_col_gen_7.npz"
data = np.load(file_name)
x_hist = data['state_history']          
t_hist  = data['time_history']

plt.figure(1) 
plt.plot(t_hist, x_hist[1])
plt.plot(t_hist, x_hist[1],'.')
plt.xlabel("Time (s)")
plt.ylabel("Y-Position (m)")

#it_minus = [29, 51, 69, 83, 97, 112, 129, 148, 164, 180, 196, 211, 252, 273, 289] #"sys_id_col_gen_2.npz"
#it_plus  = [31, 53, 71, 86,100, 115, 132, 151, 168, 183, 199, 214, 255, 276, 292] #"sys_id_col_gen_2.npz"
#it_minus = [22, 42, 60, 78, 98, 115, 154, 173, 192, 211, 225, 260, 275]   #"sys_id_col_gen_3.npz"
#it_plus  = [25, 45, 63, 81, 100, 118, 157, 175, 195, 214, 228, 263, 278]  #"sys_id_col_gen_3.npz"
#it_minus = [33, 53, 68, 86, 100, 126, 147, 172, 189, 205, 228, 249, 274]  #"sys_id_col_gen_4.npz"
#it_plus  = [37, 56, 71, 89, 103, 129, 150, 175, 191, 208, 231, 252, 277]  #"sys_id_col_gen_4.npz"
#it_minus = [25, 49, 67, 84, 99, 112, 125, 141, 160, 179, 194, 209, 226, 237, 250, 263, 280, 294]  #"sys_id_col_gen_5.npz"
#it_plus  = [27, 52, 69, 87, 102, 115, 128, 144, 163, 181, 197, 212, 229, 240, 253, 266, 283, 297]  #"sys_id_col_gen_5.npz"
#it_minus = [23, 41, 60, 78, 98, 115, 154, 173, 192, 211, 225, 260, 275]  #"sys_id_col_gen_6.npz"
#it_plus  = [25, 44, 63, 81, 101, 118, 157, 176, 195, 214, 228, 263, 278]  #"sys_id_col_gen_6.npz"
it_minus = [23]  #"sys_id_col_gen_7.npz"
it_plus  = [25]  #"sys_id_col_gen_7.npz"


for i in it_minus :
	plt.plot(t_hist[i], x_hist[1,i],'ro')
for i in it_plus: 
	plt.plot(t_hist[i], x_hist[1,i],'bo')


plt.figure(2)
plt.subplot(311)
plt.plot(t_hist, x_hist[3])
plt.subplot(312)
plt.plot(t_hist, x_hist[4])
plt.subplot(313)
plt.plot(t_hist, x_hist[5])

for i in it_minus:
	plt.subplot(311)
	plt.plot(t_hist[i], x_hist[3,i],'r.')
	plt.subplot(312)
	plt.plot(t_hist[i], x_hist[4,i],'r.')
	plt.subplot(313)
	plt.plot(t_hist[i], x_hist[5,i],'r.')
for i in it_plus:
	plt.subplot(311)
	plt.plot(t_hist[i], x_hist[3,i],'go')
	plt.subplot(312)
	plt.plot(t_hist[i], x_hist[4,i],'go')
	plt.subplot(313)
	plt.plot(t_hist[i], x_hist[5,i],'go')

#col_times = [44.3, 73, 106.2, 114.6, 134.2, 151.4, 171.7, 194.8, 212.8, 227.6, 247.4, 264.31, 280, 294.8, 309.4]
for i  in it_minus: 
	i = t_hist[i]+1
	plt.subplot(311)
	plt.plot([i, i], [-10,10])
	plt.subplot(312)
	plt.plot([i, i], [-10,10])
	plt.subplot(313)
	plt.plot([i, i], [-10,10])


plt.subplot(311)
plt.grid()
plt.axis([0, 325,-0.25,0.25])
plt.ylabel("X-Velocity")
plt.subplot(312)
plt.grid()
plt.axis([0, 325,-0.25,0.25])
plt.ylabel("Y-Velocity")
plt.subplot(313)
plt.grid()
plt.axis([0, 325,-2.5,2.5])
plt.ylabel("Omega")
plt.xlabel("Time (s)")

for i in range(it_minus.__len__()):
	print "["+str(x_hist[3,it_minus[i]])+", "+str(x_hist[4,it_minus[i]])+", "+str(x_hist[5,it_minus[i]])+", "+str(x_hist[3,it_plus[i]])+", "+str(x_hist[4,it_plus[i]])+", "+str(x_hist[5,it_plus[i]])+"],"


plt.show()


