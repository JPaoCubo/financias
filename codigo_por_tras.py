import sqlite3 as lite

con = lite.connect('dados.db')
#Se o arquivo dados.db não existir, o Python o criará automaticamente. Se já existir, ele apenas se conectará a ele

cur = con.cursor()
#O Cursor (cur) é o objeto que realmente executa os comandos SQL e navega pelos resultados. Sem ele, você tem a conexão, mas não tem como enviar comandos.

with con:
    #Tabela de categoria (ex: Alimentação, Transporte, Namorada,...)
    cur.execute("CREATE TABLE categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

    #Tabela de receita (Entrada de Dinheiro)
    cur.execute("CREATE TABLE receita(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")

    # Tabela de gastos (Saídas de dinheiro)
    cur.execute("CREATE TABLE gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")

    # Tabela de metas (onde eu quero atingir)
    cur.execute("CREATE TABLE metas(id INTEGER PRIMARY KEY AUTOINCREMENT, objetivo TEXT, valor_alvo DECIMAL)")

    #Tabela meios de pagamento(ex: Pix, Débito, Crédito,...)
    cur.execute("CREATE TABLE meios(id INTEGER PRIMARY KEY AUTOINCREMENT, tipo TEXT)")

