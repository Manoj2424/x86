import subprocess
from subprocess import Popen, PIPE

import time

s1 = 'Connectors:'
s2 = 'CRTCs:'
s3 = 'Planes:'
s4 = 'formats:'
table=[]

def getpara(string1):   
	print("finding id value of " + string1) 
	output = subprocess.check_output("modetest | grep -A 2 " + string1, shell=True)
	temp = output.decode("utf-8")
	table1=temp.split()
	#print(table)
	for i in table1:
		a=i.isnumeric()
		if a==True:
			print(string1)
			print(i)
			return i

def getformat(string1):
	global table
	print("finding Formats available ") 
	output = subprocess.check_output("modetest | grep -m 1 " + string1, shell=True)
	temp = output.decode("utf-8")
	print(temp)
	table=temp.split()
	print(table)
	table.pop(0)

def validate_mode():
	global table
	a=len(table)
	for i in range(a):
		print("testing for cmd: only Mode :")
		print("modetest -s " + conn_id + "@" + encod_id + ":640x480@" + table[i])
		output = subprocess.Popen("modetest -s " + conn_id + "@" + encod_id + ":640x480@" + table[i], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)		
		print("checkig output......")
		time.sleep(5)
		output.terminate()	
		print("terminated")	
		print("\n")


def validate_mode_plane():
	global table
	a=len(table)
	for i in range(a):
		for j in range(a):
			print("testing for cmd: Mode + plane :")
			print("modetest -s " + conn_id + "@" + encod_id + ":640x480@" + table[i] + " -P " + "38@" + encod_id + ":200x200@" + table[j])
			output = subprocess.Popen("modetest -s " + conn_id + "@" + encod_id + ":640x480@" + table[i] + " -P " + "38@" + encod_id + ":200x200@" + table[j], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)		
			print("checkig output......")
			time.sleep(5)
			output.terminate()	
			print("terminated")	
			print("\n")


conn_id = getpara(s1)	

encod_id = getpara(s2)

plane_id = getpara(s3)

getformat(s4)

validate_mode()

validate_mode_plane()































