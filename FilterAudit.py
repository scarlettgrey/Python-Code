f = open("D:/Coding/Python/audit(netadmin).log","r")
syscall = open("D:/Desktop/Uts/syscall.txt","w")
execvee = open("D:/Desktop/Uts/execve.txt","w")
pathh = open("D:/Desktop/Uts/path.txt","w")
proctitle = open("D:/Desktop/Uts/proctitle.txt","w")
elsee = open("D:/Desktop/Uts/else.txt","w")

for a in range(2010):
    str1 = f.readline()
    if 'type=SYSCALL' in str1:
        syscall.write(str(a+1) + ": " +str1)
    elif 'type=EXECVE' in str1:
        execvee.write(str(a+1) + ": " +str1)
    elif 'type=PATH' in str1:
        pathh.write(str(a+1) + ": " +str1)
    elif 'type=PROCTITLE' in str1:
        proctitle.write(str(a+1) + ": " +str1)
    else:
        elsee.writelines(str(a+1) + ": " +str1)

#audit = open("D:/Desktop/Uts/AduitSpaced.txt","w")
#for a in range(2010):
#    str1 = f.readline()
#    if 'type=SYSCALL' in str1:
#        audit.writelines("--------------------------------\n")
#        audit.writelines(str(a+1) + ": " + str1)
#    else :
#        audit.writelines(str(a+1) + ": " + str1)

print("Filtering Done...")
print("Exiting...")