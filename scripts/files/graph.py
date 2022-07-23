import matplotlib.pyplot as plt
list1=[]
list2=[]

with open("pingsmodified5.txt") as file:
    for line in file:
        list1.append(float(line.rstrip()))
for i in range (0,43):
	list2.append(i)
plt.plot(list2,list1,'g-',label="At 0.5ms")
plt.xticks( range(0,42,2) )
plt.title('Congestion and Re-routing')
plt.xlabel('Sequence number')
plt.ylabel('RTT in ms')
leg=plt.legend(loc="upper center")
plt.savefig('plot3.png')
