print('Os acompanhantes com menores de 18 anos não contam.')
print('Digite seu nome corretamente com a primeira letra maiúscula')
print('E por favor não mentem sua idade')
nome = str(input('Qual é o seu nome ?')).strip()

try:
    idade_str = input('Qual é a sua idade? ')
    idade = int(idade_str)
    idade_valida = True
except ValueError:
    print(f'Você digitou uma idade inválida senhor {nome}. Por favor, insira um número.')
    idade = -1
    idade_valida = False

invited_names = ['Pedro','Amanda','Ipoty','Thais','kyle']
separator = '-------------------------'

print (f'{separator}')

if nome in invited_names:
  print(f'Você esta convidado senhor {nome}')
elif idade_valida and idade < 18:
  print(f'Acompanhantes de menos de 18 anos não contam senhor {nome}')
elif idade_valida and idade >= 18:
  print(f'Bem-vindo senhor {nome}')
else:
  print(f'Não foi possível verificar suas informações senhor {nome}')
