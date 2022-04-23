list = [ { "a":1 , "b":2 , "c":3 }, { "d":4 , "e":5 , "f":6 } ]

newlist=[]                       #make an empty list
for i in list:                   # loop to hv a dict in list
    s={}                          # make an empty dict to store new dict data
    for k in i.keys():            # to get keys in the dict of the list
        s[k]=int(i[k])        # change the values from string to int by int func
        newlist.append(s)             # to add the new dict with integer to the list

print(newlist)