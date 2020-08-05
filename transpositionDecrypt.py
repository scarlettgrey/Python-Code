import math
message = 'TUB  J LDHIRFUOTAOECOOMVHZG KWXPEEYQ N SR'

key = 5

numOfColumns = int(math.ceil(len(message) / float(key)))
numOfRows = key
numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
maudiunchip = [''] * numOfColumns
column = 0
row = 0

for symbol in message:
    maudiunchip[column] += symbol
    column += 1

    if column == numOfColumns or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
        column=0
        row+=1

ptext = ''.join(maudiunchip)

print(ptext)
