from collections import namedtuple, deque, ChainMap,Counter,OrderedDict, defaultdict
"""
courses = namedtuple('course',['name','tech'])
print(courses)
clist = courses(name='Data Science', tech='Python')
print(clist)
print(getattr(clist,"tech"))
print(clist.name)
print(clist[0])
courselist = ['Web Development','Angular','HTML']
print(courses._make(courselist)) #convert the list into the namedtuple
"""

#Deque - It is an optimized list to perform insertion and deletion easily
"""
t_list = ["Hardik","Rohit","Rishabh","Rahul","Rinku"]
tqueue = deque(t_list)
print("original" ,tqueue)
tqueue.appendleft("Virat")
print("changed" ,tqueue)
tqueue.popleft()
print("after pop" ,tqueue)
"""

#ChainMap - It is dictionary like class which is able to make a single view
"""
tmodule_1 = {1:'Angular',2:'Python'}
tmodule_2 = {3:'React',4:'Cloud Computing', 5:'DevOps'}
mlist = ChainMap(tmodule_1,tmodule_2)
print(mlist)
tmodule_3 = {6:'Pyspark',7:'Scala'}
umlist = mlist.new_child(tmodule_3)
print(umlist)
print(umlist.maps)
print("*",60)
print(list(umlist.keys()))
print("*",60)
print(list(umlist.values()))
"""

#Counter - It is a dictionary subclass which is used to count hashtable objects
"""
Rohit_scores = [70,89,270,100,100,70,50, 60,200,89]
score_count = Counter(Rohit_scores)
print(score_count)

print(score_count.keys())
print(score_count.values())
print(score_count.items())
"""
"""
tempod = defaultdict(int)
tempod[1] ="Python"
tempod[2] = "Pyspark"
#tempod = {}
print(tempod)
print(tempod[3])
"""

"""
clistod = OrderedDict();
clistod["python"]=100
clistod["html"]=102
clistod["css"]=103
clistod["bootsrap"]=104

for key,value in clistod.items():
    print(key,value)


clistod["css"]=105
for key,value in clistod.items():
    print(key,value)


clistod_1 = OrderedDict();

clistod_1["html"]=102
clistod_1["css"]=103
clistod_1["bootsrap"]=104
clistod_1["python"]=100

print(clistod_1 == clistod)

"""