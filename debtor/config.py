class Config:
    mydb_user = 'jon'
    mydb_password = 'nathanoj35'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@localhost/debtor'.format(
        mydb_user, mydb_password)
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '8882a573b6aea17c84db7e7e'
