import numpy as np 
import matplotlib.pyplot as plt 

#E2_NOCOL_45s-02-11_08-49-05.npz
E2_NOCOL_60s = 175.619843412
E2_NOCOL_45s = 262.46890665
#E2_NOCOL_45s = 236.776619584
#E2_NOCOL_45s = 262.46890665/2+236.776619584/2


#E2_COL_45s-02-11_08-31-43.npz
E2_COL_60s = 141.643666361
#E2_COL_45s = 198.920283716
E2_COL_45s = 196.275594891

print "Print 60s"
print 1-E2_COL_60s/E2_NOCOL_60s
print 1-E2_COL_45s/E2_NOCOL_45s


print 141.643666361*141.643666361