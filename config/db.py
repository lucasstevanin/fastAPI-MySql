from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://user:password@localhost/foo")
meta = MetaData()
connect = engine.connect()