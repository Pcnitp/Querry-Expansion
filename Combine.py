
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#import re 

stop_words = set(stopwords.words('english'))
word_dict={}

def createDict(query,SE):
    
    file=open("C:\\Users\\DELL\\Desktop\\Project\\"+SE+"\\paragraph\\"+query+".txt","r",encoding="utf-8")
    
    while (True):
        x=file.readline()
        if(x==''):
            break
        
        key=x.split()
        
        for k in key:
            k=k.lower()
            word=word_tokenize(k)
            if word[0] in stop_words or len(word[0])==1:
                continue

            if k in word_dict:
                word_dict[k]+=1
            else:
                word_dict[k]=1
     


file=open("C:\\Users\\DELL\\Desktop\\Project\\query_lists.txt",'r')
#i=0
while(True):
    query=file.readline()
    if(query==""):
        break
    l=len(query)
    query=query[:l-1]
    
    word_dict={}
    createDict(query, "Bing")
    createDict(query, "Duckduckgo")
    createDict(query, "Google")
    
    #sorting in reverse 
          
    word_dict1=sorted(word_dict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True) 
    
    #print (word_dict)        
    file1=open("C:\\Users\\DELL\\Desktop\\Project\\Combined\\word_dict\\"+query+".txt","w",encoding="utf-8")
    for obj in word_dict1:
        file1.write(obj[0]+" "+str(obj[1])+"\n")
    




