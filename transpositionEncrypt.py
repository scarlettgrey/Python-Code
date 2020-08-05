message = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
encryp1 = 'TUB J  LDHIRFUOTAOECOOMVHZG KWXPEEYQ N SR'
encryp2 = 'TUB J  LDHIRFUOTAOECOOMVHZG KWXPEEYQ N SR'
key1 = [1,2,3,4,5,6,7,8,9,10]

for key in key1:
    maudichip=[''] * key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            maudichip[column] += message[currentIndex]
            currentIndex += key
    hasilchip =  ''.join(maudichip)
    print(hasilchip)
    if hasilchip == encryp1:
        print(str(key) + ':' + hasilchip)

