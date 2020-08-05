import sys
import getopt

def encrypt(string1,shifting):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !.?'
    result = ""
    for symbol in string1:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translated = (symbolIndex + int(shifting)) % 66
            result += SYMBOLS[translated]
    print(result)

def decrypt(string1,shifting):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !.?'
    result = ""
    for symbol in string1:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translated = (symbolIndex - int(shifting)) % 66
            result += SYMBOLS[translated]
    print(result)

def StartWorking(fungsi,string1,shifting):
    if fungsi == "encrypt":
        encrypt(string1,shifting)
    if fungsi == "Decrypt":
        decrypt(string1,shifting)

fungsi = ""
shifting = 0
hasil = ""

options, _ = getopt.getopt(sys.argv[1:],"D:e:",["Decrypt=","encrypt="])
print(options)
for key, value in options:
    if key == "-D" or key == "--Decrypt":
        fungsi = "Decrypt"
        shifting = value
    if key == "-e" or key == "--encrypt":
        fungsi = "encrypt"
        shifting = value
string1 = input("Masukkan kalimat yang ingin di " + fungsi + ": ")

StartWorking(fungsi,string1,shifting)