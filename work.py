#!/bin/bash/python
import copy

def getInfo():
#get everybody's shifts
    my_in = input('# of people working: ')
    d = {raw_input('enter name: '): (input('start: '), input('finish: ')) for x in range(0, my_in)}

    max = 8
    min = 22

#get open and close of work day
    for item in d.values():
        for part in item:
            if(part > max):
                max = part
            if(part < min):
                min = part

#get master list of rotation increments
    master = []
    for x in range(min,max+1):
        master.append(x)
        master.append(x+0.5)

#expand individual shifts within d
    i = 0
    for item in d.values():
        tmp = [item[0]]
        while(tmp[-1] < item[1]):
            tmp.append(tmp[-1]+0.5)
        d[d.keys()[i]] = tmp
        i = i + 1

#format
    for item in d.keys():
        if (d[item][-1] == 22.0):
            d[item][-1] = 0
            d[item][-2] = 0
        else:
            d[item][-1] = 0
    
    d2 = copy.deepcopy(d)
    return [d,d2,master]

if __name__ == '__main__':
    getInfo()



        
                
                
    
    
        

    



    
    
    


















	
	
	

	
	
	