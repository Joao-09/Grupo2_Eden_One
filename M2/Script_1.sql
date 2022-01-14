drop database if exists EDEN_ONE;

CREATE DATABASE if not exists EDEN_ONE;

use EDEN_ONE;

create table if not exists personajes (
id_personajes INT,
name varchar(20),
descripcion varchar(50),
fechacreacion varchar(30),
usuariocreacion varchar(30),
fechamodificacion varchar(30),
usuariomodificacion varchar(30)
);

create table if not exists aventura (
id_aventura INT,
name varchar(20),
descripcion varchar(50),
fechacreacion varchar(30),
usuariocreacion varchar(30),
fechamodificacion varchar(30),
usuariomodificacion varchar(30)
);

create table if not exists paso (
id_paso INT,
name varchar(20),
descripcion varchar(50),
fechacreacion varchar(30),
usuariocreacion varchar(30),
fechamodificacion varchar(30),
usuariomodificacion varchar(30)
);


create table if not exists respuesta (
id_respuesta INT,
name varchar(20),
descripcion varchar(50),
fechacreacion varchar(30),
usuariocreacion varchar(30),
fechamodificacion varchar(30),
usuariomodificacion varchar(30)
);

create table if not exists usuario (
id_usuario INT,
username varchar(30),
passsword varchar(30),
fechacreacion varchar(30),
usuariocreacion varchar(30),
fechamodificacion varchar(30),
usuariomodificacion varchar(30)
);

create table if not exists opciones (
id_opciones INT,
name varchar(20),
descripcion varchar(50),
fechacreacion varchar(30),
usuariocreacion varchar(30),
fechamodificacion varchar(30),
usuariomodificacion varchar(30)
);

create table if not exists partidas (
id_partidas INT,
name varchar(20),
numeropartidas INT,
fechacreacion varchar(30),
usuariocreacion varchar(30),
fechamodificacion varchar(30),
usuariomodificacion varchar(30)
);