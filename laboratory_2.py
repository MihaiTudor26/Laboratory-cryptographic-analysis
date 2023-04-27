#|-----------------------------ENCODING VS ENCRYPTION--------------------------------------------------

#1.ENCODING

"""
Encoding=Codificare
-transformarea datelor dintr-un format în altul
-transferul datelor între sisteme diferite
-Informația NU este păstrată 'secretă'
-decodificarea datelor se face apeland doar la algoritmul utilizat
"""

#2.ENCRYPTION

"""
-datele sunt transformate astfel incat informatia sa devina 'secreta'
-algoritmul utilizat este în general public, iar cheia este 'secretă'
-cuvinte cheie:
    -plaintext='text în clar'
    -ciphertext='text cifrat'
-tipuri:
    -Private-Key Encryption=Criptare cu Cheie Privata
        -in acest caz aceasi cheie este folosita pentru criptare si decriptare
        -criptarea cu cheie privata este mai rapida decat criptarea cu cheie publica
        -cheia privata este simetrica (aceasi cheie este folosita atat pentru criptare cat si pentru decriptare)
        -cheia este 'secreta'
    -Public-Key Encryption=Criptare cu Cheie Publică
        -in acest caz sunt folosite doua chei (o cheie pentru criptare si o cheie pentru decriptare)
        -cheia publica este asimetrica (se folosesc doua tipuri diferite de chei)
        -una dintre chei este 'secreta'
"""

#|----------------------------------------------------------------------------------------------------------------

#3.Formate pentru pastrarea datelor

"""
-ASCII (text):
   -ord('char')-returneaza codul ASCII al caracterului
   -chr(codul_ascii)-returneaza caracterul corespunzator codului ASCII
-BINAR:
   -orice numar in baza 2, are prefixul '0b'
   -bin()-face conversia din baza 10 in baza 2
-HEXAZECIMAL:
   -orice numar in baza 16 are prefixul '0x'
   -hex()-face conversia din baza 10 in baza 16
-BASE 64:
   -pentru a converti octeții ce contin date binare sau text în caractere ASCII.
   -codificarea previne coruperea datelor atunci când sunt transferate sau procesate in web
   -utilizeaza ca si caractere: a-z, A-Z, 0-9 împreună cu '+' și '/'.
OBS:
1.int(number,k)-converteste numarul din baza k, in baza 10
2.orice operatie efectuata cu numere in alta baza decat baza 10, va avea
rezultatul in baza 10
"""

#|----------------------------------------------------------------------------------------------------------------

#Ex1:Afisarea primelor 100 de caractere din UNICODE

for i in range(100):
    print(i,"-",chr(i))

#Ex2:Afisarea caracterului din spatele codului ASCII citit de la tastatura

char=int(input("Introduceti codul ASCII: "))
print(chr(char))

#Ex3: Functia urmatoare returneaza codul ASCII al caracterului transmis ca parametru

def ascii_code(char):
    return ord(char)
print(ascii_code('u'))

#Ex4: Operatii in baza 2

n1=0b101#5
n2=0b110#6
print(n1+n2)#rezultatul este returnat in baza 10
print(bin(n1+n2))#rezultatul este returnat in baza 2

#Ex5: Operatii in baza 16

n5=0xA
n6=0xB
print(n5+n6)#rezultatul este returnat in baza 10
print(hex(n5+n6))#rezultatul este returnat in baza 16

#Ex6: Codificarea datelor in Base64

import base64
string= "Laboratorul 2"
string_bytes = string.encode("ascii")#codam fiecare caracter din string in ASCII code
base64_bytes = base64.b64encode(string_bytes)#transformam fiecare valoare ASCII in binar pe 8 biti si trecem sirul in Base64
print("Encoded string: ",base64_bytes)

#Ex7: Decodificarea datelor in Base64

import base64
base64_string ="TGFib3JhdG9ydWwgMg=="
base64_bytes = base64_string.encode("ascii")
sample_string_bytes = base64.b64decode(base64_bytes)
print("Decoded string:",sample_string_bytes)


#|----------------------------------------------------------------------------------------------------------------























