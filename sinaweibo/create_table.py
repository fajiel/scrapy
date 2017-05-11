# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.engine.url import URL
import logging
from datetime import datetime

DATABASE_PLAY = {
    'drivername': 'mysql+mysqlconnector',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'Scrapy',
    'username': 'root',
    'password': '',
    'query': {
        'charset': 'utf8'
    }
	}
	
Base = declarative_base()

class Tmp(Base):
    __tablename__ = 'weibo'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    id = Column(Integer, primary_key=True)
    url = Column(String(128), nullable=False, index=True)
    title = Column(Text, nullable=False)
    image = Column(String(255))
    duration = Column(String(20))
    create_time = Column(TIMESTAMP, default=str(datetime.now()))
    update_time = Column(TIMESTAMP, default=str(datetime.now()))


def db_connect():
    return create_engine(URL(**DATABASE_PLAY), pool_size=10, pool_recycle=3600, max_overflow=20)

if __name__ =='__main__':

    logger = logging.getLogger('')
    hdlr = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

    try:
        Base.metadata.create_all(db_connect())
    except Exception:
        logging.exception('create failed')
    else:
        logging.info('created')
