COPY despesas_2023
FROM 'C:\PostgreSQL\Uploads\despesas_2023.csv'
WITH (FORMAT csv, DELIMITER ';', HEADER TRUE, ENCODING 'UTF8');

COPY despesas_1t_2024
FROM 'C:\PostgreSQL\Uploads\1T2024.csv'
WITH (FORMAT csv, DELIMITER ';', HEADER TRUE, ENCODING 'UTF8');

COPY despesas_2t_2024
FROM 'C:\PostgreSQL\Uploads\2T2024.csv'
WITH (FORMAT csv, DELIMITER ';', HEADER TRUE, ENCODING 'UTF8');

COPY despesas_3t_2024
FROM 'C:\PostgreSQL\Uploads\3T2024.csv'
WITH (FORMAT csv, DELIMITER ';', HEADER TRUE, ENCODING 'UTF8');

COPY despesas_4t_2024
FROM 'C:\PostgreSQL\Uploads\4T2024.csv'
WITH (FORMAT csv, DELIMITER ';', HEADER TRUE, ENCODING 'UTF8');

COPY operadoras_ativas
FROM 'C:\PostgreSQL\Uploads\Relatorio_cadop.csv'
WITH (FORMAT csv, DELIMITER ';', HEADER TRUE, ENCODING 'UTF8');
