from tornado.options import options
from fb_webservice.log.model import Log
import simplejson

for item in Log.select().order_by(Log.date.desc()):
    print '[%s-%s] %s' % (item.type,item.date,item.text)

    if item.arguments != 'null':
        print '\t', simplejson.loads(item.arguments)
