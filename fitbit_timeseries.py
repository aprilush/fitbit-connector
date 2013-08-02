from fitbit import Fitbit
from datetime import date

class FitbitTimeseries():

    def __init__(self, fitbit):
        self.fitbit = fitbit;
        if (self.fitbit.token == None):
            self.fitbit.get_token()

    # foods/log/caloriesIn
    def get_foods_caloriesIn(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='foods/log/caloriesIn', to_date=to_date, from_date=from_date, period=period, format=format)

    # foods/log/water
    def get_foods_water(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='foods/log/water', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/calories
    def get_activities_calories(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/calories', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/caloriesBMR
    def get_activities_caloriesBMR(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/caloriesBMR', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/steps
    def get_activities_steps(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/steps', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/distance
    def get_activities_distance(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/distance', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/floors
    def get_activities_floors(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/floors', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/elevation
    def get_activities_elevation(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/elevation', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/minutesSedentary
    def get_activities_minutesSedentary(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/minutesSedentary', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/minutesLightlyActive    
    def get_activities_minutesLightlyActive(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/minutesLightlyActive', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/minutesFairlyActive
    def get_activities_minutesFairlyActive(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/minutesFairlyActive', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/minutesVeryActive
    def get_activities_minutesVeryActive(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/minutesVeryActive', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/activeScore
    def get_activities_activeScore(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/activeScore', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/activityCalories
    def get_activities_activityCalories(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/activityCalories', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/tracker/calories
    def get_activities_tracker_calories(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/tracker/calories', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/tracker/steps
    def get_activities_tracker_steps(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/tracker/steps', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/tracker/distance
    def get_activities_tracker_distance(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/tracker/distance', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/tracker/floors
    def get_activities_tracker_floors(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/tracker/floors', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/tracker/elevation
    def get_activities_tracker_elevation(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/tracker/elevation', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/tracker/minutesSedentary
    def get_activities_tracker_minutesSedentary(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/tracker/minutesSedentary', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/tracker/minutesLightlyActive    
    def get_activities_tracker_minutesLightlyActive(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/tracker/minutesLightlyActive', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/tracker/minutesFairlyActive
    def get_activities_tracker_minutesFairlyActive(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/tracker/minutesFairlyActive', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/tracker/minutesVeryActive
    def get_activities_tracker_minutesVeryActive(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/tracker/minutesVeryActive', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/tracker/activeScore
    def get_activities_tracker_activeScore(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/tracker/activeScore', to_date=to_date, from_date=from_date, period=period, format=format)

    # activities/tracker/activityCalories   
    def get_activities_tracker_activityCalories(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='activities/tracker/activityCalories', to_date=to_date, from_date=from_date, period=period, format=format)

    # sleep/startTime
    def get_sleep_startTime(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='sleep/startTime', to_date=to_date, from_date=from_date, period=period, format=format)

    # sleep/timeInBed
    def get_sleep_timeInBed(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='sleep/timeInBed', to_date=to_date, from_date=from_date, period=period, format=format)

    # sleep/minutesAsleep
    def get_sleep_minutesAsleep(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='sleep/minutesAsleep', to_date=to_date, from_date=from_date, period=period, format=format)

    # sleep/awakeningsCount    
    def get_sleep_awakeningsCount(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='sleep/awakeningsCount', to_date=to_date, from_date=from_date, period=period, format=format)

    # sleep/minutesAwake
    def get_sleep_minutesAwake(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='sleep/minutesAwake', to_date=to_date, from_date=from_date, period=period, format=format)

    # sleep/minutesToFallAsleep
    def get_sleep_minutesToFallAsleep(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='sleep/minutesToFallAsleep', to_date=to_date, from_date=from_date, period=period, format=format)

    # sleep/minutesAfterWakeup
    def get_sleep_minutesAfterWakeup(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='sleep/minutesAfterWakeup', to_date=to_date, from_date=from_date, period=period, format=format)

    # sleep/efficiency
    def get_sleep_efficiency(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='sleep/efficiency', to_date=to_date, from_date=from_date, period=period, format=format)

    # body/weight    
    def get_body_weight(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='body/weight', to_date=to_date, from_date=from_date, period=period, format=format)

    # body/bmi
    def get_body_bmi(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='body/bmi', to_date=to_date, from_date=from_date, period=period, format=format)

    # body/fat
    def get_body_fat(self, to_date=date.today().isoformat(), from_date=None, period='max', format='json'):
        return self.fitbit.get_time_series(resource_path='body/fat', to_date=to_date, from_date=from_date, period=period, format=format)
