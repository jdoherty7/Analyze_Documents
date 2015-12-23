import make_a_graph as mg
import graph_functions as gf


def main():
	thing = mg.create_graph_from_formatted_document("the_last_answer_FORMATTED.txt")

	dictionary = thing[2]
	frequency = thing[1]
	graph_matrix = thing[0]

	#gf.nice_print_2(graph_matrix)
	#flayshall = gf.fwa(graph_matrix):
	#gf.nice_print_2(graph)


	#dic = mg.change_to_adjacency_list(graph_matrix, None)

	#mg.print_adjacency_list_as_words(dic, frequency)
	"""
	print len(frequency), "unique words"
	print "TOP TEN:"
	for i in range(10):
		print frequency[i]
	"""
	distribution = []
	for i in range(len(frequency)):
	#add if statement here if you want to limit frequency values
		#if frequency[i][1] > 1:
		distribution.append(frequency[i][1])

	return distribution



if __name__ == "__main__":
	main() 
