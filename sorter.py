import os
import re
import subprocess

#list of any extension
lis = []

#list of folder
fol = []

#dictionary to count how many item with different extension
dic = {}

for file in os.listdir():
    #extension checker
    try:
        ext = re.search(r'\.([A-Za-z0-9]*)$',file).group(1).lower()
        if ext not in lis:
            lis.append(ext)
        if ext not in dic:
            dic[ext] = 1
        else:
            dic[ext] += 1
    except:
        fol.append(file)

for e in lis:
    if e not in fol:
        subprocess.call(['mkdir',e], shell=True)
        
for file in os.listdir():
    if file not in fol:
        ext = re.search(r'\.([A-Za-z0-9]*)$',file).group(1).lower()
        subprocess.call(['move',file,ext], shell=True)