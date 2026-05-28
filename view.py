import sqlite3 as lite

con = lite.connect('dados.db')

# função para inserir categoria
def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO categoria (nome) VALUE (?)"
        cur.execute(query, i)

#funçãopara inserir receita
def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO receita (categoria, adicionado_em, valor) VALUE (?, ?, ?)"
        cur.execute(query, i)

#funçãopara inserir gastos
def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO gastos (categoria, retirado_em, valor) VALUE (?, ?, ?)"
        cur.execute(query, i)

#funçãopara inserir metas
def inserir_metas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO metas (objetivo, valor_alvo) VALUE (?, ?)"
        cur.execute(query, i)

#funçãopara inserir meios
def inserir_meios(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO meios (tipo) VALUE (?)"
        cur.execute(query, i)

#função para selecionar categoria
def ver_categoria():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM categoria")
        linha = cur.fetchall()
        for linha in linha:
            lista_itens.append(linha)
    return lista_itens

#função para selecionar receita
def ver_receita():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM receita")
        linha = cur.fetchall()
        for linha in linha:
            lista_itens.append(linha)
    return lista_itens

#função para selecionar gastos
def ver_gastos():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM gastos")
        linha = cur.fetchall()
        for linha in linha:
            lista_itens.append(linha)
    return lista_itens

#função para selecionar metas
def ver_metas():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM metas")
        linha = cur.fetchall()
        for linha in linha:
            lista_itens.append(linha)
    return lista_itens

#função para selecionar meios
def ver_meios():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM meios")
        linha = cur.fetchall()
        for linha in linha:
            lista_itens.append(linha)
    return lista_itens

#função para deletar categoria
def deletar_categoria(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM categoria WHERE id=?"
        cur.execute(query, i)

#função para deletar receita
def deletar_receita(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM receita WHERE id=?"
        cur.execute(query, i)

#função para deletar gastos
def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM gastos WHERE id=?"
        cur.execute(query, i)

#função para deletar metas
def deletar_metas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM metas WHERE id=?"
        cur.execute(query, i)

#função para deletar meios
def deletar_meios(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM meios WHERE id=?"
        cur.execute(query, i)

