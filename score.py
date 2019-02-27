import math

def scorer(query, SE):
    f=open("C:/Users/DELL/Desktop/Project/"+SE+"/word_dict1/"+query+".txt","r",encoding="utf-8")
    total=0
    lines=0
    
    while True:
        r=f.readline()
        if(r==''):
            break
        lines+=1
        obj=r.split(' ')
        total+=float(obj[1])
        
    f1=open("C:/Users/DELL/Desktop/Project/"+SE+"/word_dict1/"+query+".txt","r",encoding="utf-8")
    f2=open("C:/Users/DELL/Desktop/Project/"+SE+"/score/"+query+".txt","w",encoding="utf-8")
    
    while True:
        r=f1.readline()
        if(r==''):
            break
        obj=r.split(' ')
        freq=float(obj[1])
        score=(freq/total)*math.log10(lines/freq)
        f2.write(obj[0]+' '+str(score)+'\n')
        
        
 

file=open("C:\\Users\\DELL\\Desktop\\Project\\query_lists.txt",'r')
while(True):
    query=file.readline()
    if(query==""):
        break
    l=len(query)
    query=query[:l-1]
    
    scorer(query, "Combined")

       
