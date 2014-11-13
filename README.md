vizlit_mp2
==========

MP2 for Visualizing Literature.

The purpose of this project was to create a hierarchical representation of data from the novel Dracula.  
I chose to expand further on the word frequency concept used in MP1 (I apologize for not having that one up
on here, but I didn't understand how Github worked at the time).  

I originally tried to carry out my plan with the entire novel, but because of the task I was tackling
I shortened my text to just the first chapter.  The root of the data is the most frequent word in the entire
text.  Its children are the most frequent words in each paragraph (excluding stopwords and non-alphabetic
strings), and the children of each of those are the most frequent words in each sentence.

I had to make an exception for the most frequent word in each sentence, because more often than not there was
not a most frequent word, so I instead usually ended up choosing the first word from each sentence.  I may go 
back later on and choose a random word from each sentence, because the words are organized alphabetically and there
are a few too many b and c words.  It gets boring after a while.

Creation of visualization is in progress as of 11/13/2014 (which is very, very late, and I apologize for that).
