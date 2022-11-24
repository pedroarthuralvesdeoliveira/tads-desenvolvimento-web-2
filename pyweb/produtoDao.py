from database import Database


class ProdutoDao:
    def find_all(self):
        conn = Database.get_connection()
        res = conn.execute("""
            SELECT * FROM produto
        """
                           )
        print(res.fetchall())

    def insert(self, produto):
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
        self.conn.commit()
