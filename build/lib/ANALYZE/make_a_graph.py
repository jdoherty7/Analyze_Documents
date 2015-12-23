#graphing the words 
import document_functions as df

#turn the list of all words into a graph


#has test
#create a 2d square array of all zeros
def create(n):
	new = []
	for i in range(n):
		new.append([])
		for j in range(n):
			new[i].append(0)
	return new


#has test
def number_key(frequency):
	key_dictionary = {}
	for i in range(len(frequency)):
		key_dictionary[frequency[i][0]] = i
	#so then you can do key.get(word) to get number of the node it should be
	return key_dictionary

#no test
#delete all edges whos weight is at or below this threshold
#in range because if too low then it is just noise from adding
#a lot of things, if too high then that means it is just
#noise from high frequency words (not because relational)

#this range should probably change depending on how frequently a word
#occurs in the graph
def keep_within_range(matrix, bottom, top):
	#given a graph that is represented as a matrix this will delete
	#edges that are below a certain threshold
	size = len(matrix)
	for i in range(size):
		for j in range(size):
			if matrix[i][j] <= bottom or matrix[i][j] >= top:
				matrix[i][j] = 0
	return matrix


#has test
def create_edge_set(dic, list_of_words):
	#given a list of words as they appear in the document 
	#(repeated) create an edge set of the list of words 
	#represented as the number they appear
	edges = []
	average_sentence_length = 10
	for i in range(len(list_of_words)-average_sentence_length):
	#create an edge between words if they appear next to each other
	#in a document (experiment with speed and importance by changing this)
		'''
		IMPORTANT

		THIS WILL CREATE EDGES BETWEEN WORDS THAT ARE WITHIN A CERTAIN 
		DISTANCE OF EACH OTHER. TEST WHAT DISTANCE CREATES MEANINGFUL 
		GRAPHS AND WHAT THRESHOLD YOU SHOULD KEEP EDGES UP TILL.

		this is likely to vary with the size of your document 
		and other parameters like average sentence length.

		Maybe automate this to use the average sentence length of a document?
		find the length between periods, add lengths then divide by number of
		"sentences", things like etc. shouldnt affect it too much as this is
		an average, especially for large documents.

		'''
		for j in range(average_sentence_length):
			y = j + 1
			#y ranges from 1 to average_sentence_length
			#so it will add the next node up to asl nodes away
			edges.append([dic.get(list_of_words[i]), dic.get(list_of_words[i+y])])  

	return edges


#Has test
def create_graph(dictionary, edge_set):
	#vertices should be the list_frequency() function [i][0] element.
	#because this is the list of all words in the document (non-repeated)
	#use key_dictionary to change the words into their number form

	#vertices is basically the same as dictionary except you input 
	#the number it is and get the word. dictionary you input the word 
	#with .get(word) and you get what number it is. which im guessing 
	#is faster but might change it basically the frequency array 
	#is all you need though
	
	#make create zero function somewhere
	graph = create(len(dictionary))
	for i in range(len(edge_set)):
	#you have to add an edge at both i, j and j, i so as to keep the symmetry
	#of the matrix, because it should be symmetric and if you only have
	#it added to i, j then if you have 3,4 then 4, 3 comes up later it will
	#be added somewhere else.

		graph[edge_set[i][1]][edge_set[i][0]] += 1
		graph[edge_set[i][0]][edge_set[i][1]] += 1
		
	graph = keep_within_range(graph, 3, 7)	

	return graph
		

#creates and adjacency matrix graph of document
def create_graph_from_formatted_document(formatted_document):
	#create list of words from document then use that list to 
	#create frequency spectrum. take that frequency 
	#spectrum and graph it
	list_of_words = df.list_words(formatted_document)
	frequency_matrix = df.list_frequency(list_of_words)
	dictionary = number_key(frequency_matrix)
	edge_set = create_edge_set(dictionary, list_of_words)
	graph_of_document = create_graph(dictionary, edge_set)

	#because graph is all numbers and to get what word that is you have
	#to put that number into the frequency matrix frequency[i][0]
	return (graph_of_document, frequency_matrix, dictionary)


#has test
#change an adjacency matrix that has weights into an
#adjacency list that contains those weights
#if None then list graph as numbers, if given list graph as words
def change_to_adjacency_list(matrix, frequency=None):
	if frequency == None:	
		graph = {}
		for i in range(len(matrix)):
			for j in range(len(matrix)):
				if matrix[i][j] != 0:
					#add the node adjacent and the weight of path between them
					#make matrix added or else you overwrite previously added
					if i in graph.keys():
						graph[i].append([j, matrix[i][j]])
					else:
						graph[i] = [[j, matrix[i][j]]]
	else:	
		graph = {}
		for i in range(len(matrix)):
			for j in range(len(matrix)):
				if matrix[i][j] != 0:
					#add the node adjacent and the weight of path between them
					if frequency[i][0] in graph.keys():
						graph[frequency[i][0]].append([frequency[j][0], matrix[i][j]])
					else:
						graph[frequency[i][0]] = [[frequency[j][0], matrix[i][j]]]
	return graph

#no test
#given a graph and frequency matrix this should change the graph
#made of numbers to the words they represent
def print_adjacency_list_as_words(graph, frequency):
	for thing in graph.keys():
		array = graph[thing]
		for element in array:
			element[0] = frequency[element[0]][0]
		print frequency[thing][0], array





