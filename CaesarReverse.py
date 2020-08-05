message = input()
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(SYMBOLS)):
    translated =''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = (symbolIndex -key) % 26
            translated +=SYMBOLS[translatedIndex]
        else:
            translated += symbol
    print('Key #%s: %s' % (key, translated) )