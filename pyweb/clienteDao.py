from database import Database
from entidades import Cliente


class ClienteDao:
    def find_all(self):
        conn = Database.get_connection()
        res = conn.execute("""
        SELECT id, nome, cpf, cep, email, data_cadastro FROM cliente
        """
                           )
        results = res.fetchall()
        results = [
            {
                "id": cliente[0],
                "nome": cliente[1],
                "cpf": cliente[2],
                "cep": cliente[3],
                "email": cliente[4],
                "data_cadastro": cliente[5],
            } for cliente in results]

        conn.close()
        return results

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

    def save(self, cliente):
        # obtem uma conexao com o banco:
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO cliente (
                nome, cpf, cep, email            
            ) VALUES (?, ?, ?, ?)
            """,
            (
                cliente.nome,
                cliente.cpf,
                cliente.cep,
                cliente.email,
            )
        )
        conn.commit()
        conn.close()

    def update(self, cliente):
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE cliente SET nome = ?, cpf = ?, cep = ?, email = ?
            WHERE id = ?
            """,
            (
                cliente.nome,
                cliente.cpf,
                cliente.cep,
                cliente.email,
                cliente.id
            )
        )
        conn.commit()
        conn.close()

    def delete(self, id):
        conn = Database.get_connection()
        conn.execute(
            f"""
            DELETE FROM cliente WHERE id = {id}
            """
        )
        conn.commit()
        conn.close()

    def get_cliente(self, id):
        conn = Database.get_connection()
        res = conn.execute(f"""
        SELECT id, nome, email, cpf, cep, data_cadastro  FROM cliente WHERE id = {id}
        """
                           )
        row = res.fetchone()

        cliente = Cliente(
            nome=row[1],
            email=row[2],
            id=row[0],
            cpf=row[3],
            cep=row[4],
            data_cadastro=row[5]
        )
        conn.close()
        return cliente
