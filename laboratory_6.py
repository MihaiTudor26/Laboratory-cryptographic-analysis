################################# Laborator 6 #################################

#1.Criptarea continutului unui fisier

#importam biblioteca 'fernet'
from cryptography.fernet import Fernet

#generam o cheie de criptare
key = Fernet.generate_key()

#adaugam cheia de criptare in fisierul cheie_criptare
file_key=open('cheie_criptare.key','wb')
file_key.write(key)
file_key.close()

#deschidem fisierul cheie_criptare in modul citire
file_key_citire=open('cheie_criptare.key','rb')
key=file_key_citire.read()
file_key_citire.close()

#aplicam algoritmul de criptare Fernet pentru cheia generata
fernet=Fernet(key)

#deschidem in modul citire fisierul pe care il criptam
fisier_criptat=open('criptare.txt', 'rb') 

#citim continutul fisierului pe care il criptam
original = fisier_criptat.read()
fisier_criptat.close()

#criptam continutul fisierului
encrypted = fernet.encrypt(original)

#deschidem fisierul in modul scriere si adaugam datele criptate in el
fisier_criptat=open('criptare.txt', 'wb')
fisier_criptat.write(encrypted)
fisier_criptat.close()

#|------------------------------------------------------------------------------

#2.Decriptarea continutului unui fisier

#importam biblioteca 'fernet'
from cryptography.fernet import Fernet

#deschidem fisierul cheie_criptare in modul citire
file_key_citire=open('cheie_criptare.key','rb')
key=file_key_citire.read()
file_key_citire.close()

#aplicam algoritmul de criptare Fernet pentru cheia generata
fernet=Fernet(key)

#deschidem in modul citire fisierul pe care il decriptam

fisier_criptat=open('criptare.txt', 'rb') 
continut_criptat = fisier_criptat.read()
fisier_criptat.close()

#decriptarea fisierului criptat
continut_decriptat = fernet.decrypt(continut_criptat)

#deschidem fisierul in modul scriere si il decriptam
dec_file=open('criptare.txt', 'wb')
dec_file.write(continut_decriptat)
dec_file.close()





















