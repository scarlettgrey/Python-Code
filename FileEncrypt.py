def encrypt(string1):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !.?'
    result = ""
    for symbol in string1:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translated = (symbolIndex + 10) % 66
            result += SYMBOLS[translated]
        else:
            result += symbol
    return result


f = open("frankenstein.txt","r") #Buka File txt yang ingin dienkripsi
s = open("frankenstein.encrypted.txt","w") #Membuat file baru(jika tidak ada file yang sama) untuk diedit 

f1 = f.read(1024)

while f1:
    s.write(encrypt(f1))
    f1 = f.read(1024)