from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://qkjnfoxo:BwlpSiaSYT8SwlbPdESGn8IkB6r_1Mad@mouse.db.elephantsql.com/qkjnfoxo')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()