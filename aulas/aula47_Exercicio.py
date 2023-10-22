'''
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Seu nome e didade foram digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem{n} Letras
        A Primeira letra do seu nome é {Letra}
        A Ultima letra do seu nome é {Letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, Você deixou Campos Vazios."
'''
nome = input('Digite o seu nome: ')
idade = input('Agora digite a sua idade: ')
nome_invertido = (nome)
    
if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Sua idade e: {idade}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else: 
        print('Seu nome não contém espaços')
    
    print(f'Seu nome tem {len(nome)} Letras')
    print(f'A Primeira letra do seu nome é: {nome[0]}')
    print(f'A Ultima letra do seu nome é: {nome[-1]}')

else: 
    print("Desculpe, Você deixou Campos Vazios.")    
