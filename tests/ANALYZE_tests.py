from nose.tools import *
#change for different projects
import ANALYZE

import document_functions as df
import time
import document_functions as df
import make_a_graph as mag
#test that they do things right and the time taken to run
"""
BASIC FORMAT OF TESTS:

def test_skeleton():
	print "Test: Function"
	print "Description"

	start = time.time()

	result = script.Skeleton
	desired_result = ['what result should be']
	if thing ==  desired_result:
		print "PASS!"
	else:
		print "FAIL!"
		print "Function output was:", thing
		print "Function should be:", desired_result

	time_taken = time.time() - start
	print "Time taken:", time_taken
	print

"""

#finished
def test_remove_newlines():
	print "Test: remove_newlines"
	print "removes \\n characters from the end of matrix elements"

	start = time.time()
	matrix = ['this is\n','incredible\n','is it not\n', '\n']
	desired_result = ['this is','incredible','is it not', '']
	if df.remove_lines(matrix) == desired_result:
		print "PASS!"
	else:
		print "FAIL!"
		print "Function output was:", thing
		print "Function should be:", desired_result

	time_taken = time.time() - start
	print "Time taken:", time_taken

'''
#these require another directory of test .txt files to open
#incomplete
def nicely_format_test():
	print 'Test: nicely_format'
	print 'takes a document and removes non letter characters changes it to lower case'

	start = time.time()
	
	thing = df.nicely_format(some_test_document)
	desired_result = 

	if thing == desired_result:
		print "PASS!"
	else:
		print "FAIL!"
		print "Function outputed:", thing
		print "Function should be:", desired_result

	time_taken = time.time() - start
	print "Time taken:", time_taken


#incomplete
def list_words_test():
	print "Test: Function"
	print "Description"

	start = time.time()
	
	thing = df.list_words(some_test_formatted_document)
	desired_result = 

	if thing == desired_result:
		print "PASS!"
	else:
		print "FAIL!"
		print "Function outputed:", thing
		print "Function should be:", desired_result

	time_taken = time.time() - start
	print "Time taken:", time_taken
'''

#finished
def test_list_frequency():
	print "Test: Function"
	print "Description"

	start = time.time()
	
	#input is list of all words occuring in document in order
	#output of list_words
	word_matrix = ['this', 'is', 'a', 'this', 'a', 'list', 'of', 'no', 'is']
	thing = df.list_frequency(word_matrix)
	desired_result = [['this', 2], ['is', 2], ['a', 2], ['list', 1], ['of', 1], ['no', 1]]
	if thing ==  desired_result:
		print "PASS!"
	else:
		print "FAIL!"
		print "Function outputed:", thing
		print "Function should be:", desired_result

	time_taken = time.time() - start
	print "Time taken:", time_taken


#finished
def test_create():
	print "Test: create"
	print "creates an nxn matrix of zeros given an n"

	start = time.time()
	
	thing = mag.create(3)
	desired_result =[[0,0,0],[0,0,0],[0,0,0]] 
	if thing ==  desired_result:
		print "PASS!"
	else:
		print "FAIL!"
		print "Function outputed:", thing
		print "Function should be:", desired_result
	
	time_taken = time.time() - start
	print "Time taken:", time_taken

def test_number_key():
	print "Test: Function"
	print "Description"

	start = time.time()

	frequency_matrix = [['this', 2], ['is', 2], ['a', 2], ['list', 1], ['of', 1], ['no', 1]]
	result = mag.number_key(frequency_matrix)
	desired_result = {  'this': 0
						'is': 1
						'a': 2
						'list': 3
						'of': 4
						'no': 5
							}
	if thing ==  desired_result:
		print "PASS!"
	else:
		print "FAIL!"
		print "Function output was:", thing
		print "Function should be:", desired_result

	time_taken = time.time() - start
	print "Time taken:", time_taken


def test_create_edge_set():
	print "Test: Function"
	print "Description"

	start = time.time()

	result = script.Skeleton
	desired_result = ['what result should be']
	if thing ==  desired_result:
		print "PASS!"
	else:
		print "FAIL!"
		print "Function output was:", thing
		print "Function should be:", desired_result

	time_taken = time.time() - start
	print "Time taken:", time_taken


def test_create_graph():
	print "Test: create_graph function."
	prnt ""
	start = time.time()
	
	dictionary = {  'this': 0
					'is': 1
					'a': 2
					'list': 3
					'of': 4
					'no': 5
							}


	result = mag.create_graph()
	desired_result = ['what result should be']
	if thing ==  desired_result:
		print "PASS!"
	else:
		print "FAIL!"
		print "Function output was:", thing
		print "Function should be:", desired_result

	time_taken = time.time() - start
	print "Time taken:", time_taken


#finished
def test_change_to_adjacency_list():
	print "Test: change_to_adjacency_list"
	print "changes an adjacency matrix representation of an undirected weighted graph to an adjacency list representation"

	start = time.time()

	matrix = [[0, 2, 1, 0],[2, 0, 4, 1], [1, 4, 0, 3],[0, 1, 3, 0]]
	result = mag.change_to_adjacency_list(matrix)
	desired_result = {  0: [1, 2], [2, 1]
						1: [0, 2], [2, 4], [3, 1]
						2: [0, 1], [1, 4], [3, 3]
						3: [1, 1], [2, 3]
							}
	if thing ==  desired_result:
		print "PASS!"
	else:
		print "FAIL!"
		print "Function output was:", thing
		print "Function should be:", desired_result

	time_taken = time.time() - start
	print "Time taken:", time_taken


#finished
def test_print_adjacency_list_as_words():
	print "Test: print_adjacency_list_as_words"
	print "changes the adjacency list from a number representation to one of words"

	start = time.time()
	graph = {1: [2, 3], 2:[1, 4], 4:[2]}
	frequency = [["what", 2],['is', 7],['it', 8],['huh', 9]]

	result = mag.print_adjacency_list_as_words_test(graph, frequency)
	desired_result = graph = {: [2, 3], 2:[1, 4], 4:[2]}
	if thing ==  desired_result:
		print "PASS!"
	else:
		print "FAIL!"
		print "Function output was:", thing
		print "Function should be:", desired_result

	time_taken = time.time() - start
	print "Time taken:", time_taken
	print
