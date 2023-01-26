from database import Database
from entidades import Cliente, Produto


class FavoritoDao:
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
