Base = declarative_base()


class Conn(object):
    def __init__(self):
        self.session = None

    def connect(self):
        db_url = "postgresql://postgres:xxxxx@localhost/xxx"
        engine = create_engine(db_url, echo=False)

        Base.metadata.create_all(bind=engine)

        Session = sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()
        print db_url

    def close(self):
        self.session.close()

if __name__ == '__main__':
    db = Conn()
    db.connect()
    db.close()
