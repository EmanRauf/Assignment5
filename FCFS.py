
x=input("Enter the no of processes: ")


y=0


sum=0


i=0

b_time=[]


a_time=[]




for y in range (int(x)):
  
	
	i=input("Enter Burst time: ")
  
	
	b_time.append(i)




for y in range (int(x)):
  
	
	i=input("Enter Arrival time: ")
  
	
	a_time.append(i)





f_time=[]


t_time=[]

w_time=[]



for y in range (int(x)):
  
	t_time.append(0)
  
	f_time.append(0)
  
	w_time.append(0)

print("Burst time\t Arrival time\t Waiting time\t Turnaround time")

for y in range (int(x)):
  
	w_time[y]=sum-int(a_time[y])
  
	sum=sum+int(b_time[y])
  
	f_time[y]=sum
  
	t_time[y]=f_time[y]-int(a_time[y])
  
	print(b_time[y],'\t\t',a_time[y],'\t\t',w_time[y],'\t\t',t_time[y],'\n')



sum=0 



sum2=0

for y in range(int(x)):
   
	sum=sum+int(t_time[y])
   
	sum2=sum2+int(w_time[y])



avg=sum/int(x)

avg2=sum2/int(x)


print("Average Turnaround time",avg)

print("Average Waiting time",avg2)






