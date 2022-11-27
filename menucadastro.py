op = 0
es = 0
vit = 0
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
         vd = str(input('venceu? (S/sim. N/não')).strip().upper()[0]
         s = 0
         n = 0
         while vd not in 'S/N':
          vd = str(input('Somente> S para venceu e N para perdeu')).strip().upper()[0]
         if vd == 'S':
             vit +=1
         if vd == 'N':
             der +=1
    elif op == 3:
            print('1> editar nome\n2> editar estilo de luta\n3>editar cartel')
            ed = int(input('EScolha uma das opções: '))
            if ed == 1:
             nome = str(input('nome'))
             nome = (nome)
    elif op == 4:
        print(f'nome:{nome}\neslilo:{estilo}\nidade:{idade}\naltura:{altura}\npeso:{peso}\ncategoria:{categoria}\nvitoria:{vit}\nderrota:{der}')
    elif op == 5:
        print('finalizando programa')