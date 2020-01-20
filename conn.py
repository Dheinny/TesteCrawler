import sqlalchemy as db

class Conn:
    config = {
        'host': "db",
        'port': 3306,
        "user": "user",
        "password": "userpassword",
        "database": "app_crawler"
    }

    @staticmethod
    def get_url():
        db_user = Conn.config.get("user")
        db_pwd = Conn.config.get("password")
        db_host = Conn.config.get("host")
        db_port = Conn.config.get("port")
        db_name = Conn.config.get("database")

        conn_url = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'

        return conn_url

#engine = db.create_engine(conn_str)
#conn = engine.connect()

 # metadata = db.MetaData(bind=engine)
# metadata.reflect(only=['test_table'])
#
# test_table = metadata.tables['test_table']

# print(conn)