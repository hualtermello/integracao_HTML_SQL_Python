create schema cadastro;
use cadastro;

create table cliente(
cpf varchar(11) not null primary key,
primeiro_nome varchar(50) not null,
sobrenome varchar(50) not null,
idade int not null
);


select * from cliente;




