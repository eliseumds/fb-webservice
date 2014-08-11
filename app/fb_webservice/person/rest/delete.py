from ..model import Person
from fb_webservice.log import log
import tornado

__all__ = ['Handler']

class Handler(tornado.web.RequestHandler):
    def delete(self,facebook_id):
        try:
            Person.delete().where(Person.id == facebook_id).execute()
            self.set_status(204)
        except:
            self.set_status(500)

        self.finish()
