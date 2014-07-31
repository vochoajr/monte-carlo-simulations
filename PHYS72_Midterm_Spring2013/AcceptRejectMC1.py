import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def f(x):
	return np.abs(x)

def acceptReject(N):
	listx = [] #lists that will hold x
	
	#do experiments
	for i in range(N):
		x = np.random.uniform(-1,1) # generate observation for x
		y = np.random.uniform(0,1) # generate observation for y
		if y < f(x): #if true: accept, else: reject
			listx.append(x)
	return listx

def makePlots():
	# number of Monte Carlo Experiments
	N_e2 = 100
	N_e3 = 1000
	N_e5 = 100000
	nBins = 50 # number of bins for Histograms
	
	# carry out accept/reject algorithm for each number of MC experiments
	listx_e2 = acceptReject(N_e2)
	listx_e3 = acceptReject(N_e3)
	listx_e5 = acceptReject(N_e5)
	
	efficiency_e2 = len(listx_e2) / float(N_e2)
	efficiency_e3 = len(listx_e3) / float(N_e3)
	efficiency_e5 = len(listx_e5) / float(N_e5)
	
	mean_e2 = np.mean(listx_e2)
	stddev_e2 = np.std(listx_e2)
	mean_e3 = np.mean(listx_e3)
	stddev_e3 = np.std(listx_e3)
	mean_e5 = np.mean(listx_e5)
	stddev_e5 = np.std(listx_e5)
	
	#setup figures
	fig = plt.figure(figsize=(13,5)) #figsize=(width, height) in inches
	fig_x2 = fig.add_subplot(1,3,1)
	fig_x3 = fig.add_subplot(1,3,2)
	fig_x5 = fig.add_subplot(1,3,3)
	
	binHeight, binEdges, patches = fig_x2.hist(listx_e2,nBins,normed=True)
	fig_x2.set_title("N = " + str(N_e2))
	fig_x2.text(-0.5, 1.5, "mean = " +str(mean_e2))
	fig_x2.text(-0.5, 1.0, "std = " +str(stddev_e2))
	fig_x2.text(-0.5, 0.5, "efficiency = " +str(efficiency_e2))
	
	listx_e2a = np.array(listx_e2)
	points = [listx_e2a.min(), 0, listx_e2a.max()]
	absf = np.abs(points)
	fig_x2.plot(points,absf, 'g', linewidth=2)
	
	binHeight, binEdges, patches = fig_x3.hist(listx_e3,nBins,normed=True)
	fig_x3.set_title("N = " + str(N_e3))
	fig_x3.text(-0.5, 1.0, "mean = " +str(mean_e3))
	fig_x3.text(-0.5, 0.8, "std = " +str(stddev_e3))
	fig_x3.text(-0.5, 0.6, "efficiency = " +str(efficiency_e3))
	
	listx_e3a = np.array(listx_e3)
	points = [listx_e3a.min(), 0, listx_e3a.max()]
	absf = np.abs(points)
	fig_x3.plot(points,absf, 'g', linewidth=2)
	
	binHeight, binEdges, patches = fig_x5.hist(listx_e5,nBins,normed=True)
	fig_x5.set_title("N = " + str(N_e5))
	fig_x5.text(-0.5, 0.8, "mean = " +str(mean_e5))
	fig_x5.text(-0.5, 0.7, "std = " +str(stddev_e5))
	fig_x5.text(-0.5, 0.6, "efficiency = " +str(efficiency_e5))
	
	listx_e5a = np.array(listx_e5)
	points = [listx_e5a.min(), 0, listx_e5a.max()]
	absf = np.abs(points)
	fig_x5.plot(points,absf, 'g', linewidth=2)
	
	#y = mlab.normpdf( binEdges, mean_e5, stddev_e5)
	#l = fig_x5.plot(binEdges, y, 'g', linewidth=2)
	
	fig.savefig('result1.pdf')
	fig.show()

makePlots()
	
