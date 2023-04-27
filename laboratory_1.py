######################   BASIC ELEMENTS OF A PYTHON PROGRAM  ##########################

"""
Python IDLE (Integrated DeveLopment Enviroment):https://www.python.org/downloads/
CMD--->pip install module_name
"""


#1.Comments
#Acesta este un mesaj pe un singur rand
"""
Acesta este un mesaj
pe mai multe randuri"""

#2. Output

print("Acesta este mesaj")
print(2.6+2.9)
x=4
print("Continutul variabilei x este: ",x)

#3.Assigments
"""
variable_name=expression"""

a=b=c=3
print(a,b,c)

#EX: Interschimbarea continutului a doua variabile

"""
Var1:
"""
x1=4
x2=9
x3=x1
x1=x2
x2=x3
print("x1=",x1)
print("x2=",x2)

"""
Var 2:
"""
x1=4
x2=9
x1,x2=x2,x1
print("x1=",x1)
print("x2=",x2)

"""
Var3:
"""
x1=4
x2=9
x1=x1+x2
x2=x1-x2
x1=x1-x2
print("x1=",x1)
print("x2=",x2)

#4.Numeric data type
var1=4
var2=2.9
var3=True
var4="Python"
var5=[1,4,9,0]
print("Tipul variabilei: ",type(var5))
"""
obs: Tipul unei variabile in Python se poate stabili apeland functia tipe()"""

#5.Input
#-citirea unei valori numerica
a=eval(input("Introduceti o valoare numerica:"))
print("a=",a)
#-citirea unei valori in functie de tipul sau
a=str(input("Introduceti o valoare:"))
print("a=",a)

#Obs: str poate fi inlocuit in structura de mai sus in functie de context cu:
"""floot,bool,list,int..."""

#6.Comparation operators
"""
>,<,==,!=,<=,>="""
print(2==6)

#7. Logic operators
"""
and,or,not"""

#8.Aritmetic operators
"""
+,-,/,%,//,*,**
//-returneaza rezultatul impartirii intregi
**-operatorul de ridicare la putere"""
print(3/2)
print(3//2)
print(3**2)

#9. Conditional Statements

"""
A) if condtion:
     expression
     --------
   else:
     expression

B) if condition:
      expression
      ---------
   elif condition:
      expression
   else:
      expression"""

#Ex: Maximul a trei valori citite de la tastatura
a=eval(input("a="))
b=eval(input("b="))
c=eval(input("c="))
if a>b and a>c:
    print("Max: ",a)
elif b>a and b>c:
    print("Max: ",b)
elif c>a and c>b:
    print("Max: ",c)

#10. Control flow: while and for loops

"""
while condition:
   expression
   ---------

for variable in range(star_point,end_point+1,step):
    expression
    --------
"""
#Ex1: Suma primelor n numere pare, n citit de la tastatura
n=int(input("n="))
s=0
for i in range(0,n+1,2):
    s=s+i
print(s)

#Ex2: Prima cifra a unui numar citit de la tasatatura
n=int(input("n="))
while n>9:
    n=n//10
print("Prima cifra a numarului: ",n)

#Ex3: Cel mai mare divor comun a doua numere citite de la tasatatura
a=int(input("a="))
b=int(input("b="))
if a==0:
    gcd=b
else:
    if b==0:
        gcd=a
    else:
        while a!=b:
            if a>b:
                a=a-b
            else:
                b=b-a
        gcd=a
print("GCD:",gcd)


#11. Random module
from random import*
print("Generam un numar random intreg intre 1-10: ",randint(1,10))
print("Generam un random real intre 1-10: ",uniform(1,10))
print("Generam un numar random intre 0-1:",random())

#Ex: Generati 6 numere intregi intre 1-49
for i in range(6):
    print(randint(1,49),end=" ")




    








































