from nose.tools import *

import ANALYZE
from ANALYZE import document_functions as df
from ANALYZE import document_functions as df
from ANALYZE import make_a_graph as mag


#test that they do things right and the time taken to run
"""
BASIC FORMAT OF TESTS:

def test_skeleton():
	print "Test: Function"
	print "Description"

	start = time.time()

	result = script.Skeleton
	desired_result = ['what result should be']
	assert_equal(result, desired_result)

	time_taken = time.time() - start
	print "Time taken:", time_taken

"""

#finished
def test_remove_newlines():
	print "Test: remove_newlines"
	print "removes \\n characters from the end of matrix elements"

	matrix = ['this is\\n','incredible\\n','is it not\\n', '\\n']
	desired_result = ['this is','incredible','is it not', '']
	thing = df.remove_newlines(matrix)
	assert_equal(thing, desired_result)


'''
#these require another directory of test .txt files to open
#incomplete
def nicely_format_test():
	print 'Test: nicely_format'
	print 'takes a document and removes non letter characters changes it to lower case'

	thing = df.nicely_format(some_test_document)
	desired_result = 

	assert_equal(thing, desired_result)


#incomplete
def list_words_test():
	print "Test: Function"
	print "Description"

	
	thing = df.list_words(some_test_formatted_document)
	desired_result = 

	assert_equal(thing, desired_result)
	
'''

#finished
def test_list_frequency():
	print "Test: Function"
	print "Description"

	#input is list of all words occuring in document in order
	#output of list_words
	word_matrix = ['this', 'is', 'a', 'this', 'a', 'list', 'of', 'no', 'is']
	thing = df.list_frequency(word_matrix)
	desired_result = [['this', 2], ['is', 2], ['a', 2], ['list', 1], ['of', 1], ['no', 1]]
	
	assert_equal(thing, desired_result)


#finished
def test_create():
	print "Test: create"
	print "creates an nxn matrix of zeros given an n"
	
	thing = mag.create(3)
	desired_result =[[0,0,0],[0,0,0],[0,0,0]] 



def test_number_key():
	print "Test: number key"
	print "show the number in frequency graph that the"
	print "word is represented by"


	frequency_matrix = [['this', 2], ['is', 2], ['a', 2], ['list', 1], ['of', 1], ['no', 1]]
	result = mag.number_key(frequency_matrix)
	desired_result = {  'this': 0,
						'is': 1,
						'a': 2,
						'list': 3,
						'of': 4,
						'no': 5
							}
	assert_equal(result, desired_result)

'''
#not finished
def test_create_edge_set():
	print "Test: create_edge_set"
	print ""

	result = script.Skeleton
	desired_result = ['what result should be']
	assert_equal(thing, desired_result)
	

def test_create_graph():
	print "Test: create_graph function."
	print ""

	dictionary = {  'this': 0,
					'is': 1,
					'a': 2,
					'list': 3,
					'of': 4,
					'no': 5
							}


	result = mag.create_graph()
	desired_result = ['what result should be']
	assert_equal(thing, desired_result)

'''

#finished
def test_change_to_adjacency_list():
	print "Test: change_to_adjacency_list"
	print "changes an adjacency matrix representation of an"
	print "undirected weighted graph to an adjacency list representation"

	matrix = [[0, 2, 1, 0],[2, 0, 4, 1], [1, 4, 0, 3],[0, 1, 3, 0]]
	result = mag.change_to_adjacency_list(matrix)
	desired_result = {  0: [[1, 2], [2, 1]],
						1: [[0, 2], [2, 4], [3, 1]],
						2: [[0, 1], [1, 4], [3, 3]],
						3: [[1, 1], [2, 3]]
							}
	assert_equal(result, desired_result)


#finished
def test_make_adjacency_list_into_words():
	print "Test: print_adjacency_list_as_words"
	print "changes the adjacency list from a number" 
	print "representation to one of words"

	graph = {0: [1, 2], 1:[0, 3], 3:[1]}
	frequency = [["what", 2],['is', 7],['it', 8],['huh', 9]]

	result = mag.make_adjacency_list_into_words(graph, frequency)
	desired_result = {"what": ['is', 'it'], 
					  "is":   ['what', 'huh'],
					  "huh":  ['is']}
	assert_equal(result, desired_result)

