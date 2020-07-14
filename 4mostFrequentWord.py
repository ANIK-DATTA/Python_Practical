fname=input("a.txt") 
count=0 
maxcount=0
l=[]
with open(fname,'r') as f:
	contents=f.read() 
words=content.split()
for i in range(len(words)):
	for j in range(len(words)): 
		if(words[i]==words[j]):
			count+=1
		else:
			count=count

if(count==maxcount):
	l.append(words[i]) 
elif(count>maxcount):
	l.clear() 
l.append(words[i]) 
maxcount=count
print(l)