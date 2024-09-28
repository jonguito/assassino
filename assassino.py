assassino = 0
p1 = int(input('''Telefonou para a vítima?
[1]- sim
[2]- não
--> '''))
if p1 == 1:
    assassino +=1

p2 = int(input('''Esteve no local do crime?
[1]- sim
[2]- não
--> '''))
if p2 == 1:
    assassino +=1

p3 = int(input('''Mora perto da vítima?
[1]- sim
[2]- não
--> '''))
if p3 == 1:
    assassino +=1

p4 = int(input('''Devia para a vítima?
[1]- sim
[2]- não
--> '''))
if p4 == 1:
    assassino += 1

p5 = int(input('''Já trabalhou com a vítima?
[1]- sim
[2]- não
--> '''))
if p5 == 1:
    assassino += 1
if assassino  == 2 :
    
    print('inocente meu patrão.')
elif assassino == 3 or assassino == 4:
    
    print('tu é cumplice.')
elif assassino == 5:
    print('O ASSASSINO É TU FI DA PESTE!!')
    
else:
    print('tu é inocente meu patrao,bom dia.')
