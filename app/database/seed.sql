-- script para popular o banco

INSERT INTO tb_laboratory (laboratory_id, name, description) VALUES
(1, 'LAAI', 'Laboratório de Inteligência Artificial Aplicada. Linhas de pesquisa: Metaheurísticas aplicadas a problemas de otimização combinatória, Inteligência artificial distribuída em sistemas multiagentes, Desenvolvimento de algoritmos inteligentes para sistemas elétricos de distribuição e smart grids.'),
(2, 'LABES', 'Laboratório de Engenharia de Software. Linhas de pesquisa: Engenharia de Software, Melhoria do Processo de Software, Modelo MPS-BR Software, Desenvolvimento de Software, Inovação, Qualidade de Software, IA aplicada a processos de software, Computer Supported Collaborative Work (CSCW), Engenharia de Software Empírica, Engenharia de Software Colaborativa.'),
(3, 'LABSC', 'Laboratório de Segurança e Criptografia Aplicada. Linhas de pesquisa: Segurança Computacional, Protocolos Criptográficos, Votação Digital Segura, Segurança de Redes, Privacidade.'),
(4, 'LABIOCAD', 'Laboratório de Bioinformática e Computação de Alto Desempenho. Linhas de pesquisa: Computação de Alto Desempenho, Programação Paralela, Bioinformática, Biologia Computacional, Computação Forense, Inteligência Artificial.'),
(5, 'GERCOM', 'Laboratório de Redes de Computadores e Comunicação Multimídia. Linhas de pesquisa: Internet do Futuro, Redes Definidas por Software, Internet das Coisas, Redes Centradas em Informação, Tecnologias de Computação em Nuvem, Redes sem Fio, Blockchain/Tecnologia de registro distribuídos.'),
(6, 'HIT', 'Laboratório de Interação Humano-Tecnologia. Linhas de pesquisa: Banco de Dados, Informática na Educação, Mineração de dados, Voz, Acessibilidade, Engenharia Semiótica, Interação Humano-Computador, Tecnologias Assistivas.'),
(7, 'LID', 'Laboratório de Inteligência de Dados. Linhas de pesquisa: Inteligência Artificial, Análise de Dados, Sistemas Inteligentes Baseados em Aprendizado de Máquina, Ciência de Dados, Visualização da Informação, Mineração de Dados, Heurísticas, Metaheurísticas, Otimização Multimodal.'),
(8, 'SPIDER', 'Laboratório de Melhoria de Processos de Software: Desenvolvimento e Pesquisa. Linhas de pesquisa: Qualidade de Software, Melhoria Contínua, Processos de Desenvolvimento de Software, Modelos e Normas de Qualidade, Ferramentas de Software Livre, Revisão Sistemática.'),
(9, 'LACIS', 'Laboratório de Cidades Inteligentes e Sustentáveis. Linhas de pesquisa: Disseminação de Dados, Computação em Nuvem e Névoa, Análise de Dados, Cidades Inteligente, Mobilidade, Comunicação sem fio.');

INSERT INTO tb_researcher (researcher_id, name, email, laboratory_id) VALUES
	-- laai
	(1, 'Dr. Dionne Cavalcante Monteiro', 'dionne@ufpa.br', 1),
    (2, 'Dr. Filipe de Oliveira Saraiva', 'saraiva@ufpa.br', 1),
    (3, 'Dr. Lídio Campos', 'lidio@ufpa.br', 1),
    (4, 'Dr. Raimundo Viégas Junior', 'rviegas@ufpa.br', 1),
    -- labes
    (5, 'Dra. Carla Alessandra Lima Reis', 'lima@ufpa.br', 2),
    (6, 'Dr. Cledson Ronald Botelho de Souza', 'cdesouza@ufpa.br', 2),
    (7, 'Dr. Gustavo Henrique Lima Pinto', 'gpinto@ufpa.br', 2),
    (8, 'Dr. Rodrigo Quites Reis', 'quites@ufpa.br', 2),
    (9, 'Dr. Victor Hugo Santiago Costa Pinto', 'victor.santiago@ufpa.br', 2),
    -- labsc
    (10, 'Dr. Renato Hidaka Torres', 'renatohidaka@ufpa.br', 3),
    (11, 'Dr. Roberto Samarone dos Santos Araújo', 'rsa@ufpa.br', 3),
    -- labiocad
    (12, 'Dr. Josivaldo de Souza Araújo', 'josivaldo@ufpa.br', 4),
    (13, 'Dra. Regiane Silva Kawasaki Frances', 'kawasaki@ufpa.br', 4),
    (14, 'Dr. Vinícius Augusto Carvalho de Abreu', 'vabreu@ufpa.br', 4),
    -- gercom
    (15, 'Dr. André Figueira Riker', 'ariker@ufpa.br', 5),
    (16, 'Dr. Antônio Jorge Gomes Abelém', 'abelem@ufpa.br', 5),
    (17, 'Dr. Denis Lima do Rosário', 'denis@ufpa.br', 5),
    (18, 'Dr. Eduardo Coelho Cerqueira', 'cerqueira.ufpa@gmail.com', 5),
    -- hit
    (19, 'Drª. Fabíola Pantoja Oliveira Araújo', 'fpoliveira@ufpa.br', 6),
    (20, 'Drª. Marcelle Pereira Mota', 'mpmota@ufpa.br', 6),
    -- lid
    (21, 'Dr. Adam Dreyton Ferreira dos Santos', 'adamdreyton@unifesspa.edu.br', 7),
    (22, 'Dr. Claudomiro de Souza de Sales Junior', 'cssj@ufpa.br', 7),
    (23, 'Dr. Fabricio Rossy de Lima Lobato', 'fbarros@ufpa.br', 7),
    (24, 'Dr. Joao Crisóstomo Weyl Albuquerque Costa', 'jweyl@ufpa.br', 7),
    (25, 'Dr. Moisés Felipe Mello Da Silva', 'moises.silva@icen.ufpa.br', 7),
    (26, 'Dr. Reginaldo Cordeiro dos Santos Filho', 'regicsf@ufpa.br', 7),
    -- spider
    (27, 'Dr. Alexandre Marcos Lins de Vasconcelos', 'amlv@cin.ufpe.br', 8),
    (28, 'Dr. Sandro Ronaldo Bezerra Oliveira', 'srbo@ufpa.br', 8),
    (29, 'Drª. Ana Cristina Rouiller', 'anarouiller@gmail.com', 8),
    -- lacis
    (30, 'Dr. Denis Lima do Rosário', 'denis@ufpa.br', 9),
    (31, 'Dr. Eduardo Coelho Cerqueira', 'cerqueira.ufpa@gmail.com', 9),
    (32, 'Dr. Helder May Nunes da Silva Oliveira', 'heldermay@ufpa.br', 9);

INSERT INTO tb_student (student_id, degree, registration, name) VALUES
    (1, 'Sistemas de Informação', '202311140049', 'Rebeca Mendonça'),
    (2, 'Sistemas de Informação', '202311140048', 'Danilo Chaves'),
    (3, 'Sistemas de Informação', '202411140007', 'Kael Carvalho'),
    (4, 'Sistemas de Informação', '202411140008', 'Isaque Costa')