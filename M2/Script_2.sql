ALTER TABLE personajes modify id_personajes INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
Alter table personajes modify name varchar(30) NOT NULL UNIQUE;
Alter table personajes modify descripcion varchar(30) NOT NULL;
Alter table personajes modify fechacreacion varchar(30) NOT NULL;
Alter table personajes modify usuariocreacion varchar(30) NOT NULL;
Alter table personajes modify fechamodificacion varchar(30) NULL;
Alter table personajes modify usuariomodificacion varchar(30) NULL;

ALTER TABLE aventura modify id_aventura INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
Alter table aventura modify name varchar(30) NOT NULL;
Alter table aventura modify descripcion varchar(30) NOT NULL;
Alter table aventura modify fechacreacion varchar(30) NOT NULL;
Alter table aventura modify usuariocreacion varchar(30) NOT NULL;
Alter table aventura modify fechamodificacion varchar(30) NULL;
Alter table aventura modify usuariomodificacion varchar(30) NULL;

ALTER TABLE paso modify id_paso INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
Alter table paso modify name varchar(30) NOT NULL;
Alter table paso modify descripcion varchar(30) NOT NULL;
Alter table paso modify fechacreacion varchar(30) NOT NULL;
Alter table paso modify usuariocreacion varchar(30) NOT NULL;
Alter table paso modify fechamodificacion varchar(30) NULL;
Alter table paso modify usuariomodificacion varchar(30) NULL;

ALTER TABLE respuesta modify id_respuesta INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
Alter table respuesta modify name varchar(30) NOT NULL;
Alter table respuesta modify descripcion varchar(30) NOT NULL;
Alter table respuesta modify fechacreacion varchar(30) NOT NULL;
Alter table respuesta modify usuariocreacion varchar(30) NOT NULL;
Alter table respuesta modify fechamodificacion varchar(30) NULL;
Alter table respuesta modify usuariomodificacion varchar(30) NULL;

ALTER TABLE personajes modify id_personajes INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
Alter table personajes modify name varchar(30);
Alter table personajes modify descripcion varchar(30);
Alter table personajes modify fechacreacion varchar(30) NOT NULL;
Alter table personajes modify usuariocreacion varchar(30) NOT NULL;
Alter table personajes modify fechamodificacion varchar(30) NULL;
Alter table personajes modify usuariomodificacion varchar(30) NULL;

ALTER TABLE usuario modify id_usuario INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
Alter table usuario modify username varchar(30) NOT NULL UNIQUE;
Alter table usuario modify passsword varchar(30) NOT NULL;
Alter table usuario modify fechacreacion varchar(30) NOT NULL;
Alter table usuario modify usuariocreacion varchar(30) NOT NULL;
Alter table usuario modify fechamodificacion varchar(30) NULL;
Alter table usuario modify usuariomodificacion varchar(30) NULL;


ALTER TABLE partidas modify id_partidas INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
Alter table partidas modify name varchar(30) NOT NULL;
Alter table partidas modify numeropartidas INT NOT NULL;
Alter table partidas modify fechacreacion varchar(30) NOT NULL;
Alter table partidas modify usuariocreacion varchar(30) NOT NULL;
Alter table partidas modify fechamodificacion varchar(30) NULL;
Alter table partidas modify usuariomodificacion varchar(30) NULL;




