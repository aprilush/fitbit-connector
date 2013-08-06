import argparse, logging, pprint, json
from datetime import datetime, date, time
from fitbit import Fitbit
from fitbit_timeseries import FitbitTimeseries
from fitbit_resources import FitbitResources
from fitbit_intraday import FitbitIntraDay

""" A simple command-line client to demontrate usage of the library. """

parser = argparse.ArgumentParser(description = "Use the Fitbit API")
parser.add_argument('--date', default = '2012-03-02', type = str, help = "Start date, like: 2012-03-02")
parser.add_argument('--debug', default = False, action="store_true", help = "Turn on verbose debugging")

args = vars(parser.parse_args())

if args['debug']:
    logging.basicConfig(level = logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

consumer_key = "add_your_consumer_key_here"
consumer_secret = "add_your_consumer_secret_here"
access_token_key = "add_your_token_key_here"
access_token_secret = "add_your_token_secret_here"

fitbit = Fitbit(consumer_key, consumer_secret)
# fitbit = Fitbit(consumer_key, consumer_secret, access_token_key, access_token_secret)
if (fitbit.token == None):
	fitbit.get_token()

if args['date']:
	day = datetime.strptime(args['date'], '%Y-%m-%d').date()
else:
	day = date.today()

fitbit_res = FitbitResources(fitbit)

print '\nget user info:\n'
pprint.pprint(fitbit_res.get_user_info())
print '\nget body measurements:\n'
pprint.pprint(fitbit_res.get_body_measurements(day))
print '\nget activities:\n'
pprint.pprint(fitbit_res.get_activities(day))

fitbit_ts = FitbitTimeseries(fitbit)

print '\nget activities steps:\n'
pprint.pprint(fitbit_ts.get_activities_steps())
print '\nget activities distance:\n'
pprint.pprint(fitbit_ts.get_activities_distance())

print '\nget activities tracker steps:\n'
pprint.pprint(fitbit_ts.get_activities_tracker_steps())
print '\nget activities tracker distance:\n'
pprint.pprint(fitbit_ts.get_activities_tracker_distance())

print '\nget body weight:\n'
pprint.pprint(fitbit_ts.get_body_weight())

fitbit_id = FitbitIntraDay(fitbit)

pprint.pprint(fitbit_id.get_steps(datetime.combine(day, time(12,0)), datetime.combine(day, time(17,15))))
