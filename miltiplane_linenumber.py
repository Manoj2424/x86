import subprocess
import time

s1 = 'Connectors:'
s2 = 'CRTCs:'
s3 = 'Planes:'
s4 = 'formats:'
s='wlp2s0:'
plane_table=[]

def linenumber(string1):   
	print("finding the line number of " + string1) 
	output1 = subprocess.check_output("cat modetest | grep -n " + s4, shell=True).decode("utf-8")
	table1=output1.split('\n')
	#print(table1)
	for i in table1:
		temp=i.split(':')
		for j in temp:
			if j.isnumeric():
				return j

def plane():
	print("finding the line number of " + s4) 
	output1 = subprocess.check_output("cat modetest | grep -B 1 " + s4, shell=True).decode("utf-8")
	#print(output1)
	table1=output1.split('\n')
	#print(table1)
	length1=len(table1)
	for i in range(0,length1-1,3):
		temp=table1[i].split()
		plane_table.append(temp[0])
		

plane()
print(plane_table)
#print(linenumber(s4))






