MP2
==========

MP2 for Visualizing Literature.

The purpose of this project was to create a hierarchical representation of data from the novel Dracula.  
I chose to expand further on the word frequency concept used in MP1 (I apologize for not having that one up
on here, but I didn't understand how Github worked at the time).  

I originally tried to carry out my plan with the entire novel, but because of the task I was tackling
I shortened my text to just the first chapter.  The root of the data is the most frequent word in the entire
text.  Its children are the most frequent words in each paragraph (excluding stopwords and non-alphabetic
strings), and the children of each of those are the most frequent words in each sentence.

I occasionally had to make an exception for the most frequent word in each sentence, because oftentimes there was no 'most frequent word'.  If that was the case, then I simply chose the first word in the sentence.  Details on how all of this was implemented can be found in drac_tree.py (I've commented several parts of the code, explaining exactly what's taking place).

The final product can be found here: http://web.engr.illinois.edu/~spratle2/

I used a zoomable circle packing layout.  I've changed several things, such as the colors used.  I've also made the size uniform for all the leaf nodes (there was no associated data I could use for the size, as is seen in the famous "flare.json" example).  

One note that should be made: I no longer use index.js for my javascript, instead inserting it directly into the file.  For whatever reason, nothing appears on the page if I place the javascript code in a function and then run the function.

Creation of visualization is in progress as of 11/13/2014 (which is very, very late, and I apologize for that).  The visualization has been finalized as of 11/18/2014.
