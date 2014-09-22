#!/bin/bash/python
    
def moveInfo():
    import work
    info = work.getInfo()
    global d
    d = info[0]
    return info

def workNum(time):
    num = 0
    for item in d.values():
        if time in item:
            num = num + 1
    return num

def isWorking(time, key):
    if not time in d[key]:
        return False
    elif (d[key].index(time) >= 0):
        return True
    return False

def getRoster(time):
    roster = []
    for item in d.keys():
        if isWorking(time,item):
            roster.append(item)
    return roster
            
def comp(list1, list2):
    change = {'add': [], 'lost': []}
    if not list1:
        for x in list2:
            change['add'].append(x)
    else:
        for x in list1:
            if not x in list2:
                change['lost'].append(x)
        for x in list2:
            if not x in list1:
                change['add'].append(x)
    return change

def backTrack(loc, stop, list):
    while (loc > stop):
        if (list[loc] > 1):
            list[loc-1] = list[loc] - 1
        else:
            list[loc-1] = workNum(list[loc-1]+0.5)
        loc = loc - 1
    return list

def forward(loc, stop, list):
    while (loc < stop) and not (list[loc+1] == 0):
        if (list[loc] < workNum(list[loc+1]-0.5)):
            list[loc+1] = list[loc] + 1
        else:
            list[loc+1] = 1
        loc = loc + 1
    return list


    






        


