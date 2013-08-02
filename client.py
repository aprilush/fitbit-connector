import argparse, logging, pprint, json
from fitbit import Fitbit
from fitbit_timeseries import FitbitTimeseries
from fitbit_resources import FitbitResources

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

consumer_key = "c9c3c3541fc14f8e839b5e51d21e7011"
consumer_secret = "353a8e82be6748dc9d83fba425fe0af5"
access_token_key = "f42721b1a764eab409991c0419ba58ed"
access_token_secret = "e2fae176127c712f1e54a14da23b051b"

# fitbit = fitbit.Fitbit(consumer_key, consumer_secret)
fitbit = Fitbit(consumer_key, consumer_secret, access_token_key, access_token_secret)
if (fitbit.token == None):
		fitbit.get_token()

fitbit_resources = FitbitResources(fitbit)

pprint.pprint(fitbit_resources.get_user_info())

pprint.pprint(fitbit_resources.get_body_measurements(date='2012-03-14'))

# pprint.pprint(fitbit_resources.get_body_weight(to_date='2012-03-14'))
# pprint.pprint(fitbit_resources.get_body_weight(to_date='2012-03-14', from_date='2012-02-17'))
# pprint.pprint(fitbit_resources.get_body_weight(to_date='2012-03-14', period='1m'))

# pprint.pprint(fitbit_resources.get_body_fat(to_date='2012-03-14'))
# pprint.pprint(fitbit_resources.get_body_fat(to_date='2012-03-14', from_date='2012-02-17'))
# pprint.pprint(fitbit_resources.get_body_fat(to_date='2012-03-14', period='1m'))

# pprint.pprint(fitbit_resources.get_body_weight_goal())
# pprint.pprint(fitbit_resources.get_body_fat_goal())

# pprint.pprint(fitbit_resources.get_activities(date='2012-03-14'))
# pprint.pprint(fitbit_resources.get_activity_daily_goals())
# pprint.pprint(fitbit_resources.get_activity_weekly_goals())

# pprint.pprint(fitbit_resources.get_foods(date='2012-03-14'))
# pprint.pprint(fitbit_resources.get_water(date='2012-03-14'))
# pprint.pprint(fitbit_resources.get_food_goals())

# pprint.pprint(fitbit_resources.get_sleep(date='2012-03-14'))
# pprint.pprint(fitbit_resources.get_heart_rate(date='2012-03-14'))
# pprint.pprint(fitbit_resources.get_blood_pressure(date='2012-03-14'))
# pprint.pprint(fitbit_resources.get_glucose(date='2012-03-14'))

# get_time_series tested separately, through the helper functions in fitbit_resources_timeseries

# pprint.pprint(fitbit_resources.get_activity_stats())
# pprint.pprint(fitbit_resources.get_recent_activities())
# pprint.pprint(fitbit_resources.get_frequent_activities())
# pprint.pprint(fitbit_resources.get_favorite_activities())

# pprint.pprint(fitbit_resources.get_recent_foods())
# pprint.pprint(fitbit_resources.get_frequent_foods())
# pprint.pprint(fitbit_resources.get_favorite_foods())
# pprint.pprint(fitbit_resources.get_meals())

# pprint.pprint(fitbit_resources.get_friends())
# pprint.pprint(fitbit_resources.get_friends_leaderboard())
# pprint.pprint(fitbit_resources.get_invites()) # getting 401 Unauthorized - works in API explorer
# pprint.pprint(fitbit_resources.get_badges())

# devices = fitbit_resources.get_devices()
# pprint.pprint(devices)
# pprint.pprint(fitbit_resources.get_alarms('198353')) # getting 400 Bad request - also no longer available in the API explorer

# activities = fitbit_resources.browse_activities()
# pprint.pprint(activities)
# pprint.pprint(fitbit_resources.get_activity(activities['categories'][0]['activities'][0]['id']))

# white_bread = fitbit_resources.search_foods('white bread')
# pprint.pprint(white_bread)
# pprint.pprint(fitbit_resources.get_food(white_bread['foods'][0]['foodId']))

# pprint.pprint(fitbit_resources.get_food_units())


# fitbit_timeseries = FitbitTimeseries(fitbit)

# pprint.pprint(fitbit_timeseries.get_foods_caloriesIn())
# pprint.pprint(fitbit_timeseries.get_foods_water())

# pprint.pprint(fitbit_timeseries.get_activities_calories())
# pprint.pprint(fitbit_timeseries.get_activities_caloriesBMR())
# pprint.pprint(fitbit_timeseries.get_activities_steps())
# pprint.pprint(fitbit_timeseries.get_activities_distance())
# pprint.pprint(fitbit_timeseries.get_activities_floors())
# pprint.pprint(fitbit_timeseries.get_activities_elevation())
# pprint.pprint(fitbit_timeseries.get_activities_minutesSedentary())
# pprint.pprint(fitbit_timeseries.get_activities_minutesLightlyActive())
# pprint.pprint(fitbit_timeseries.get_activities_minutesFairlyActive())
# pprint.pprint(fitbit_timeseries.get_activities_minutesVeryActive())
# pprint.pprint(fitbit_timeseries.get_activities_activeScore())
# pprint.pprint(fitbit_timeseries.get_activities_activityCalories())

# pprint.pprint(fitbit_timeseries.get_activities_tracker_calories())
# pprint.pprint(fitbit_timeseries.get_activities_tracker_steps())
# pprint.pprint(fitbit_timeseries.get_activities_tracker_distance())
# pprint.pprint(fitbit_timeseries.get_activities_tracker_floors())
# pprint.pprint(fitbit_timeseries.get_activities_tracker_elevation())
# pprint.pprint(fitbit_timeseries.get_activities_tracker_minutesSedentary())
# pprint.pprint(fitbit_timeseries.get_activities_tracker_minutesLightlyActive())
# pprint.pprint(fitbit_timeseries.get_activities_tracker_minutesFairlyActive())
# pprint.pprint(fitbit_timeseries.get_activities_tracker_minutesVeryActive())
# pprint.pprint(fitbit_timeseries.get_activities_tracker_activeScore())
# pprint.pprint(fitbit_timeseries.get_activities_tracker_activityCalories())

# pprint.pprint(fitbit_timeseries.get_sleep_startTime())
# pprint.pprint(fitbit_timeseries.get_sleep_timeInBed())
# pprint.pprint(fitbit_timeseries.get_sleep_minutesAsleep())
# pprint.pprint(fitbit_timeseries.get_sleep_awakeningsCount())
# pprint.pprint(fitbit_timeseries.get_sleep_minutesAwake())
# pprint.pprint(fitbit_timeseries.get_sleep_minutesToFallAsleep())
# pprint.pprint(fitbit_timeseries.get_sleep_minutesAfterWakeup())
# pprint.pprint(fitbit_timeseries.get_sleep_efficiency())

# pprint.pprint(fitbit_timeseries.get_body_weight())
# pprint.pprint(fitbit_timeseries.get_body_bmi())
# pprint.pprint(fitbit_timeseries.get_body_fat())

