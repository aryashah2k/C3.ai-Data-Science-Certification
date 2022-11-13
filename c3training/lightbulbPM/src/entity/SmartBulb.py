import pandas as pd
import datetime as dt

def convert_dates_to_common_format(input_date):
        
        # if the date is a datetime, we need to strip timezone information
        if isinstance(input_date, dt.datetime):
            date = input_date.replace(tzinfo=None)
        # if the date is a string, we need to convert it to a datetime
        elif isinstance(input_date, str):
            date = dt.datetime.strptime(input_date, "%Y-%m-%dT%H:%M:%S")
        
        return date

def abs_day_diff(input_date_1, input_date_2):
    # Convert dates and subtract using the convert_dates_to_common_format funtion
    date_1 = convert_dates_to_common_format(input_date_1)
    date_2 = convert_dates_to_common_format(input_date_2)
    
    return abs((date_1 - date_2).days) / 365.

def lifeSpanInYears(bulbId):
    # Get startDate from SmartBulbMeasurement
    bulb = c3.SmartBulb.get(this={'id': bulbId})
    startDate = bulb.startDate
    
    # Get data from SmartBulbMeasurement
    limitSpec = -1
    defectFilter = "status == 1 && lumens == 0 && parent.id == '" + 'SBMS_serialNo_' + bulb.id + "'"
    smartbulbmeasurement_objs = c3.SmartBulbMeasurement.fetch(spec={'limit':limitSpec,
                                                                    'filter':defectFilter}).objs
    smartbulbmeasurement_pd = pd.DataFrame(smartbulbmeasurement_objs.toJson())
    
    # get endDate from filtered measurements
    smartbulbmeasurement_pd.sort_values(by='start',ascending=False)
    endDate = str(smartbulbmeasurement_pd[['start']].iloc[0].values[0])
    
    # return endDate - startDate from using abs_day_diff function
    return abs_day_diff(startDate, endDate)

