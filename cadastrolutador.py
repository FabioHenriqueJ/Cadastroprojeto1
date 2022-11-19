op = 0
es = 0
vit = 1
der = 0
while op != 5:
    print('========Cadastro de LUTADORES========')
    print('1> cadastrar\n2> Adicionar cartel\n3> Editar cartel\n4> Mostrar\n5> Sair do programa')
    op = int (input('EScolha uma das opções: '))
    if op == 1:
        nome = str(input('nome '))
        estilo = str(input('estilo de luta '))
        idade = int(input('idade '))
        altura = float(input('altura '))
        peso = float(input('peso '))
        categoria = str(input('categoria '))

    elif op == 2:
         s = 0
         n = 0
         vd = int(input('venceu? (1/sim. 2/não'))
         if vd == 1:
             vit +=1
         elif vd == 2:
             der +=1
    elif op == 4:
        print(f'nome:{nome}\neslilo:{estilo}\nidade:{idade}\naltura:{altura}\npeso:{peso}\ncategoria:{categoria}\nvitoria:{vit}\nderrota:{der}')
    elif op == 5:
        print('finalizando programa')














