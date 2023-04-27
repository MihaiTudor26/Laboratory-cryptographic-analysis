#Brute Force----------------------------------------------------

"""
Un atac de tip Brute Force presupune incercarea tuturor key-lor
posibile pentru decripatarea codului."""

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'#mesajul criptata
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'#totalitatea caracterelor ce pot fi folosite in criptarea mesajului
for key in range(len(SYMBOLS)):#generam toate key-le posibile
    translated=''#pentru fiecare cheie generata, 'translated' va retine mesajul decriptat
    for symbol in message:#parcurgem fiecare caracter al mesajului
        if symbol in SYMBOLS:
            symbolIndex=SYMBOLS.find(symbol)#determinam index-ul pe care se regaseste litera din mesajul criptat in lista tuturor caractrelor posibile folosite la criptare
            translatedIndex=symbolIndex-key#determinam index-ul caracterului ce decripteaza litera criptata folosind cheia de decriptare corespunzatoare pasului de loop-are
            if translatedIndex<0:
                translatedIndex=translatedIndex+len(SYMBOLS)#in cazul unui index de decriptare negativ apare efectul de wrapp-around
            translated=translated+SYMBOLS[translatedIndex]#determinam indexul decriptat si il adaugam la variabila translated ce va retine mesajul decriptat folosind cheia de decriptare de la pasul curent
        else:
            translated=translated+symbol#daca caracterul din mesajul criptat nu se regaseste in lista cu posibilele carctere utilizate in criptare, acesta se adauga neschimbat in mesajul decriptat
    print('Key #',key,translated)#pentru fiecare cheie posibila afisam mesajul decriptat cu cheia respectiva


"""
Punctul cel mai vulnerabil din Caesar Cipher se datoreaza numarului mic de chei posibile ce pot fi utilizate
pentru a cripta mesajul.
Astfel, generarea tuturor cheilor posibile pentru decriptare, presupune un efort scazut."""
        


