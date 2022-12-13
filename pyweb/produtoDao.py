from database import Database
from entidades import Produto


class ProdutoDao:
    def find_all(self):
        conn = Database.get_connection()
        res = conn.execute("""
        SELECT id, nome, categoria FROM produto
        """
                           )
        results = res.fetchall()
        results = [
            {
                "id": produto[0],
                "nome": produto[1],
                "categoria": produto[2],
            } for produto in results]

        conn.close()
        return results

    def insert(self, produto):
        from database import Database
        conn = Database.get_connection()
        conn.execute(
            """
            INSERT INTO produto (nome, categoria) VALUES (?, ?)
            """,
            (
                produto.nome,
                produto.categoria
            )
        )
        conn.commit()

    def save(self, produto):
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO produto (
                nome, cpf          
            ) VALUES (?, ?)
            """,
            (
                produto.nome,
                produto.categoria
            )
        )
        conn.commit()
        conn.close()

    def update(self, produto):
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE produto SET nome = ?, categoria = ?
            WHERE id = ?
            """,
            (
                produto.nome,
                produto.categoria
            )
        )
        conn.commit()
        conn.close()

    def delete(self, id):
        conn = Database.get_connection()
        conn.execute(
            f"""
            DELETE FROM produto WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()

    def get_produto(self, id):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT id, nome, categoria  FROM produto WHERE id = {id}
        """
                           )
        row = res.fetchone()

        produto = Produto(
            categoria=row[2],
            id=row[0],
            nome=row[1]
        )
        conn.close()
        return produto
