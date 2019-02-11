# Query-Expansion
# NITP CSE

In general, query of a user is too short and contains some mistakes. Query expansion is a process of reform these queries for improving the efficiency of textual information retrieval system. In this process, on similarity basis we can add, remove or edit any word in the given query so that we can obtain best search result.


Extraction of top N URLS :
==========================
We are extracting the top N Urls for each query from the most popular search engines i.e Google and Bing
for our case, N is 50 
first of all we fired any query using both the Google and the Bing API
Then with the help Google and Bing search API in  Python programming language we extracted the top 50 links following the above steps
We have excluded the videos links,Advertisements,E-commerce website from our web search 
we saved all the links in folder like structure containing different files in which each file contains the links for each query

*********************************************************************************************************************

TEXT COLLECTION FROM WEB PAGE OF TOP N URLS FROM DIFFERENT SEARCH ENGINE:
========================================================================
After extracting the top 50 Urls from Bing and Google and saving the obtained results in folder like structure containing different files in which each file contains the links for each query,we did the following steps to collect meaningful text from the web pages of the top 50 urls which can be used further for our project.The steps are:
1.for every query we read the links saved earlier in file 
2.for every link we scrapped web using beautifulsoup  module
3.Then for every web page we extracted all the text that appears on that page.
4.While scrapping we have excluded the the content of the tags and the tags itself which are script,title,head,style,meta
5.We have also excluded the pdf,ppt and cgi type links
6.Now the texts which we got after scrapping the web was stored in different files where in for each query one file was created having the same name as that of the query
********************************************************************************************************************

PREPROCESSING OF TEXT CONTENT
=============================
There were major three steps involved in the preprocessing of text content which were...
Step1:NLTK Tagger:
We read the saved text line by line then using nltk tagger we tagged each word into the parts of speech i.e noun,pronoun,verb,etc. as per the English Language rules
Step2:Creation of Phrases:
In this step,we created the phrases according to previously tagged words by considering if two or more verb,noun,adverb comes consecutively then this forms a phrases and saved the so obtained phrases into file
Step3:
Then we counted the frequency of each phrase and words from the file obtained in the step2 and formed a dictionary where the phrases or words were used as the key and the frequency was the value mapped to the key.The so obtained dictionary was sorted in the decreasing order as per the value of each phrase and word and finally saved the dictionary into a file.
Now we have the preprocessed data  for the query optimization
