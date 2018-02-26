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
		if not f.startswith('.') and os.path.isfile(os.path.join(dir,f)):


			fi = open(dir+f,'r')
			print(f)
			lines = fi.readlines()
			fi.close()
			counter = 0
			li = 1
#Read from line 20 to the next 15556  lines from the data and append it to the features vector
			while li < len(lines):
				try:
					features = []
        				features.append(lines[li].split()[5])
        				features.append(lines[li].split()[7])
        				features.append(lines[li].split()[11])
        				features.append(lines[li].split()[12])
       		 			features.append(lines[li].split()[13])
        				features.append(lines[li].split()[14])
        				features.append(lines[li].split()[26])
       		 			features.append(lines[li].split()[31])
        				features.append(lines[li].split()[32])
					features.append(dict1[dir])
					check.append(features)

					li = li+1 

				except:
					print('error with dir' +str(dir)+ 'and file '+ str(fi))

			print('finished reading ' + f)


feature_array= np.asarray(check)
'''
fwrite = open('features.txt','w')
for c in check:
	fwrite.write(c)
	fwrite.flush()
'''



fwrite = open('features.npy','w')
np.save(fwrite,feature_array)
print(check)




