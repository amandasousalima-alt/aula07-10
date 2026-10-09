import random
nome = input('Qual o seu nome? ')
quem = ['meu cachorro', 'meu primo', 'o wi-fi', 'o professor de matemática', 'meu gato']
acao = ['comeu', 'apagou', 'escondeu', 'hackeou', 'derrubou café']
alvo = ['meu caderno', 'meu notebook', 'minha tarefa', 'meu pen drive']

sorteio_quem = random.choice(quem)
sorteio_acao = random.choice(acao)
sorteio_alvo = random.choice(alvo)

print(f'Professor, desculpa! {sorteio_quem.capitalize()} {sorteio_acao} {sorteio_alvo}')
print(f'Assinado: {nome}')