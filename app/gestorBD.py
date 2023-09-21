from app.database.db import get_db
# select
def selectAll(tabla):
    db, c = get_db()
    c.execute(f'select * from {tabla}')
    return c.fetchall()

def selectAllPaginado(tabla, pag):
    tam = 10
    inf = (pag-1)*tam
    db, c = get_db()
    c.execute(f'select * from {tabla} limit {inf}, {tam}')
    return c.fetchall()

def selectAllBusqueda(tabla, arg, atr, ord):
    db, c = get_db()
    b = '%{}%'.format(arg)
    if ord:
        c.execute(f'select * from {tabla} where {atr} like %s order by {atr} asc', (b,))
    else:
        c.execute(f'select * from {tabla} where {atr} like %s', (b,))
    return c.fetchall()

def selectId(tabla, atr, val):
    db, c = get_db()
    c.execute(f'select * from {tabla} where {atr} = {val}')
    return c.fetchone()
# insert
def insert(tabla, datos):
    db, c = get_db()
    llv=list(datos)
    n=len(llv)
    col, v = '', ''
    i = 0
    while i < n:
        if i != n-1:
            col += '{}, '.format(llv[i])
            v += "'{}', ".format(datos[llv[i]])
        else:
            col += llv[i]
            v += "'{}'".format(datos[llv[i]])
        i += 1
    c.execute(f'insert into {tabla} ({col}) values ({v})')
    db.commit()
    return 0
# update
def update(tabla, id, datos):
    db, c = get_db()
    llv=list(datos)
    n=len(llv)
    w = ''
    i = 0
    while i < n:
        if i != n-1:
            w += "{} = '{}', ".format(llv[i], datos[llv[i]])
        else:
            w += "{} = '{}'".format(llv[i], datos[llv[i]])
        i += 1
    c.execute(f'update {tabla} set {w} where id = {id}')
    db.commit()
    return 0
# delete
def delete(tabla, id):
    db, c = get_db()
    c.execute(f'delete from {tabla} where id = {id}')
    db.commit()
    return 0
