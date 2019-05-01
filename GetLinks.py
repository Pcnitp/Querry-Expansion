def googleSearch(query):
    print(query)
    from googlesearch import search 
    
    file=open("C:/Users/DELL/Desktop/Project/Trec/Google/"+query+".txt",'w')
    for j in search(query, tld="co.in", num=50, start=0,stop=None, pause=2): 
        print(j)
        file.write(j+"/n")
    file.close()
        
#==========================================================
        
def bingSearch(search_term, i):

    subscription_key = '96de0fef4a994eb1945bcd7eb9e00626'
    assert subscription_key
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
    #search_term = "swine flu"
    
    import requests
    
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML","count":"50"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    #print(response)
    #print(search_results)
    #name=search_term+".txt"
    l=len(search_term)
    name=search_term[:l-1]+".txt"
    #print(name)
    file=open("C:/Users/DELL/Desktop/Project/Trec/Bing/QueryLinks/"+name,'w')
    for v in search_results["webPages"]["value"]:
        #print(v["url"])
        #print(" ")
        file.write(v["url"]+"\n")
    file.close();
        
#bingSearch("swine flu vaccine",0)
#i=0
file= open("C:\\Users\\DELL\\Desktop\\Project\\query_lists1.txt", 'r')
while True:
    s=file.readline()
    if(s==""):
        break
    l=len(s)
    #i=i+1
    s=s[:l-1]
    googleSearch(s)
    #print(i)   
    
file.close()
#========================================================================
'''      
def yahooSearch():
    
    import simplejson, urllib
    APP_ID = '5A1rZg48' # Change this to your API key
    SEARCH_BASE = 'http://search.yahooapis.com/ WebSearchService/V1/webSearch'
    
    class YahooSearchError(Exception):
        pass
    
    def search(query, results=20, start=1, **kwargs):
        kwargs.update({
            'appid': APP_ID,
            'query': query,
            'results': results,
            'start': start,
            'output': 'json'
        })
        url = SEARCH_BASE + '?' + urllib.parse.urlencode(kwargs)
        print(url)
        result = simplejson.load(urllib.request.urlopen(url))
        if 'Error' in result:
            # An error occurred; raise an exception
            raise YahooSearchError, result['Error']
        return result['ResultSet']
    
    info = search('swine flu vaccine')
    results = info['Result']
    for result in results:
        print(result['Url'])
'''  
#==========================================================================

