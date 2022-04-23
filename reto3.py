def senalSatelite(t1:tuple,t2:tuple):
    l1=len(t1)
    l2=len(t2)
    control=True
    long=l1-1
    
    obj1=list(t1)
    obj2=list(t2)
    obj3=list(t1)
    obj4=list(t2)
    obj5=list(t1)
    obj6=list(t1)
    lst = list(t1)  
            
    if l1==l2:
        
        for x in range(0,long+1):
            comp=t1[x]
            if comp > 1:
               
                response="Señal corrupta"
                control=False

        for x in range(0,long+1):
            comp=t2[x]
            if comp > 1:
              
                response="Señal corrupta"
                control=False
        
    else:
        response="Señal corrupta"
        control=False

    if control==True:
        if l1 >= 2:
           
            obj1.insert(0, 0)
            obj1.append(0)
            

            obj2.insert(0, 0)
            obj2.append(0)
           

            obj3.insert(0, 0)
            obj3.append(0)

            obj4.insert(0, 0)
            obj4.append(0)

           

            for x in range(1,long+2):
               
                if obj1[x-1]==obj1[x+1]:
                           
                    obj3[x] = 0
                
                if obj1[x-1]!=obj1[x+1]:
                    
                    obj3[x] = 1
            for x in range(1,long+1):
               
                if obj2[x-1]==obj2[x+1]:
                           
                    obj4[x] = 0
                
                if obj2[x-1]!=obj2[x+1]:
                    
                    obj4[x] = 1      
            
            
            obj3.pop(0)
            obj4.pop(0)
           
            obj3.pop(long+1)
            obj4.pop(long+1)
            
            for x in range(0,l1//2):
               
                if obj3[2*x]==obj4[2*x]:
                    obj5[2*x] = 1
                if obj3[2*x]!=obj4[2*x]:
                    obj5[2*x] = 0

                
                if obj3[2*x+1]==obj4[2*x+1]:
                    obj5[2*x+1] = 0 
                if obj3[2*x+1]!=obj4[2*x+1]:
                    obj5[2*x+1] = 1 
                
            for x in range(0,long+1):
                
               
                if obj5[x] == 1:
                    obj6[x] = 0
                    
                    

                if obj5[x] == 0:
                    obj6[x] = 1
                    

            




            response=tuple(obj6)
                       


                        
                        
           
    
        else:
            response="Señal corrupta"

    
    return response

t1=(1,0,1)
t2=(0,0,1)

print(senalSatelite(t1,t2))




