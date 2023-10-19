instructions = [
    'SET FOREIGN_KEY_CHECKS = 0;',
    'drop table if exists TipoCliente;',
    'drop table if exists Mercado;',
    'drop table if exists Marca;',
    'drop table if exists Usuario;',
    'drop table if exists Producto;',
    'drop table if exists Cliente;',
    'drop table if exists Cotizacion;',
    'SET FOREIGN_KEY_CHECKS = 1;',
    """
    create table TipoCliente(
        id int not null auto_increment,
        tipo varchar(50) not null,
        estado boolean default true,
        primary key (id)
    );
    """,
    """
    create table Mercado(
        id int not null auto_increment,
        nombre varchar(50) not null,
        codigo varchar(3) not null,
        estado boolean default true,
        primary key (id)
    );
    """,
    """
    create table Marca(
        id int not null auto_increment,
        nombre varchar(50) not null,
        codigo varchar(3) not null,
        estado boolean default true,
        primary key (id)
    );
    """,
    """
    create table Usuario(
        id int not null auto_increment,
        nombre varchar(50) not null,
        paterno varchar(20) not null,
        materno varchar(20) not null,
        admin boolean not null,
        estado boolean default true,
        primary key (id)
    );
    """,
    """
    create table Producto(
        id int not null auto_increment,
        clave varchar(50) not null,
        modelo text,
        precioCompra varchar(20),
        precioVentaMXN varchar(20),
        precioVentaUSD varchar(20),
        descuento varchar(20),
        marca varchar(50),
        descripcion text,
        primary key (id)
    );
    """,
    """
    create table Cliente(
        id int not null auto_increment,
        nombre text,
        organizacion text,
        tipo varchar(50),
        telefono varchar(50),
        email varchar(100),
        puesto varchar(50),
        industria varchar(50),
        primary key (id)
    );
    """,
    """
    create table Cotizacion(
        id int not null auto_increment,
        folio varchar(12),
        fechaCreacion varchar(50),
        marcaId int,
        moneda text,
        mercadoId int,
        version varchar(5),
        clienteId int,
        saludo text,
        producto text,
        observaciones text,
        lugarEntrega text,
        tiempoEntrega text,
        fechaCierre text,
        probabilidad text,
        primary key(id),
        unique(id),
        foreign key(marcaId) references Marca(id),
        foreign key(mercadoId) references Mercado(id),
        foreign key(clienteId) references Cliente(id)
    );
    """
    ]
