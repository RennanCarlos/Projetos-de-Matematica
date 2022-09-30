import math

hipotenusa = str(input("Digite o valor da hipotenusa: "))
cateto1 = str(input("Digite o valor do cateto1: "))
cateto2 = str(input("Digite o valor do cateto2: "))

letras = ['a', 'b','c', 'd','e', 'f','g', 'h','i', 'j','k', 'l','m', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
l = [hipotenusa, cateto1, cateto2]
x = 0

for i in range(0,3):
    if l[i] in letras:
        l.pop(i)
        break

if not hipotenusa in l:
    x = (int(l[0]) ** 2) + (int(l[1]) ** 2) 
    
    x = math.sqrt(x)
    print("Hipotenusa é:",x)

if not cateto1 in l or cateto2 not in l:
    if int(l[1]) < 0:
        l[1] = int(l[1]) + abs(int(l[1]) * 2)
        x = (int(l[0]) ** 2) + (int(l[1]) ** 2)
        
        math.sqrt(x)
        print("x é igual a:",x)

    if int(l[1]) > 0:
        l[1] = int(l[1]) / (-1)
        x = (int(l[0]) ** 2) - (int(l[1]) ** 2)
        
        x = math.sqrt(x)
        print("x é igual a:",x)