import random
#Informações do bebê
resposta = 's'
while resposta.upper() == 'S':
    print('*'*50)
    nome_crianca = input('Nome da criança: ')
    nasc = (input('Data de nascimento: '))
    peso = float(input('Peso de nascimento em KG: '))
    altura = float(input('Altura de nascimento em CM: '))

    mae = input('Mãe:  ')
    pai = input('Pai: ')
    medico = input('Médico que realizou o parto: ')

    #RELATÓRIO
    print('*'*50)
    print('RELATÓRIO')
    print(f'Nome do bebê: {nome_crianca}. \n')
    print(f'Data de nascimento: {nasc}. \n')
    print(f'Peso de nascimento da criança: {peso}. \n')
    print(f'Altura de nascimento: {altura}. \n')
    print(f'Nome da mãe: {mae}. \n')
    print(f'Nome do pai: {pai}. \n')
    print(f'Responsável pelo parto: {medico}. \n')


    #Controle do berçario
    print('*'*50)
    quarto = (input('Quarto alocado: '))

    #Dados da gestante
    print(f'Nome da mãe: {mae}. ')
    endereco = input('Endereço: ')
    telefone = int(input('Telefone de contato: '))
    nascimento = input('Data de nascimento: ')

    print('*'*50)
    print('FICHA DE INTERNAÇÃO')
    print(f'Gestante: {mae}. \n')
    print(f'Endereço: {endereco}. \n')
    print(f'Telefone: {telefone}. \n')
    print(f'Data de nascimento: {nascimento}. \n')
    print(f'Quarto de internação: {quarto}. \n')
    print('*'*50)


    #Dados do médico 
    
    print(f'Nome do médico:  {medico} \n')
    telefone_md = int(input('Telefone para contato: \n'))
    especialidade = input('Especialidade: \n')
    
    CRM = '1234567890'
    crm_aleatoria = random.choices(CRM,k=10)

    crm_final = ''
    for numero in crm_aleatoria:
        crm_final += numero

    print(f'O número do CRM é: {crm_final}. \n')
    resposta = input('Deseja fazer outro cadastro? S/N: ')
    print('Operação Realizada com sucesso.')
