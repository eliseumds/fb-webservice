from ..model import Person
from fb_webservice.log import log
import simplejson
import tornado
from tornado import httpclient

__all__ = ['Handler']

class Handler(tornado.web.RequestHandler):
    def get(self):
        result = []

        try:
            limit = int(self.get_query_argument('limit'))
        except:
            limit = -1

        for item in Person.select().limit(limit).dicts():
            result.append(item)

        self.write(simplejson.dumps(result))

    def post(self):
        facebook_id = self.get_body_argument('facebookId')
        http_client = httpclient.HTTPClient()
        url = 'https://graph.facebook.com/%s' % facebook_id

        try:
            response = http_client.fetch(url)
            assert self.save(simplejson.loads(response.body))
            log.info('Person created',arguments=response.body)
            self.set_status(201)
        except httpclient.HTTPError, e:
            log.warn('Facebook request error: %s' % url)
            self.set_status(500)
        except AssertionError:
            log.warn('Person already created: %s' % facebook_id)
            self.set_status(409)
        except:
            self.set_status(500)

        self.finish()

    def save(self,data):
        try:
            Person.get(id=data['id'])
            return False
        except:
            pass

        Person.create(id=data['id'],
                      first_name=data['first_name'],
                      last_name=data['last_name'],
                      gender=data['gender'],
                      locale=data['locale'],
                      name=data['name'],
                      username=data['username'])
        return True
