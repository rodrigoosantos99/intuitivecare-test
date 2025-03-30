SELECT 
    oa.razao_social AS operadora,
    SUM(d4.vl_saldo_final) AS total_despesas
FROM despesas_4t_2024 d4
JOIN operadoras_ativas oa ON d4.reg_ans = oa.registro_ans
WHERE d4.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
GROUP BY oa.razao_social
ORDER BY total_despesas DESC
LIMIT 10;


