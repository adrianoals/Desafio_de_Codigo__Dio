#Desafio Otimizando o Sistema Bancário com Funções Python
"""
Objetivo Geral:
Separar as funçoões existentes de saque, depósito e extrato em funções: cadastrar usuário (cliente) e cadastrar conta bancária.

Precisamos deixar nosso códigco mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e vizualizar histórico. Além disso criar duas novas funções: criar usuário(cliente do banco) e criar conta corrente (vincular com usuário).

Separação Em Funcões
Devemos criar funções para todas as operações do sistema. Para exercitar tudo que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.

Saque:
A função saque deve receber os arugumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saque, limite_saques. Sugestão de retorno: saldo e extrato.

Depósito
A função depósito deve receber os argumentos apenas por posição(posional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

Extrato:
A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

Novas Funções:
Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

Criar usuário (cliente):
O programa deve armazenar os usuários em uma list, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é umas string com o formato: logradouro, nro  -  bairro  - cidade/sigla estado.Deve ser armazenado somento os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

Criar conta corrente
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário

Dica:
Para vincular usuário a uma conta filtre a lista de usuários buscando o número do CPF informando para cada usuário da lista. 
"""
