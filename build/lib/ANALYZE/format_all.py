import document_functions as df
import os

#find all files in unformatted and reformats them even if they had
#been formatted earlier. maybe check if already formatted 
def main():
	all_files = os.listdir(os.getcwd()+"/docs/Unformatted")
	new = []
	#must remove .txt to make it easier on function
	for element in all_files:
		new.append(element[:-4:])

	for element in new:
		df.nicely_format(element)

if __name__ == "__main__":
	main()
