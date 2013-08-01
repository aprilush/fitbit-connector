import argparse, logging, pprint, json
from fitbit import Fitbit

""" A simple command-line client to demontrate usage of the library. """

parser = argparse.ArgumentParser(description = "Use the Fitbit API")
# parser.add_argument('start_date', type = str, help = "Start date, like: 2013-03-20")
# parser.add_argument('end_date', type = str, help = "End date, like: 2013-03-21")
parser.add_argument('--debug', default = False, action="store_true", help = "Turn on verbose debugging")

args = vars(parser.parse_args())

if args['debug']:
    logging.basicConfig(level = logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

fitbit = fitbit.Fitbit()
if (fitbit.token == None):
		fitbit.get_token()
pprint.pprint(json.loads(fitbit.get_user_info()))

