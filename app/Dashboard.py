from flask import (
Blueprint, render_template, request, flash, url_for, redirect
)
from app.Producto import *
from app.Cliente import *
from app.database.db import get_db
from app.gestorBD import *

bp = Blueprint('dashboard', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('pagina/index.html')

# --------------------------------------------------
# ------------------Cotizaciones--------------------
# --------------------------------------------------
@bp.route('/cotizaciones', methods=['GET'])
def cotizaciones():
    cotizaciones = selectAll(tabla='Cotizacion')
    return render_template('pagina/cotizaciones.html', cotizaciones=cotizaciones)

@bp.route('/add_cot/', methods=['GET'])
def nuevaCotizacion():
    db, c = get_db()
    c.execute('select * from Marca')
    marcas = c.fetchall()
    c.execute('select * from Mercado')
    mercados = c.fetchall()
    if len(request.args) == 0:
        return render_template('pagina/add_cot.html', marcas=marcas, mercados=mercados)
    else:
        if 'busqueda_clt' in request.args.keys():
            if request.args.get('busqueda_clt') == '':
                return render_template('pagina/add_cot.html', marcas=marcas, mercados=mercados)
            else:
                b = '%{}%'.format(request.args.get('busqueda_clt'))
                c.execute("select * from Cliente where nombre like %s order by nombre asc", (b,))
                clientes = c.fetchall()
                return render_template('pagina/add_cot.html', marcas=marcas, mercados=mercados, clientes=clientes, encontrado=True)
        elif 'cliente' in request.args.keys():
            if request.args.get('cliente') == '':
                return render_template('pagina/add_cot.html', marcas=marcas, mercados=mercados)
            else:
                c.execute('select * from Cliente where id = {}'.format(request.args.get('cliente')))
                cliente = c.fetchone()
                return render_template('pagina/add_cot.html', marcas=marcas, mercados=mercados, seleccionado=True, cliente=cliente)
        else:
            return render_template('pagina/add_cot.html', marcas=marcas, mercados=mercados)

@bp.route('/add_cot/', methods=['POST'])
def registraCotizacion():
    print(request.form)
    return redirect(url_for('dashboard.cotizaciones'))

# --------------------------------------------------
# -------------------Cliente------------------------
# --------------------------------------------------
@bp.route('/clientes/pag/<int:n>/', methods=['GET'])
def clientes(n):
    if len(request.args) == 0:
        clientes = selectAllPaginado(tabla='Cliente', pag=n)
        return render_template('pagina/clientes.html', clientes=clientes, pag=n)
    else:
        if request.args.get('busqueda') == '':
            return redirect(f'/clientes/pag/{n}/')
        clientes = selectAllBusqueda(tabla='Cliente', arg=request.args.get('busqueda'), atr='nombre', ord=True)
    return render_template('pagina/clientes.html', clientes=clientes, pag=n)


@bp.route('/add_clt', methods=['GET', 'POST'])
def nuevoCliente():
    db, c = get_db()
    if request.method == 'GET':
        tipos = selectAll(tabla='TipoCliente')
        mercados = selectAll(tabla='Mercado')
        return render_template('pagina/add_clt.html', tipos=tipos, mercados=mercados)
    if request.method == 'POST':
        insert(tabla='Cliente', datos=request.form.copy())
        flash('Cliente agregado correctamente')
        return redirect('/clientes/pag/1/')

@bp.route('/edit_clt/<string:id>', methods=['GET', 'POST'])
def editaCliente(id):
    db, c = get_db()
    if request.method == 'GET':
        cliente = selectId(tabla='Cliente', atr='id', val=id)
        tipos = selectAll('TipoCliente')
        mercados = selectAll('Mercado')
        return render_template('pagina/edit_clt.html', cliente=cliente, tipos=tipos, mercados=mercados)
    if request.method == 'POST':
        update(tabla='Cliente', id=id, datos=request.form.copy())
        flash('Cliente actualizado correctamente')
        return redirect('/clientes/pag/1/')

@bp.route('/delete_clt/<string:id>', methods=['GET'])
def borraCliente(id):
    delete(tabla='Cliente', id=id)
    flash('Cliente eliminado correctamente')
    return redirect('/clientes/pag/1/')
# --------------------------------------------------
# ------------------Producto------------------------
# --------------------------------------------------
@bp.route('/productos/pag/<int:n>/', methods=['GET'])
def productos(n):
    db, c = get_db()
    if len(request.args) == 0:
        productos = selectAllPaginado(tabla='Producto', pag=n)
        return render_template('pagina/productos.html', productos=productos, pag=n)
    else:
        if request.args.get('busqueda') == '':
            return redirect(f'/productos/pag/{n}')
        productos = selectAllBusqueda(tabla='Producto', arg=request.args.get('busqueda'), atr='clave', ord=True)
    return render_template('pagina/productos.html', productos = productos, pag=n)

@bp.route('/add_pdt', methods=['GET', 'POST'])
def nuevoProducto():
    db, c = get_db()
    if request.method == 'POST':
        p = Producto()
        p.setByRequest(request.form)
        col, val = p.insertQuery()
        c.execute('insert into Producto ({}) values ({})'.format(col, val))
        db.commit()
        flash('Producto agregado correctamente')
        return redirect('productos/pag/1/')
    elif request.method == 'GET':
        c.execute('select * from Marca')
        marcas = c.fetchall()
        return render_template('pagina/add_pdt.html', marcas=marcas)
    else:
        return render_template('pagina/index.html')

@bp.route('/edit_pdt/<string:id>', methods=['GET', 'POST'])
def editaProducto(id):
    db, c = get_db()
    c.execute('select * from Producto where id = {}'.format(id))
    producto = c.fetchone()
    c.execute('select * from Marca')
    marcas = c.fetchall()
    db.commit()
    if request.method == 'GET':
        return render_template('pagina/edit_pdt.html', id=id, producto=producto, marcas=marcas)
    elif request.method == 'POST':
        p = Producto()
        p.setByRequest(request.form)
        s = p.updateQuery()
        c.execute("update Producto set {} where id = {}".format(s, id))
        db.commit()
        flash('Producto actualizado correctamente')
        return redirect('/productos/pag/1/')

@bp.route('/delete_pdt/<string:id>', methods=['GET'])
def borraProducto(id):
    db, c = get_db()
    c.execute('delete from Producto where id = {}'.format(id))
    db.commit()
    flash('Producto eliminado correctamente')
    return redirect('/productos/pag/1/')
# -----------------------------------------------------#
# -----------------------------------------------------#
# -----------------------------------------------------#
@bp.route('/usuarios', methods=['GET'])
def usuarios():
    db, c = get_db()
    c.execute('select * from Usuario')
    usuarios = c.fetchall()
    return render_template('pagina/usuarios.html', usuarios=usuarios)

@bp.route('/usua-nuevo', methods=['GET'])
def nuevoUsuario():
    return render_template('pagina/form-usua.html')
