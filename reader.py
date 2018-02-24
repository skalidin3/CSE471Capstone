import os
import sys
import numpy as np


dirs = ['Capstone_Results/Expday_D/','Capstone_Results/Expday_ND/','Capstone_Results/Expfog_D/','Capstone_Results/Expfog_ND/','Capstone_Results/Expfognight_D/','Capstone_Results/Expfognight_ND/','Capstone_Results/Expnight_D/','Capstone_Results/Expnight_ND/']

dict1 = {'Capstone_Results/Expday_D/':0,'Capstone_Results/Expday_ND/':1,'Capstone_Results/Expfog_D/':2,'Capstone_Results/Expfog_ND/':3,'Capstone_Results/Expfognight_D/':4,'Capstone_Results/Expfognight_ND/':5,'Capstone_Results/Expnight_D/':6,'Capstone_Results/Expnight_ND/':7}

check = []
labels = []
for dir in dirs:
	files = os.listdir(dir)
	for f in files:	
		print(f)
		fi = open(dir+f,'r')
		lines = fi.readlines()
		fi.close()
		counter = 0
		features = []
		li = 20
#Read from line 20 to the next 15556  lines from the data and append it to the features vector
		while counter != 15556:
			try:
        			features.append(lines[li].split()[5])
        			features.append(lines[li].split()[7])
        			features.append(lines[li].split()[11])
        			features.append(lines[li].split()[12])
        			features.append(lines[li].split()[13])
        			features.append(lines[li].split()[14])
        			features.append(lines[li].split()[26])
        			features.append(lines[li].split()[31])
        			features.append(lines[li].split()[32])
        			li = li+1
				counter = counter +1
			except:
				print('error with dir' +str(dir)+ 'and file '+ str(fi))
		check.append(features)
		labels.append(dict1[dir])


feature_array= np.asarray(check)
'''
fwrite = open('features.txt','w')
for c in check:
	fwrite.write(c)
	fwrite.flush()
'''
print(len(check))
print(feature_array)
print(len(labels))
print(labels)

