def convertOpposite(broken): 
    
    
    broken = list(broken)
    
    val = len(broken)
        
    for i in range(val): 
        if broken[i] >= 'a' and broken[i] <= 'z': 
  
            
            broken[i] = chr(ord(broken[i]) - 32) 
  
        elif broken[i] >= 'A' and broken[i] <= 'Z': 
  
            
            broken[i] = chr(ord(broken[i]) + 32) 
            
    broken = "".join(broken)
    print(broken)        

if __name__ == "__main__": 
    
    bool = "aWESOME is cODING"
    
    broken = list(bool)
    
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q = broken
    
    broken = l,m,n,o,p,q,k,i,j,h,a,b,c,d,e,f,g
    
    broken = "".join(broken)
    
    red = convertOpposite(broken) 
    
