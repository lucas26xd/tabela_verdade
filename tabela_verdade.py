COND = (' ', '&', '|')


def tabela_verdade(linha, cond):  # Calcula a expressão de cada linha par a par
    result = True if cond == '&' else False  # Elemneto neutro do AND é V e do OR é F
    for i in range(len(linha)):
        if cond == '&':
            result = result and linha[i]
        else:
            result = result or linha[i]
    return 'V' if result else 'F'

### INICIALIZAÇÃO DAS VARIÁVEIS ###
n = int(input('x = '))
qtd_repete = 2 ** n
qtd_alterna = 1
tabela = []
for i in range(qtd_repete):
    tabela.append([])

### PREENCHIMENTO DA TABELA VERDADE DE ACORDO COM O NÚMERO DE VARIÁVEIS ###
for v in range(n + 1):
    qtd_alterna = qtd_alterna * 2
    qtd_repete = qtd_repete // 2
    valor = True
    x = 0
    for i in range(qtd_alterna):
        for j in range(qtd_repete):
            tabela[x].append(valor)
            x += 1
        valor = not valor

### IMPRIME CABEÇALHO ###
for c in COND:
    for i in range(n):
        print(chr(65 + i), end=c if i < n - 1 else '')  # chr(65 + i) = A, B, C, ...
    print('  ', end='')
print()
print('_' * (n * 6 + 4))

### IMPRIME TABELA VERDADE COM RESPECTIVOS RESULTADOS DE AND E OR ###
for i in range(len(tabela)):
    for j in range(len(tabela[i])):
        print('V' if tabela[i][j] else 'F', end=' ')
    print(f'{tabela_verdade(tabela[i], cond="&"):>{n * 2}}', end=' ')
    print(f'{tabela_verdade(tabela[i], cond="|"):>{n * 2}}')
