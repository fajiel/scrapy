# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from db_manage import sessionmaker, WeiBo, engine
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class SinaweiboPipeline(object):
    def process_item(self, item, spider):
        query = session.query(WeiBo)
        result = query.filter_by(title=item['title']).first()
        if result is None:
            result = WeiBo()
            result.url = item['url']
            result.title = item['title']
            result.image = item['image']
            result.duration = item['duration']
            session.add(result)
        else:
            return item
        session.commit()
        return item


