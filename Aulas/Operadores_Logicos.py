True or False
7 != 3 and 2 > 3 

#Tabela verdade do AND
True and True
True and False
False and True
False and False
True and True and True and True and True and True and False and True

#Tabela verdade do OR
True or True
True or False
False or True
False or False 
False or False or False or False or False or False or True or False 

#Tabela verdade do XOR
True != True
True != False
False != True
False != False

# Operador de Negação (unário)
not True
not False

not 0
not 1
not not -1
not not True

#Operador Binário, cuidado !!!
True & False
False | True
True ^ False

# AND Bit-a-Bit
# 3 = 11 
# 2 = 10
# _ = 10
3 & 2

# OR Bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 11
3 | 2 

# XOR Bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 01
3 ^ 2 

# Realidade
saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas
print(meta)

