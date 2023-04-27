#Reverse Cipher-------------------------------------------

"""
-metoda de criptare simplista ce consta in criptarea mesajului, prin
scrierea acestuia in ordine inversa
-decriptarea mesajului consta in scrierea in ordine inversa a mesajului
criptat"""

#Criptarea unui string------------------------------------

def reverse_enc(message):
    enc_message=""
    k=len(message)-1
    while k>=0:
        enc_message=enc_message+message[k]
        k-=1
    return enc_message
print(reverse_enc("Laborator 3"))

#Decriptarea unui string------------------------------------
def reverse_dec(enc_message):
    message=""
    k=len(enc_message)-1
    while k>=0:
        message=message+enc_message[k]
        k-=1
    return message
print(reverse_dec("3 rotarobaL"))

#Caesar Ciphers ----------------------------------------------

"""
-Ideea de baza este de a transforma fiecare litera din plaintext
prin deplasarea la stânga a poziției literei curente cu trei poziții.
Ex: A devine D, B devine E, C devine F, și așa mai departe.

-Operația de criptare a unei litere m: Enc(m)=(m+3) mod 26.

-Operatia de decriptare:- trebuie să facem deplasarea la stanga cu 3 poziții.
                        -Dec(c)=(c−3) mod 26, c-litera din ciphertext """

#Implementare--------------------------------------------------
"""
-ord('caracter')-reurneaza codul ASCII al caraterului
-chr(cod ASCII)-returneaza caracterul din spatele codului ASCII"""

#Criptarea unei litere-----------------------------------------

alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet2 = "abcdefghijklmnopqrstuvwxyz"
def caesar_enc(letter):
    if (letter<'A' or letter>'Z') and (letter<'a' or letter>'z'):
        print("Caracter invalid")
        return None
    elif letter>='A' and letter<='Z':
        return alphabet1[(ord(letter) - ord('A') + 3) % len(alphabet1)]
    else:
        return alphabet2[(ord(letter) - ord('a') + 3) % len(alphabet2)]
       
print(caesar_enc('a'))   
print(caesar_enc('A'))

#Decriptarea unei litere-----------------------------------------

alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet2 = "abcdefghijklmnopqrstuvwxyz"
def caesar_dec(letter):
    if (letter<'A' or letter>'Z') and (letter<'a' or letter>'z'):
        print("Caracter invalid")
        return
    elif letter>='A' and letter<='Z':
        return alphabet1[(ord(letter) - ord('A') - 3) % len(alphabet1)]
    else:
        return alphabet2[(ord(letter) - ord('a') - 3) % len(alphabet2)]
       
print(caesar_dec('d'))   
print(caesar_dec('D'))

#Criptarea unui string--------------------------------------------

def caesar_enc_string(string):
    cipherstring =''
    for letter in string:
        cipherstring=cipherstring+caesar_enc(letter)
    return cipherstring

print(caesar_enc_string('laborator'))

#Decriptarea unui string--------------------------------------------

def caesar_dec_string(string):
    cipherstring =''
    for letter in string:
        cipherstring=cipherstring+caesar_dec(letter)
    return cipherstring

print(caesar_dec_string('oderudwru'))   


