import os

path ="/home/technaureus/Desktop/python testing comments" 

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' and '.py' in file:
            files.append(os.path.join(r, file))

for f in files:
 fileHandler=open(f,'r+')
 listOfLines=fileHandler.readlines()
 with open(f,"w") as f:
     for line in listOfLines:
         if not line.strip().startswith('#'):
             f.write(line)



 
 

 
     
 
