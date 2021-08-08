galera = []
dado = []
totmai = totmen = 0
for i in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for i in galera:
    if i[1] >= 18:
        print(f'{i[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{i[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} pessoas maior de idade e {totmen} menor de idade')


'''galera = [['Patricia', 27], ['Nenkinho', 31], ['Jose', 12]]
for i in galera:
    print(f'{i[0]} tem {i[1]} anos')'''
