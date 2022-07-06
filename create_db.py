import conexao

#conexao.conexao("CREATE TABLE tb_titulo (id_itulo int NOT NULL, id_forn varchar(40), ID_Autor int NOT NULL, ID_Editora int NOT NULL, Data_Pub date, Genero varchar(25), Num_Paginas int, PRIMARY KEY (ID_Livro), FOREIGN KEY (ID_Autor) REFERENCES tbl_Autor (ID_Autor));")


#CREATE TABLE tb_titulo(id_titulo serial NOT NULL, id_forn serial serial NOT NULL, venc date, CONSTRAINT tb_titulo_pkey PRIMARY KEY (id_titulo), FOREIGN KEY (id_forn) REFERENCES tb_fornecedor (id_forn));


