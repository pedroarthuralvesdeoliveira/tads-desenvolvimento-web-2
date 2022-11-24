class ClienteDao:
    def find_all(self):
        from database import Database
        conn = Database.get_connection()
        res = conn.execute("""
            SELECT * FROM cliente
        """
                           )
        print(res.fetchall())

    def insert(self, cliente):
        from database import Database
        conn = Database.get_connection()
        conn.execute(
            """
            INSERT INTO cliente (nome, cpf, cep, email) VALUES (?, ?, ?, ?)
            """,
            (
                cliente.nome,
                cliente.cpf,
                cliente.cep,
                cliente.email
            )
        )
        conn.commit()
