from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#import re 

stop_words = set(stopwords.words('english'))

def createDict(query,SE):
    
    file=open("C:\\Users\\DELL\\Desktop\\Project\\Trec\\"+SE+"\\paragraph\\"+query+".txt","r",encoding="utf-8")
    word_dict={}
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
     
    
    #sorting in reverse 
          
    word_dict1=sorted(word_dict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True) 
    
    #print (word_dict)        
    file1=open("C:\\Users\\DELL\\Desktop\\Project\\Trec\\"+SE+"\\word_dict\\"+query+".txt","w",encoding="utf-8")
    for obj in word_dict1:
        file1.write(obj[0]+" "+str(obj[1])+"\n")
    

#createDict("swine flu vaccine","Bing")


file=open("C:\\Users\\DELL\\Desktop\\Project\\query_lists1.txt",'r')
#i=0
while(True):
    query=file.readline()
    if(query==""):
        break
    l=len(query)
    query=query[:l-1]
    
    createDict(query, "Bing")
    #createDict(query, "Duckduckgo")

