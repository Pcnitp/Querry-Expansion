import math

def applyKNN(query):
    fileg=open("C:/Users/DELL/Desktop/Project/Google/score/"+query+".txt",'r',encoding="utf-8-sig")
    fileb=open("C:/Users/DELL/Desktop/Project/Bing/score/"+query+".txt",'r',encoding="utf-8-sig")
    filed=open("C:/Users/DELL/Desktop/Project/DuckDuckGo/score/"+query+".txt",'r',encoding="utf-8-sig")
    filec=open("C:/Users/DELL/Desktop/Project/Combined/score/"+query+".txt",'r',encoding="utf-8-sig")
    
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
        t=(y[0],y[1])
        wordc.append(t)
        
    fileg.close()
    fileb.close()
    filed.close()
    filec.close()
    
    filer=open("C:/Users/DELL/Desktop/Project/Result/"+query+".txt",'w',encoding="utf-8")
    
    for i in range(1):
        j=0
        wordr={}
        for obj in wordc:
            if j==0:
                j+=1
                t1=obj[0]
                print(obj)
                filer.write(obj[0]+" "+str(obj[1])+"\n")
                wordc=wordc[1:]
                continue
            
            try:
                wt1g=wordg[t1]
                wt1b=wordb[t1]
                wt1d=wordd[t1]
                
                ti=obj[0]
                wtig=wordg[ti]
                wtib=wordb[ti]
                wtid=wordd[ti]
                print(wt1g,wt1b,wt1d,wtig,wtib,wtid);
                num=(wt1g*wtig + wt1b*wtib + wt1d*wtid)
                den=math.sqrt((wt1g*wt1g + wt1b*wt1b + wt1d*wt1d)*(wtig*wtig + wtib*wtib + wtid*wtid))
                cs=num/den
                print(num,den,cs)
                wordr[ti]=cs
            except KeyError:
                continue
                
            wordc=sorted(wordr.items(), key = lambda kv:(kv[1], kv[0]),reverse=True) 
    
    for obj in wordc:
        filer.write(obj[0]+" "+str(obj[1])+"\n")

#============================================================================

applyKNN('xyz')

'''
file=open("C:\\Users\\DELL\\Desktop\\Project\\query_lists.txt",'r')
while(True):
    query=file.readline()
    if(query==""):
        break
    l=len(query)
    query=query[:l-1]
    
    applyKNN(query)
    
'''
