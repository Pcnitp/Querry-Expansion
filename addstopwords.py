
x=['could','may','new','would','us','retrieved','also','might','news','even','found','find','said','get','like','one','shall','top','see','two','share','state','isbn','edit','temp','min', 'max', '65535','details', 'original']

def createDict(query,SE):
    file=open("C:/Users/DELL/Desktop/Project/"+SE+"/word_dict/"+query+".txt","r",encoding="utf-8")
    file1=open("C:/Users/DELL/Desktop/Project/"+SE+"/word_dict1/"+query+".txt","w",encoding="utf-8")
    
    while (True):
        key=file.readline()
        if not key:
            break
        
        word=key.split()
        if word[0] in x:
            continue
        else:
            file1.write(key)

    

file=open("C:\\Users\\DELL\\Desktop\\Project\\query_lists.txt",'r')
while(True):
    query=file.readline()
    if(query==""):
        break
    l=len(query)
    query=query[:l-1]
    
    createDict(query, 'Combined')
    createDict(query, 'Google') 
    createDict(query, 'Bing')
    createDict(query, 'DuckDuckGo')




