# coding=utf-8

from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#  Create base for base
Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:''@localhost:3306/Scrapy?charset=utf8', echo=False)


class WeiBo(Base):
    __tablename__ = 'weibo'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    #  table schema
    id = Column(Integer, primary_key=True)
    url = Column(String(128), nullable=False, index=True)
    title = Column(Text, nullable=False, doc=u'标题')
    image = Column(String(255))
    duration = Column(String(20), doc=u'节目时长')
    create_time = Column(TIMESTAMP, nullable=False, default=str(datetime.now()))
    update_time = Column(TIMESTAMP, nullable=False, onupdate=str(datetime.now()))
