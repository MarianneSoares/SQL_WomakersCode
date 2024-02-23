import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#1
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

#2
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "João Carlos", 21, "Medicina")');
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Maria Adelaide", 25, "Direito")');
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Robson Roberto", 20, "Engenharia")');
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Patricia Andre", 30, "Jornalista")');
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Gabriel Antonio", 18, "Engenharia")')

#3
#a)
cursor.execute('SELECT * FROM alunos')
dados = cursor.execute('SELECT * FROM alunos')
for usuario in dados:
    print(usuario)
print('---------------------------------------------------------')
#b)
cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
for usuario in dados:
    print(usuario)
print('---------------------------------------------------------')
#c)
cursor.execute('SELECT * FROM alunos WHERE curso =="Engenharia" ORDER BY nome')
dados = cursor.execute('SELECT * FROM alunos WHERE curso =="Engenharia" ORDER BY nome')
for usuario in dados:
    print(usuario)
print('---------------------------------------------------------')

#d)
cursor.execute('SELECT nome FROM alunos GROUP BY id')
b =0
aba = cursor.execute('SELECT nome FROM alunos GROUP BY id')
for a in aba:
    b = 1+b
    print(a)
print('total de alunos é', b)

#4
#a)
cursor.execute('UPDATE alunos SET idade = 23 WHERE id = 2')
idade_atualizada = cursor.execute('SELECT * FROM alunos WHERE id =2')
for i in idade_atualizada:
    print(i)
print('---------------------------------------------------------')

#b)
cursor.execute('DELETE FROM alunos WHERE id =1')
remover_aluno = cursor.execute('SELECT * FROM alunos')
for J in remover_aluno:
    print(J)
print('---------------------------------------------------------')

#5
cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT)')

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Joaquina", 35, 224.84)');
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Marcia Andreza", 26, 23.77)');
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Roberta Natalia", 43, 880.00)');
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Ana Bianca", 22, 01.55)');
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Carla", 55, 11.99)')

clientes = cursor.execute('SELECT * FROM clientes')
for unidade in clientes:
    print(unidade)
print('---------------------------------------------------------')

#6
#a)
idade_clientes = cursor.execute('SELECT nome FROM clientes WHERE idade>30')
for cliente in idade_clientes:
    print(cliente)
print('----------------------------------------------------')
#b)
mediaSaldo = cursor.execute('SELECT AVG(saldo) FROM clientes')
for cliente in mediaSaldo:
    cliente+=cliente
print(cliente)
print('----------------------------------------------------')
#c)
saldoMaximo = cursor.execute('SELECT Max(saldo) FROM clientes')
for cliente in saldoMaximo:
    print(cliente)
print('----------------------------------------------------')
#d)
saldo1000 = cursor.execute('SELECT nome FROM clientes WHERE saldo>1000')
for cliente in saldo1000:
    print(f'Os seguintes clientes com saldo acima de 1000 são: {cliente}')
print('----------------------------------------------------')

#7
#a)
cursor.execute('UPDATE clientes SET saldo = 1001 WHERE id=4')
#b)
cursor.execute('DELETE FROM clientes WHERE id=2')
print('----------------------------------------------------')

#8
cursor.execute('CREATE TABLE compras(id INT, cliente_id INT , produto VARCHAR(100), valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES clientes(id))');
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (1, "coleira", 55.99)');
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (2, "ração", 80.00)');
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (3, "pote de água", 25.50)');
cursor.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (5, "bolinha", 20.22)');
JuncaoTabelas = conexao.execute('SELECT clientes.nome AS nome_cliente, compras.produto, compras.valor FROM clientes JOIN compras ON clientes.id = compras.cliente_id')
for cliente in JuncaoTabelas:
    print(cliente)

conexao.commit()
conexao.close