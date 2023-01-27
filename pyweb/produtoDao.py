import csv
from database import Database
from entidades import Produto


class ProdutoDao:
    def busca_produto(self, nome):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT id, nome, categoria, preco  FROM produto WHERE nome LIKE '%{nome}%'
        """
                           )
        produtos = res.fetchall()
        produtos = [
            {
                "id": produto[0],
                "nome": produto[1],
                "categoria": produto[2],
                "preco": produto[3]
            } for produto in produtos]

        conn.close()
        return produtos

    def delete(self, id):
        conn = Database.get_connection()
        conn.execute(
            f"""
            DELETE FROM produto WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()

    def favoritar(self, id):
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO favoritos (
                clienteID, produtoID          
            ) VALUES (?, ?)
            """,
            (
                1,
                id
            )
        )
        conn.commit()
        conn.close()

    def find_all(self):
        conn = Database.get_connection()
        res = conn.execute("""
        SELECT id, nome, categoria, preco FROM produto
        """
                           )
        results = res.fetchall()
        results = [
            {
                "id": produto[0],
                "nome": produto[1],
                "categoria": produto[2],
                "preco": produto[3]
            } for produto in results]

        conn.close()
        return results

    def get_produto(self, id):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT id, nome, categoria, preco  FROM produto WHERE id = {id}
        """
                           )
        row = res.fetchone()

        produto = Produto(
            categoria=row[2],
            id=row[0],
            nome=row[1],
            preco=row[3]
        )
        conn.close()
        return produto

    def import_csv(self):
        dao = ProdutoDao()
        with open('lista-500.csv', encoding='utf-8') as arquivo_referencia:
            tabela = csv.reader(arquivo_referencia, delimiter=',')
            for item in tabela:
                nome = item[1]
                categoria = item[2]
                preco = item[3]
                produto = Produto(nome, categoria, preco)

                dao.save(produto)

    def remover_favorito(self, id):
        conn = Database.get_connection()
        conn.execute(
            f"""
            DELETE FROM 
                favoritos 
            WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()

    def save(self, produto):
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO produto (
                nome, categoria, preco          
            ) VALUES (?, ?, ?)
            """,
            (
                produto.nome,
                produto.categoria,
                produto.preco
            )
        )
        conn.commit()
        conn.close()

    def update(self, produto):
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE produto SET nome = ?, categoria = ?, preco = ?
            WHERE id = ?
            """,
            (
                produto.nome,
                produto.categoria,
                produto.preco,
                produto.id
            )
        )
        conn.commit()
        conn.close()
