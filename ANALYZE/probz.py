import os
import random

#create a nxn square array
def create(n):
	new = []
	for i in range(n):
		new.append(0)
		i = 1 + i
	return new


#return either the miniumum or max value in a 1D array
def minmax(array, what_to_do):
	new = [0]
	if what_to_do == "minimum":
		for i in range(len(array)):
			if array[i]	< new[0]:
				new[0] = array[i]
	else:
		for i in range(len(array)):
			if array[i]	> new[0]:
				new[0] = array[i]
	return new[0]


#sum the entire (one-dimensional) matrix up
def the_sum(matrix):
	x = 0.0
	for i in range(len(matrix)):
		x = x + matrix[i]
	return x

#average value of an array of numbers
def the_average(array):
	
	a_sum = the_sum(array)
	average = a_sum / float(len(array))

	return average


#find the factorial of a positive integer i
def factorial(i):
	new = [1]
	while i > 1:		
		new[0] = i*new[0]
		i = i-1
	return new[0]


#set the initial conditions randomly
def rand_initial():
	start = create(random.randrange(5, 25))
	for i in range(len(start)):
		start[i] = random.randrange(30)
	return start

#mass function of probability of obtaining that random variable
def probabilities(distribution):
	new = create(len(distribution))
	x = the_sum(distribution)
	for i in range(len(distribution)):
	#make floating point only five decimal places	
		new[i] = '%.5f' %(distribution[i] / x) 
	return new


#the most likely value a random variable is likely to take
def expected_value(order, distribution):
	new = create(len(distribution))
	#create an array with individual terms of ev. then sum them
	for i in range(len(distribution)):
		val = (i**order)
		then = distribution[i]
		new[i] = val*then
	z = the_sum(new)
	return z / float(the_sum(distribution))


#gives probability of obtaining a number <= the one input
def cumulative_function(mass_function):
	new = create(len(mass_function))
	temp = 0.0
	for i in range(len(mass_function)):
		temp = float(temp) + float(mass_function[i])
		new[i] = '%.5f' %(temp)
	return new


#p(i) = (n choose i)*(p^i)*(1-p)^n-i
#p(i) = the probability of having i successes
#and p is the probability of having just 1 success
#this is for events having only two outcomes, success or failure.
def binomial_mass_function(distribution):
	n = len(distribution)


#p(i) = (e^-lambda)[(lambda^i)/(i!)]
#finding a formula for the distribution
def poisson_mass_function(distribution):
	#the e^-lambda is just a constant so ignore for the moment
	#and find later
	n = len(distribution)
	
	#make a table of lambda values for different i's
	#then average them
	#because first case of i = 0 leads to a one
	lambdas = [1]
	#up to 170 or else factorial becomes too long to convert to float
	for i in range(1, 170):
	#distribution[i] is the non normalized probability of i occuring	
		temp = distribution[i] * factorial(i)
		#need float cause computers cant decimal
		the_lambda = temp**(1.0/(float(i)))
		lambdas.append(the_lambda)
	
	minL = minmax(lambdas, 'minimum') 
	maxL = minmax(lambdas, 'maximum')
	averageL = the_average(lambdas)
	print averageL
	print minL
	print maxL
	print lambdas
	


def testing_poisson():
	import analyze_graph as ag
	#import matplotlib as mp

	distribution = ag.main()
	print "This is the first order expected value:"
	one = expected_value(1, distribution)
	print one
	thing = one / float(len(distribution)-1)
	print "as a fraction of the array:", thing
	print ''
	print "This is the second order expected value:"
	two = expected_value(2, distribution)
	print two
	print ''
	print "This is the variance:"
	print (two - one**2.0)**.5
	print ''

	
def Main():
	dist = rand_initial()
	os.system('cls' if os.name == 'nt' else 'clear')

	print "This is the distribution:"	
	print dist
	print ''
	
	print "This is the probability mass function."
	print "It is the probability of each value occuring:"
	z = probabilities(dist)
	print z 
	print ''
	print "This is the first order expected value:"
	one = expected_value(1, dist)
	print one
	thing = one / float(len(dist)-1)
	print "as a fraction of the array:", thing
	print ''
	print "This is the second order expected value:"
	two = expected_value(2, dist)
	print two
	print ''
	print "This is the variance:"
	print (two - one**2.0)**.5
	print ''
	

	print "This is the cumulative probability function:"
	h = cumulative_function(z)
	print h


if __name__ == "__main__":
	testing_poisson()
