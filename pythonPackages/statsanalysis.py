import matplotlib.pyplot as plt
import random
import numpy as np

steps = 20

population = []
bias = 0
time = []
for _ in range(steps):
	time.append(_)
	bias += random.gauss(-20,30)
	population.append(bias + random.gauss(800,20) - random.uniform(0,300))
plt.plot(population)
plt.ylim(0,1000)


previous_state = state = [population[0], population[1]-population[0]]
state = [population[0], population[1]-population[0]]

A = np.array([[1.,1.],[0.,1.]])
improved = []
v_cov = 0.9
neg = 0
gainz = []
for datum in population:
	innovation = datum - state[0] # error
	if innovation < 0:
		neg += -2*innovation/state[0]
	else:
		neg = 0
	gain1 = 0.9 if innovation > 0 else min(0.2*neg,1)
	gainz.append(min(0.2*neg,1)*200)

	state[0] = state[0] + gain1 * innovation # correction
	improved.append(state[0]) # posterior

	state[1] = state[1]* (1-v_cov) + v_cov * (state[0] - previous_state[0])
	# prediction
	previous_state = state
	state = np.matmul(A, state)
	v_cov = v_cov * 0.9


plt.plot(time,population,time,improved,time,gainz)
plt.ylim(0,1000)
plt.show()
