import simplejson
import sys
from tornado.options import define,options
from tornado.testing import AsyncHTTPTestCase,main
from tornado.web import Application
from unittest import TestLoader
from fb_webservice.routes import routes
from fb_webservice.person.model import Person

class PersonTest(AsyncHTTPTestCase):
    facebook_id = '1510993915'
    facebook_id_2 = '100000157318644'

    @classmethod
    def setUpClass(self):
        Person.delete().execute()

    def get_app(self):
        return Application(routes,debug=options.debug)

    def test_1_nonexistent_facebook_id(self):
        self.http_client.fetch(self.get_url('/person'), self.stop,
                               method='POST',
                               body='facebookId=__nonexistent__')
        response = self.wait()
        assert response.code == 500

    def test_2_creation(self):
        self.http_client.fetch(self.get_url('/person'), self.stop,
                               method='POST',
                               body='facebookId=%s' % self.facebook_id)
        response = self.wait()
        assert response.code == 201

    def test_2_creation_2(self):
        self.http_client.fetch(self.get_url('/person'), self.stop,
                               method='POST',
                               body='facebookId=%s' % self.facebook_id_2)
        response = self.wait()
        assert response.code == 201

    def test_3_listing(self):
        self.http_client.fetch(self.get_url('/person'), self.stop)
        response = self.wait()
        assert response.code == 200
        assert len(simplejson.loads(response.body)) == 2

    def test_3_listing_with_limit(self):
        self.http_client.fetch(self.get_url('/person?limit=1'), self.stop)
        response = self.wait()
        assert response.code == 200
        assert len(simplejson.loads(response.body)) == 1

    def test_4_already_created(self):
        self.http_client.fetch(self.get_url('/person'), self.stop,
                               method='POST',
                               body='facebookId=%s' % self.facebook_id)
        response = self.wait()
        assert response.code == 409

    def test_5_delete(self):
        self.http_client.fetch(self.get_url('/person/%s' % self.facebook_id), self.stop,
                               method='DELETE')
        response = self.wait()
        assert response.code == 204

    def test_6_listing_again(self):
        self.http_client.fetch(self.get_url('/person'), self.stop)
        response = self.wait()
        assert response.code == 200
        assert len(simplejson.loads(response.body)) == 1

    def test_7_delete_2(self):
        self.http_client.fetch(self.get_url('/person/%s' % self.facebook_id_2), self.stop,
                               method='DELETE')
        response = self.wait()
        assert response.code == 204

    def test_8_listing_nothing(self):
        self.http_client.fetch(self.get_url('/person'), self.stop)
        response = self.wait()
        assert response.code == 200
        assert len(simplejson.loads(response.body)) == 0

def all():
    return TestLoader().loadTestsFromModule(sys.modules[__name__])

if __name__ == '__main__':
    main()
