import os
import time
#also be cool to see if graphs are isomorphisms
#make function in here to have metric that can later
#be easily used to compare if graphs are isomorphic since
#these functions only run on one graph

'''
important graph functions within:

- fwa(graph) takes a dictionary graph and returns the matrix of shortest
paths between nodes i, j

- find_deg(graph) input is dictionary graph and gives list of degree of all nodes

- edge_matrix(graph) turns dictionary graph into an adjacency matrix

'''
def mirror(matrix):
	#reflecting nxn matrix from upper triangle to fully symmetric
	for i in range(len(matrix)):
		for j in range(i, len(matrix)):
			matrix[j][i] = matrix[i][j]
	return matrix


def nice_print_2(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			print repr(matrix[i][j]).rjust(4),
		print '\n'

def nice_print_3(saysomethingimgivinguponyou, matrix):
	for k in range(len(matrix)):
		os.system("clear")
		print saysomethingimgivinguponyou, k+1
		for i in range(len(matrix)):
			for j in range(len(matrix)):
				print repr(matrix[k][i][j]).rjust(4),
			print '\n'
		time.sleep(1)

def create_zero(l):
	w = []
	for i in range(l):
		w.append([])
		for j in range(l):
			w[i].append(0)
	return w

def create_zero_three(l):
	w = []
	for i in range(l):
		w.append([])
		for j in range(l):
			w[i].append([])
			for x in range(l):
				w[i][j].append(0)
	return w

#find degrees of all vertices
def find_deg(graph):
	degrees = []
	for i in range(len(graph)):
		degrees.append(len(graph.get(i+1)))
	return degrees

def the_minimum(x, y):
	if x > y:
		return y
	else:
		return x

#create a matrix that has all edges as ones and non edges as 0
#mirror function is for a future effort to better these
#run times
def edge_matrix(graph):
	l = len(graph)
	w = create_zero(l)
	for i in range(len(graph)):
		#for j in range(i, len(graph.get(i+1))):
		for j in range(len(graph.get(i+1))):
			w[i][graph.get(i+1)[j]-1] = 1
	#w  = mirror(w)
	return w

#floyd whatever algorithm for calculating shortest paths
def fwa(graph):
	w = []
	edges = edge_matrix(graph)
	
	#initializing the w matrix
	L = len(edges)
	#if there is no path from i to j then weight is infinite
	#but largest path you can have is number of nodes so just
	#make infinite = largest number of nodes + something in case
	for i in range(L):
		for j in range(L):
			if i != j and edges[i][j] == 0:
				edges[i][j] = L + 10
	
	more = create_zero_three(L)
	w.append(edges)
	for i in range(len(more)-1):
		w.append(more[i])
	
	#length of w matrix
	z = len(w)

	#heart of the f whatever algorithm
	#w[k][i][j] is the 'cost' (here all edges are only one so its equal to
	#length of path) from i to j by traversing nodes 1-k.
	for k in range(1, z):
	#switching this i and j seems to do nothing (now and before). dont know 
	#why, maybe because symmetric but I wasnt even getting 
	#a symmetric matrix earlier (i j add switched) and
	#it still did nothing
		for i in range(z):
			for j in range(z):
	#switching the i and j in last addition term fixed the symmetry breaking
	#in the fifth node of my test graph and made it work. who
	#knows why. i know i dont. y travel j to k then k to i, why not i to k
	#then k to j? I would say its because of the order in which you call the
	#is and js but switching their order in for loop changes nothing.
				w[k][i][j] = the_minimum(w[k-1][i][j], w[k-1][j][k]+w[k-1][k][i])
	return w


def main():
	graph = {1: [2, 3, 4, 5],
			 2: [1, 3, 5, 6],
			 3: [1, 2, 4],
			 4: [1, 3, 6],
			 5: [1, 3],
			 6: [2, 4]}
	'''
	nice_print(create_zero_three(3))
	find_deg(graph)
	'''

	nice_print_3("This is the path from i to j, utilizing nodes 1 to", fwa(graph))
	print "Here are the degrees of all the nodes:"
	print find_deg(graph)
	print
	print "This is the adjacency matrix representation of this graph."
	nice_print_2(edge_matrix(graph))


if __name__ == "__main__":
	main()
