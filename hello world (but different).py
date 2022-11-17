import time
def c(string):
    list1 = []
    list1[:0] = string
    return list1

def f():
    s='hello world'
    s=c(s)
    i='abcdefghijklmnopqrstuvwxyz'
    i=c(i)
    n=['a','a','a','a','a',' ','a','a','a','a','a',]
    g=''
    
    for k in range(len(s)):
        if s[k]==' ':
            continue
        for j in i:
            if n[k]!=s[k]:
                n[k]=j
                print(g.join(n[0:k+1]))
                time.sleep(0.1)
                
f()


            
        
