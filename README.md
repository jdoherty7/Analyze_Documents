# Analyze Documents


# Format Documents

The purpose of this script is to take a document, which will be inputted as a text file, and
copy the document and format it nicely, saving the formatted version in a new folder. The script
will also output the an array of all the words in the formatted document. 

Run this script from the root and run "python ANALYZE/format_all.py" to change your unformatted documents
in docs/Unformatted into formatted documents ready for analysis in docs/Formatted.
You do not need to run this script again until you add more text files. 
Make sure to run all scripts from the root, Analyze_Documents!


# Analysis

Run "python ANALYZE/main.py" to run the program. Currently, it is hard coded to only
analyze "The Last Answer," but this can be simply changed by editing the document you wish
by editing the main.py file.

Furthermore, the visualazation of these analyses is limited at the moment. There is a simple
print function that allows you to view the Edge Matrix in the terminal, but this is unwieldly for
very large (or just not tiny) documents. The graph algorithms implemented include
a simple function to find the degree of each node in the Edge Matrix and the
Floyd–Warshall algorithm to find the least 'costly' path between any two nodes in the Edge matrix.

# Future Work and Tangents

One interesting thing I would like to do would be to seperate chunks of words into different categories
based on how frequently occur, then analyze the graphs of the words in those spectral bands and how those
spectral bands interact with other spectral bands.

This can possibly be done by seperating the distribution you are
given at the end of main.py and then using the graph functions to create an edge set then running
the Floyd-Warshall algorithm on it to see what words are ussually around them.

The important part would be to look for outliers that have statistically shorter paths but occur in a lower
band than we would expect (higher frequency words should have the shortest paths afterall, since they are found
more often in the document and therefore will appear next to more words).

The end goal would be to find some 'fingerprint' of words used to uniquely identify an author
and develop a method to analyze similarities between different 'fingerprints.'

(Some kind of basis set of words would be nice to create too.)
