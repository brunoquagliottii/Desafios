import re

import pandas as pd
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'banco_filmes'
}

def criar_banco():
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Filmes(
                id INT AUTO_INCREMENT,
                nome VARCHAR(255),
                ano INT,
                genero VARCHAR(255),
                PRIMARY KEY (id)
            )
        """)

        df = pd.read_csv('movie.csv', delimiter=',', quotechar='"')
        batch_size = 100
        num_batches = len(df) // batch_size + (1 if len(df) % batch_size > 0 else 0)

        for i in range(num_batches):
            batch = df.iloc[i*batch_size:(i+1)*batch_size]

            filmes = []
            for _, row in batch.iterrows():
                titulo = row['title']
                ano_str = re.search(r'\((\d{4})\)', titulo)
                ano = int(ano_str.group(1)) if ano_str is not None else None
                generos = row['genres']

                filme = {
                    'nome': titulo[:-7],
                    'ano': ano,
                    'genero': generos
                }

                filmes.append(filme)

            cursor.executemany("""
                INSERT INTO Filmes (nome, ano, genero) 
                VALUES (%(nome)s, %(ano)s, %(genero)s)
            """, filmes)

        conn.commit()

def buscar_nome_filme(filme):
    with mysql.connector.connect(**db_config) as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT nome, ano, genero FROM Filmes WHERE nome LIKE %s
            """, (filme,))
            results = cursor.fetchall()
            filmes = []
            for row in results:
                filme = {}
                filme['nome'] = row[0]
                filme['ano'] = row[1]
                filme['genero'] = row[2]
                filmes.append(filme)
            return filmes

def apagar_table():
    with mysql.connector.connect(**db_config) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            DROP TABLE Filmes
        """)