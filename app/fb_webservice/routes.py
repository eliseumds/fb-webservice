import fb_webservice
from fb_webservice import person

__all__ = ['routes']

routes = [(r'/person',fb_webservice.person.rest.main.Handler),
          (r'/person/(.*)',fb_webservice.person.rest.delete.Handler)]
