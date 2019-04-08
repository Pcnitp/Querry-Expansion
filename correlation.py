
def score(query):
    fileg=open("C:/Users/DELL/Desktop/Project/Google/weight/"+query+".txt",'r',encoding="utf-8-sig")
    fileb=open("C:/Users/DELL/Desktop/Project/Bing/weight/"+query+".txt",'r',encoding="utf-8-sig")
    filed=open("C:/Users/DELL/Desktop/Project/DuckDuckGo/weight/"+query+".txt",'r',encoding="utf-8-sig")
    filec=open("C:/Users/DELL/Desktop/Project/Combined/weight/"+query+".txt",'r',encoding="utf-8-sig")
    
    wordg={}
    wordb={}
    wordd={}
    wordc=[]
    
    while True:
        x=fileg.readline()
        if(x==''):
            break
        y=x.split()
        wordg[y[0]]=float(y[1])
    
    while True:
        x=fileb.readline()
        if(x==''):
            break
        y=x.split()
        wordb[y[0]]=float(y[1])
    
    while True:
        x=filed.readline()
        if(x==''):
            break
        y=x.split()
        wordd[y[0]]=float(y[1])
        
    while True:
        x=filec.readline()
        if(x==''):
            break
        y=x.split()
        #t=(y[0],y[1])
        wordc.append(y[0])
        
    fileg.close()
    fileb.close()
    filed.close()
    filec.close()
    
    filer=open("C:/Users/DELL/Desktop/Project/Correlation/"+query+".txt",'w',encoding="utf-8")
    
    wordr={}
    q=query.split()
    for t in wordc:
        try:
            val=0.0
            for p in q:
                p=p.lower()
                val+=wordg[p]*wordg[t] + wordg[p]*wordb[t] + wordd[p]*wordd[t]
            val=1000*val/len(q)
            wordr[t]=val
            
        except:
            continue
        
    wordx=sorted(wordr.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
    for x in wordx:
        filer.write(x[0]+" "+str(x[1])+"\n")

#============================================================================

score('Swine flu vaccine')

'''
file=open("C:\\Users\\DELL\\Desktop\\Project\\query_lists.txt",'r')
while(True):
    query=file.readline()
    if(query==""):
        break
    l=len(query)
    query=query[:l-1]
    
    score(query)
 '''   

