#Shift ciphers----------------------------------------------------

"""
-cifrul lui Cesar folosește o cheie fixată k=3.
-putem generaliza pe mai multe valori ale cheii(adică, în cazul alfabetului englez, putem avea valori de la 0 la 25).
-această modalitate de criptare este numită Shift Cipher.
-criptarea unui mesaj: Enc(m,k)=(m+k) mod 26,
-decriptarea  Dec(c,k)=(c−k) mod 26"""

#Criptarea unei litere-----------------------------------------

alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet2 = "abcdefghijklmnopqrstuvwxyz"
def shift_enc(letter,k):
    if k<0 or k>25:
        print("Cheie invalida")
    else:
        if (letter<'A' or letter>'Z') and (letter<'a' or letter>'z'):
             print("Caracter invalid")
             return None
        elif letter>='A' and letter<='Z':
             return alphabet1[(ord(letter) - ord('A') + k) % len(alphabet1)]
        else:
             return alphabet2[(ord(letter) - ord('a') + k) % len(alphabet2)]
       
print(shift_enc('a',24))   
print(shift_enc('A',5))

#Decriptarea unei litere-----------------------------------------

alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet2 = "abcdefghijklmnopqrstuvwxyz"
def shift_dec(letter,k):
    if k<0 or k>25:
        print("Cheie invalida")
    else:
        if (letter<'A' or letter>'Z') and (letter<'a' or letter>'z'):
              print("Caracter invalid")
              return
        elif letter>='A' and letter<='Z':
              return alphabet1[(ord(letter) - ord('A') - k) % len(alphabet1)]
        else:
              return alphabet2[(ord(letter) - ord('a') - k) % len(alphabet2)]
       
print(shift_dec('d',2))   
print(shift_dec('D',8))

#Criptarea unui string--------------------------------------------

def shift_enc_string(string,k):
    cipherstring =''
    for letter in string:
        cipherstring=cipherstring+shift_enc(letter,k)
    return cipherstring

print(shift_enc_string('Laborator',4))

#Decriptarea unui string--------------------------------------------

def shift_dec_string(string,k):
    cipherstring =''
    for letter in string:
        cipherstring=cipherstring+shift_dec(letter,k)
    return cipherstring

print(shift_dec_string('Pefsvexsv',4))      















