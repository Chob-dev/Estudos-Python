#Questão 1
a = float(input())
pi = 3.14159
print(f"A={pi*(a**2):.4f}")
#Questão 2
b = float(input())
c = float(input())
d = float(input())
print(f"Média={((b*2)+(c*3)+(d*5))/10:.1f}")
#Questão 3
e = int(input())
f = float(input())
print(f"{e/f:.3f}km/l")
#Questão 4
g = float(input())
h = float(input())
i = float(input())
j = float(input())
print(f"{((i-g)**2+(j-h)**2)**(0.5):.4f}")
#Questão 5 
k = int(input())
l = int(input())
m = int(input())
maiorkl = (k+l+abs(k-l))/2
maior = (maiorkl + m +abs(maiorkl-m))/2
print(f"{maior:.0f} é o maior")
#Questão 6
n = int(input())
o = int(input())
if o % n == 0:
    print("Sim")
else:
    print("Não")
#Questão 7
p = float(input())
if p<=1212:
    print(f"R$ {((p*20)/100)+p:.2f}")
else:
    print(f"R${((p*15)/100)+p:.2f} ")
#Questão 8
q = float(input())
r = float(input())
media = (q+r)/2
if media<3:
    print(f"{media:.1f} - Reprovado")
elif 3<media<7:
    print(f"{media:.1f} - Exame")
elif 10>media>7:
    print(f"{media:.1f} - Aprovado")
#Questão 9
s = float(input()) 
t = float(input())
u = float(input())
if s>t and u:
    print(f"{s:.0f}")
elif t>s and u:
    print(f"{t:.0f}")
elif u>s and t:
    print(f"{u:.0f}")
#Questão 10
v = float(input())
w = float(input())
x = int(input())
if x==1:
    print(f"{v**w:.1f}")
elif x==2:
    print(f"{((v)**2)+((w)**2):.1f}")
elif x==3:
    print(f"{((v)**0.5)+((w)**0.5):.1f}")
elif x!=1 and 2 and 3:
    print("ERRO")





















