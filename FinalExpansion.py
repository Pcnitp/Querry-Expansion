filename = "C:/Users/DELL/Desktop/Project/query.txt"
filehandle = open(filename, 'r',encoding="utf-8") 
file1=open("C:/Users/DELL/Desktop/Project/Result/DuckDuckGo_30.txt",'w',encoding="utf-8")
        
queries = [] 
while True:  
    # read a single line
    line = filehandle.readline()
    if not line:
        break
    
    if "<title>" in line:
        start = 7
        end = line.find("</",0,len(line))
        st = line[start:end]
        stm =""
        for i in st:
            if i=="'" or i==",":
                stm=stm+" "
            stm=stm+i
        print(stm)
        #queries.append(stm)
        file1.write("<title>"+stm+", ")
        file=open("C:/Users/DELL/Desktop/Project/DuckDuckGo/score/"+stm+".txt",'r',encoding="utf-8")
        for i in range(35):
            term=file.readline().split()
            file1.write(term[0]+", ")
        file1.write("</title>"+"\n")
        file.close()
    else:
        file1.write(line)
        
file1.close()
filehandle.close()


#print(queries)