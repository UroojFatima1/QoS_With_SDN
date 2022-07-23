import matplotlib.pyplot as plt
list1=[]
list2=[]
list3=[]
with open("modifiednoqospings.txt") as file:
    for line in file:
        list1.append(float(line.rstrip()))
with open("pingsmodified5.txt") as file:
    for line in file:
        list2.append(float(line.rstrip()))
for i in range (0,43):
	list3.append(i)
plt.plot(list3,list1,'r--',label="Non-QoS")
plt.plot(list3,list2,'b.',label="QoS")
plt.title('QoS vs Non-QoS results')
plt.xlabel('Sequence number')
plt.ylabel('RTT in ms')
leg=plt.legend(loc="upper center")
plt.savefig('graph2.png')
