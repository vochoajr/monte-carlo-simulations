import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def f(x):
	return np.abs(x)
	
def acceptReject(N):
	listx = [] #lists that will hold x
	
	#do experiments
	while len(listx) < N:
		x = np.random.uniform(-1,1) # generate observation for x
		y = np.random.uniform(0,1) # generate observation for y
		if y < f(x): #if true: accept, else: reject
			listx.append(x)
	return listx

nBins = 50
N = 10000
M1,M2,M4,M8,M16,M32 = 1,2,4,8,16,32
means = []
stddev =[]
lists1, lists2, lists4, lists8, lists16, lists32 = [], [], [], [], [], []

for i in range(N):
	x_i = acceptReject(M1)
	s = np.sum(x_i)
	lists1.append(s)
mean1 = np.mean(lists1)
std1 = np.std(lists1)

for i in range(N):
	x_i = acceptReject(M2)
	s = np.sum(x_i)
	lists2.append(s)
mean2 = np.mean(lists2)
std2 = np.std(lists2)

for i in range(N):
	x_i = acceptReject(M4)
	s = np.sum(x_i)
	lists4.append(s)
mean4 = np.mean(lists4)
std4 = np.std(lists4)

for i in range(N):
	x_i = acceptReject(M8)
	s = np.sum(x_i)
	lists8.append(s)
mean8 = np.mean(lists8)
std8 = np.std(lists8)

for i in range(N):
	x_i = acceptReject(M16)
	s = np.sum(x_i)
	lists16.append(s)
mean16 = np.mean(lists16)
std16 = np.std(lists16)

for i in range(N):
	x_i = acceptReject(M32)
	s = np.sum(x_i)
	lists32.append(s)
mean32 = np.mean(lists32)
std32 = np.std(lists32)

#setup figures
fig = plt.figure(figsize=(13,5)) #figsize=(width, height) in inches
fig_1 = fig.add_subplot(2,3,1)
fig_2 = fig.add_subplot(2,3,2)
fig_3 = fig.add_subplot(2,3,3)
fig_4 = fig.add_subplot(2,3,4)
fig_5 = fig.add_subplot(2,3,5)
fig_6 = fig.add_subplot(2,3,6)

fig_1.set_title("M = 1")
fig_1.text(-0.75, 0.9, "mean = " +str(mean1), color='r')
fig_1.text(-0.75, 0.7, "std dev = " +str(std1), color='r')

fig_2.set_title("M = 2")
fig_2.text(-1.5, 0.5, "mean = " +str(mean2), color='r')
fig_2.text(-1.5, 0.4, "std dev = " +str(std2), color='r')

fig_3.set_title("M = 4")
fig_3.text(-3., 0.25, "mean = " +str(mean4), color='r')
fig_3.text(-3., 0.2, "std dev = " +str(std4), color='r')

fig_4.set_title("M = 8")
fig_4.text(-6., 0.15, "mean = " +str(mean8), color='r')
fig_4.text(-6., 0.10, "std dev = " +str(std8), color='r')

fig_5.set_title("M = 16")
fig_5.text(-10., 0.12, "mean = " +str(mean16), color='r')
fig_5.text(-10., 0.10, "std dev = " +str(std16), color='r')

fig_6.set_title("M = 32")
fig_6.text(-10., 0.10, "mean = " +str(mean32), color='r')
fig_6.text(-10., 0.08, "std dev = " +str(std32), color='r')

binHeight, binEdges, patches = fig_1.hist(lists1,nBins, normed = True)
y = mlab.normpdf( binEdges, mean1, std1)
l = fig_1.plot(binEdges, y, 'g', linewidth=2)

binHeight, binEdges, patches = fig_2.hist(lists2,nBins, normed = True)
y = mlab.normpdf( binEdges, mean2, std2)
l = fig_2.plot(binEdges, y, 'g', linewidth=2)

binHeight, binEdges, patches = fig_3.hist(lists4,nBins, normed = True)
y = mlab.normpdf( binEdges, mean4, std4)
l = fig_3.plot(binEdges, y, 'g', linewidth=2)

binHeight, binEdges, patches = fig_4.hist(lists8,nBins, normed = True)
y = mlab.normpdf( binEdges, mean8, std8)
l = fig_4.plot(binEdges, y, 'g', linewidth=2)

binHeight, binEdges, patches = fig_5.hist(lists16,nBins, normed = True)
y = mlab.normpdf( binEdges, mean16, std16)
l = fig_5.plot(binEdges, y, 'g', linewidth=2)

binHeight, binEdges, patches = fig_6.hist(lists32,nBins, normed = True)
y = mlab.normpdf( binEdges, mean32, std32)
l = fig_6.plot(binEdges, y, 'g', linewidth=2)

fig.savefig('result4.pdf')
fig.show()