#!/bin/bash/python
import os,sys
import f
import copy
info = f.moveInfo()
d = info[0]
d2 = info[1]
master = info[2]

prevRoster = f.getRoster(master[0])
prevNum = f.workNum(master[0])

master2 = []
master2.append(f.comp([],prevRoster))
for x in master[1:]:
    num = f.workNum(x)
    roster = f.getRoster(x)
    master2.append(f.comp(prevRoster,roster))
    prevNum = num
    prevRoster = roster

master3 = []
for x in master[:len(master)-2]:
    master3.append(range(1,f.workNum(x)+1))
if (master[len(master)-2] == 22):
    master3 = master3[:len(master3)-1]


def execute(z,bool,special):
        if (z['lost'] and not z['add']):
            lost = copy.deepcopy(z['lost'])
            if bool:
                loc = special
            else:
                loc = master2.index(z)-1
            for x in master2[:loc+1]:
                if any(item in x['add'] for item in lost):
                    loc2 = master2.index(x)
                    if x['add'] and not x['lost']:
                        if all(item in x['add'] for item in lost) and not bool:
                            for item in z['lost']:
                                var1 = len(master3[loc])
                                place = d2[item].index(master[loc])
                                end = d2[item].index(master[loc2])
                                d2[item][place] = master3[loc][var1-1]
                                master3[loc].remove(master3[loc][var1-1])
                                d2[item] = f.backTrack(place,end,d2[item])
                            z['lost'] = []
                        else:
                            l = []
                            for item in lost:
                                if item in x['add']:
                                    l.append(item)
                            for item in l:
                                z['lost'].remove(item)
                            for item in l:
                                var2 = len(master3[loc2])
                                place = d2[item].index(master[loc2])
                                end = d2[item].index(master[loc])
                                d2[item][place] = master3[loc2][var2-1]
                                master3[loc2].remove(master3[loc2][var2-1])
                                d2[item] = f.forward(place,end,d2[item])
                
                    elif x['add'] and x['lost']:
                        postrep = []
                        prerep = []
                        start = []
                        for item in x['add']:
                            if (item in z['lost']) and x['lost']:
                                postrep.append(item)
                                prerep.append(x['lost'][0])
                                x['lost'] = x['lost'][1:]
                        for item in postrep:
                            x['add'].remove(item)
                        fake = {'add':[],'lost':copy.deepcopy(prerep)}
                        execute(fake,True,loc2-1)
                        for item in prerep:
                            start.append(d2[item][-2])
                        count = 0
                        while count < len(start):
                            if start[count] < master3[loc2-1][-1]:
                                start[count] = start[count] + 1
                            else:
                                start[count] = 1
                            count = count + 1
                        count = 0
                        for item in postrep:
                            d2[item][0] = start[count]
                            d2[item] = f.forward(0,len(d2[item])-2,d2[item])
                            count = count + 1
                        execute(z,False,0)



for z in reversed(master2[1:]):
    execute(z,False,0)


print d2




