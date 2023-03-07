import sys
import importlib

HAL=9000
L=[3]
BB = '8'
R2 = ['D','2']
C =[ {'3PO'}]
K={'2SO'}
e=[]
e.extend('E')
WALL=[]
WALL.append(e)
Poppins=set(list('supercalifragilisticexpialidocious'))
Galactica = {'Kara':'Starbuck','Lee':'Apollo','Louanne':'Kat'}
Galactica['Karl']='Helo'
Galactica['Sharon']='Boomer'
Galactica['Marge']='Racetrack'
del Galactica['Louanne']

Germanna_levels=['Freshman','Sophomore']
UMW_levels=['Freshman','Sophomore','Junior','Senior']
MaryWash_levels=UMW_levels
CNU_levels=list(UMW_levels)

def plus2(var):
    return var+2

dat_set={'Pris','Leon','Roy'}
def gimme_dat_set():
    return dat_set

def gimme_set_like_dat():
    like_dat={'Neo','Morpheus','Trinity'}
    return like_dat

def center(string):
    if len(string)==0:
        return None
    else:
        temp=(len(string))//2
        if (len(string)%2)==1:
            return string[temp:temp+1]
        else:
            return string[temp-1:temp+1]

def nuke_last(lst, item):
    lst.reverse()
    lst.remove(item)
    lst.reverse()
    return lst

def middlest(a,b,c):
    lst=[a,b,c]
    lst.sort()
    return (lst[1])

def tack_on_end(lst,data,scale=1):
    if scale==None:
        lst.extend(data)
    else:
        lst.extend(scale*data)

def wondrous_count(num):
    count=0
    while(num!=1):
        count=count+1
        if num%2==0:
            num=num/2
        else:
            num=(3*num)+1
    return count

def unique_vals(dic):
    lst=[]
    st=set()
    for k, v in dic.items():
        lst.append(v)
    st=set(lst)
    return sorted(st)
        
