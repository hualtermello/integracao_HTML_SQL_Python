use cadastro;
select * from produtos;
create table produtos(
cod_produto int auto_increment primary key not null,
nome_produto varchar(50) not null,
descricao varchar(50) not null,
preco int not null
);