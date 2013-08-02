import json, urllib, urllib2, urlparse, logging, cookielib, pprint
from datetime import date
import oauth2 as oauth

# TODO add an accept-language header to set the measurement units to us or metric
class Fitbit:
      
    def __init__(self, consumer_key, consumer_secret, access_token_key=None, access_token_secret=None):
        self.logger = logging.getLogger("fitbit")

        self.api_base_url = "http://api.fitbit.com"

        self.consumer = oauth.Consumer(consumer_key, consumer_secret)

        self.token = None
        if (access_token_key !=None and access_token_secret !=None):
            self.token = oauth.Token(access_token_key, access_token_secret)

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

    def call_get_api(self, url):
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

    def get_time_series(self, resource_path, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        # from_date and to_date in the format yyyy-MM-dd
        # period can be one of {1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, max}
        # to_date takes precedence over period, if both are given
        # use fitbit_timeseries helper functions for a list of possible resource paths
        if (from_date == None):
            url = "{0}/1/user/-/{1}/date/{2}/{3}.{4}".format(self.api_base_url, resource_path, to_date, period, format)
        else:
            url = "{0}/1/user/-/{1}/date/{2}/{3}.{4}".format(self.api_base_url, resource_path, from_date, to_date, format)
        data = self.call_get_api(url)
        return json.loads(data)
        return
