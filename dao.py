class ClienteDao:
    def find_all(self):
        from database import Database

        conn = Database.get_connection()
        res = conn.execute("""
            SELECT * FROM cliente
        """
                           )
        print(res.fetchall())


if __name__ == '__main__':
    dc = ClienteDao()
    dc.find_all()
