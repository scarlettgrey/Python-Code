files = input('Name of the file containing name? ')
listfile = input('Name of the file containing list of string (leave empty if you have no Unique String File)? ')

try:
  appendFile = open(listfile, 'a')
except:
  appendFile = open('Results.txt','w')
UniqueStringName = []

def uniqueStrName(name, length):
    unique = False
    first = 0
    last = 1
    while(not unique):    
        try:
            shortenName = name[first] + name[last]
            if shortenName not in UniqueStringName:
                UniqueStringName.append(shortenName)
                appendFile.write('\n' + shortenName)
                break
            else:
                if last < length - 1:
                    last += 1
                else:
                    first += 1
                    last = first + 1
        except:
            print('This name \'{}\' can\'t generate new Unique String because all of possible unique string that can be created is taken'.format(name))

with open(listfile, 'r') as r:
    lis = r.readlines()
    for l in lis:
        l = l.strip().upper()
        UniqueStringName.append(l)

with open(files, 'r') as f:
    names = f.readlines()
    for name in names:
        name = name.strip().upper()
        uniqueStrName(name, length=len(name))

appendFile.close()
