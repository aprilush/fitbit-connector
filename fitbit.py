import json, urllib, urllib2, urlparse, logging, cookielib, pprint
import oauth2 as oauth

class Fitbit:
      
    def __init__(self, access_token_key=None, access_token_secret=None):
        self.logger = logging.getLogger("python-fitbit-oauth")

        self.api_base_url = "http://api.fitbit.com"
        self.token = None
        if (access_token_key !=None and access_token_secret !=None):
        	self.token = oauth.Token(access_token_key, access_token_secret)

        consumer_key = "c9c3c3541fc14f8e839b5e51d21e7011"
        consumer_secret = "353a8e82be6748dc9d83fba425fe0af5"
        self.consumer = oauth.Consumer(consumer_key, consumer_secret)

    def get_token(self):
        baseurl = "https://www.fitbit.com"
        request_url = baseurl + "/oauth/request_token"
        authorize_url = baseurl + "/oauth/authorize"
        access_url = baseurl + "/oauth/access_token"
        callback_url = "http://localhost:8211/apps/fitbit/authorized"
        client = oauth.Client(self.consumer)

        resp, body = client.request(request_url, method="POST")
        if resp['status'] != '200':
            raise Exception("Invalid response getting the request token {0}.".format(resp['status']))
            sys.exit(1)

        req_token = dict(urlparse.parse_qsl(body))

        self.logger.info("Successfully got request oauth_token: {0}, oauth_token_secret: {1}".format(req_token['oauth_token'], req_token['oauth_token_secret']))

        # this interaction needs to be improved, but works for now 
        print "Go to the following link in your browser:"
        print "{0}?oauth_token={1}".format(authorize_url, req_token['oauth_token'])
        pin = raw_input('What is the PIN? ')

        token = oauth.Token(req_token['oauth_token'], req_token['oauth_token_secret'])
        token.set_verifier(pin)
        client = oauth.Client(self.consumer, token)

        resp, body = client.request(access_url, method="POST")
        if resp['status'] != '200':
            raise Exception("Invalid response getting the access token {0}.".format(resp['status']))
            sys.exit(1)
        self.token = dict(urlparse.parse_qsl(body))

        self.logger.info("Successfully got access oauth_token: {0}, oauth_token_secret: {1}".format(self.token['oauth_token'], self.token['oauth_token_secret']))
        return self.token

    def get_user_info(self, format='json'):
        url = "{0}/1/user/-/profile.{1}".format(self.api_base_url, format)
        req = oauth.Request.from_consumer_and_token(consumer=self.consumer, token=self.token, http_method="GET", http_url=url)
        sig_method = oauth.SignatureMethod_HMAC_SHA1()
        req.sign_request(sig_method, self.consumer, self.token)
        headers = req.to_header()

        req = urllib2.Request(url)
        req.get_method = lambda: "GET"
        req.add_header('Authorization', headers['Authorization'])
        resp = urllib2.urlopen(req)
        data = resp.read()
        return data

    def get_food_units(self, format='json'):
        url = "{0}/1/foods/units.{1}".format(self.api_base_url, format)
        req = oauth.Request.from_consumer_and_token(consumer=self.consumer, token=self.token, http_method="GET", http_url=url)
        sig_method = oauth.SignatureMethod_HMAC_SHA1()
        req.sign_request(sig_method, self.consumer, self.token)
        headers = req.to_header()

        req = urllib2.Request(url)
        req.get_method = lambda: "GET"
        req.add_header('Authorization', headers['Authorization'])
        resp = urllib2.urlopen(req)
        data = resp.read()
        return data

