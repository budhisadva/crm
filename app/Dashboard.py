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
# -------------------Cliente------------------------
# --------------------------------------------------
@bp.route('/clientes/pag/<int:n>/', methods=['GET'])
def clientes(n):
    contexto = dict()
    contexto['n'] = n
    if n < 1:
        return redirect(url_for('dashboard.clientes', n=1))
    if len(request.args) == 0:
        contexto['clientes'] = selectAllPaginado(tabla='Cliente', pag=n)
        contexto['total'] = selectCount('Cliente')['total']
        t = contexto['total']
        contexto['paginas'] = int((t - (t % 15))/15)
    else:
        if request.args.get('busqueda') == '':
            return redirect(url_for('dashboard.clientes', n=n))
        else:
            contexto['clientes'] = selectAllBusqueda(tabla='Cliente', arg=request.args.get('busqueda'), atr='nombre', ord=True)
            return render_template('clientes/clientes.html', **contexto)
    return render_template('clientes/paginado.html', **contexto)


@bp.route('/add_clt/', methods=['GET', 'POST'])
def nuevoCliente():
    contexto = dict()
    if request.method == 'GET':
        contexto['tipos'] = selectAll(tabla='TipoCliente')
        contexto['mercados'] = selectAll(tabla='Mercado')
        return render_template('clientes/add_clt.html', **contexto)
    else:
        # insert(tabla='Cliente', datos=request.form.copy())
        flash('Cliente agregado correctamente')
        return redirect(url_for('dashboard.clientes', n=1))

@bp.route('/edit_clt/<string:id>', methods=['GET', 'POST'])
def editaCliente(id):
    contexto = dict()
    if request.method == 'GET':
        contexto['cliente'] = selectId(tabla='Cliente', atr='id', val=id)
        contexto['tipos'] = selectAll('TipoCliente')
        contexto['mercados'] = selectAll('Mercado')
        return render_template('clientes/edit_clt.html', **contexto)
    else:
        # update(tabla='Cliente', id=id, datos=request.form.copy())
        flash('Cliente actualizado correctamente')
        return redirect(url_for('dashboard.clientes', n=1))

@bp.route('/delete_clt/<string:id>', methods=['GET'])
def borraCliente(id):
    delete(tabla='Cliente', id=id)
    flash('Cliente eliminado correctamente')
    return redirect(url_for('dashboard.clientes', n=1))
# --------------------------------------------------
# ------------------Producto------------------------
# --------------------------------------------------
@bp.route('/productos/pag/<int:n>/', methods=['GET'])
def productos(n):
    contexto = dict()
    contexto['n'] = n
    if n < 1:
        return redirect(url_for('dashboard.clientes', n=1))
    if len(request.args) == 0:
        contexto['productos'] = selectAllPaginado(tabla='Producto', pag=n)
        contexto['total'] = selectCount('Producto')['total']
        t = contexto['total']
        contexto['paginas'] = int((t - (t % 15))/15)
    else:
        if request.args.get('busqueda') == '':
            return redirect(url_for('dashboard.productos', n=n))
        else:
            contexto['productos'] = selectAllBusqueda(tabla='Producto', arg=request.args.get('busqueda'), atr='clave', ord=True)
            return render_template('productos/productos.html', **contexto)
    return render_template('productos/paginado.html', **contexto)

@bp.route('/add_pdt/', methods=['GET', 'POST'])
def nuevoProducto():
    contexto = dict()
    if request.method == 'GET':
        contexto['marcas'] = selectAll('Marca')
        return render_template('productos/add_pdt.html', **contexto)
    else:
        # insert(tabla='Producto', datos=request.form.copy())
        flash('Producto agregado correctamente')
        return redirect(url_for('dashboard.productos', n=1))


@bp.route('/edit_pdt/<string:id>', methods=['GET', 'POST'])
def editaProducto(id):
    contexto = dict()
    if request.method == 'GET':
        contexto['id'] = id
        contexto['producto'] = selectId(tabla='Producto', atr='id', val=id)
        contexto['marcas'] = selectAll('Marca')
        return render_template('productos/edit_pdt.html',**contexto)
    else:
        # update(tabla='Producto', id=id, datos=request.form.copy())
        flash('Producto actualizado correctamente')
        return redirect(url_for('dashboard.productos', n=1))

@bp.route('/delete_pdt/<string:id>', methods=['GET'])
def borraProducto(id):
    delete(tabla='Producto', id=id)
    flash('Producto eliminado correctamente')
    return redirect(url_for('dashboard.productos', n=1))
# -----------------------------------------------------#
# -----------------Usuario-----------------------------#
# -----------------------------------------------------#
@bp.route('/usuarios/', methods=['GET'])
def usuarios():
    contexto = dict()
    contexto['usuarios'] = selectAll('Usuario')
    return render_template('pagina/usuarios.html', **contexto)

@bp.route('/add_usr/', methods=['GET', 'POST'])
def nuevoUsuario():
    contexto=dict()
    if request.method == 'GET':
        return render_template('pagina/add_usr.html')
    else:
        return redirect(url_for('dashboard.usuarios'))

@bp.route('/edit_usr/<string:id>/')
def editaUsuario(id):
    flash('Usuario actualizado correctamente')
    return redirect(url_for('dashboard.usuarios'))

@bp.route('delete_usr/<string:id>/')
def borraUsuario(id):
    # delete(tabla='Usuario', id=id)
    flash('Usuario eliminado correctamente')
    return redirect(url_for('dashboard.usuarios'))
# ------------------------
# ---- Inventarios -------
# ------------------------
@bp.route('/inventario/', methods=['GET'])
def inventario():
    contexto = dict()
    if len(request.args) < 2:
        pass
    else:
        if request.args.get('busqueda') != '':
            contexto['productos'] = selectAllBusqueda(tabla='Producto', atr=request.args.get('categoria'), arg=request.args.get('busqueda'), ord=True)
        else:
            return redirect(url_for('dashboard.inventario'))
    return render_template('inventario/inventario.html', **contexto)

@bp.route('', methods=['GET'])

# --------------------------------------------------
# ------------------Cotizaciones--------------------
# --------------------------------------------------
@bp.route('/cotizaciones/', methods=['GET'])
def cotizaciones():
    cotizaciones = selectAll(tabla='Cotizacion')
    return render_template('pagina/cotizaciones.html', cotizaciones=cotizaciones)

@bp.route('/add_cot/', methods=['GET', 'POST'])
def nuevaCotizacion():
    if request.method == 'GET':
        contexto = dict(marcas = selectAll('Marca'),
                        mercados = selectAll('Mercado'))
        print('#############################')
        print('Argumentos: ', request.args)
        print('#############################')
        print('Formulario: ', request.form)
        print('#############################')
        return render_template('pagina/add_cot.html', contexto=contexto)
    else:
        print(request.form)
        return redirect(url_for('dashboard.cotizaciones'))
