from sqlalchemy import create_engine, Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection
    Returns sqlalchemy engine instance
    """
    return create_engine("postgresql://postgres:Gatsby@localhost:5432/test", echo=True)


engine = db_connect()    
    
# Session = sessionmaker(bind=db_connect())

Session = sessionmaker(bind=engine)

session = Session()

class User(DeclarativeBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                self.name, self.fullname, self.password)
                
DeclarativeBase.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

session.add(ed_user)

session.commit()

session = Session()

getit = session.query(User).first()

print(getit)