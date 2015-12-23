#another try!!! wooohhoooo
import os

def remove_newlines(matrix):
	for i in range(len(matrix)):
		matrix[i] = matrix[i][0:len(matrix[i])-2]
	return matrix

def nicely_format(document_name):
	#take a document and lowercase everything and remove punctuation
	#then resave new document as "original name + FORMATTED" in a new folder

	#string of terms to remove, must be added so as to include ' and "
	terms_to_remove = ',./;[]-"=!@#$%^&*()_' + "'<>?:{}|"
	path = os.getcwd() + "/docs"

	#open document to change and new one to write to in
	#their respective folders
	document = open(path + '/Unformatted/' + document_name + ".txt", 'r')
	new_document = open(path + "/Formatted/" + document_name + "_FORMATTED.txt", 'w')
	
	#create matrix of all the lines then remove new lines at end 
	#before replacing so you dont remove wrong thing with 
	#remove newlines function
	z = document.readlines()
	for i in range(len(z)):
		z[i] = z[i].lower()
	#z = remove_newlines(z)
	
	#take out all that stupid formatting stuff and punctuation
	#as well as if there are extra spaces
	#go through each line in doc and remove each term in string of
	#things wanted out of doc.
	for i in range(len(z)):
		for j in range(len(terms_to_remove)):
			z[i] = z[i].replace(terms_to_remove[j], "")
		z[i] = z[i].replace('  ', '')
	
	#write all the lines to the new document

	new_document.writelines(z)

	document.close()
	new_document.close()


def list_words(formatted_document):
	#this function takes a document and creates an array
	#of all the words in the document in order.	
	list_of_words = []

	z = open(formatted_document)
	L = z.readlines()
	for i in range(len(L)):
		temp = L[i].split()
		for j in range(len(temp)):
			list_of_words.append(temp[j])
	z.close()
	return list_of_words


def list_frequency(word_matrix):
	frequency_array = [[0,0]]

	for i in range(len(word_matrix)):
		word_found = False
		for j in range(len(frequency_array)):
			if word_matrix[i] == frequency_array[j][0]:
				frequency_array[j][1] = frequency_array[j][1] + 1
				j = len(frequency_array) + 30
				word_found = True
		if word_found == False:
			frequency_array.append([word_matrix[i], 1])

	return frequency_array[1:]


