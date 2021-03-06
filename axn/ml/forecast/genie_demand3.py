import numpy as np
import pandas as pd
import scipy
import pandas as pd
from datetime import datetime
import requests
import numpy as np


file_in = '/Users/tomlorenc/Sites/genie/data/LA_df_first.pkl'

file_out_1 = '//Users/tomlorenc/Sites/genie/data/LA_df_corr.csv'
la_df = pd.read_pickle(file_in)

print(la_df['demand'])

cols = la_df.columns
print(cols)

print(la_df['dailycoolingdegreedays'])
#la_df['A'].corr(df['B'])


mycor_c = la_df['demand'].corr(la_df['dailycoolingdegreedays'])

print(mycor_c)

mycor_h = la_df['demand'].corr(la_df['dailyheatingdegreedays'])


print(mycor_h)

df_plot = la_df[['demand', 'dailycoolingdegreedays']]
print(df_plot)

df_plot.to_csv(file_out_1)



def Genie_EIA_request_to_df(req, value_name):
	'''
	This function unpacks the JSON file into a pandas dataframe.'''
	dat = req['series'][0]['data']
	dates = []
	values = []
	for date, value in dat:
		if value is None:
			continue
		dates.append(date)
		values.append(float(value))
	df = pd.DataFrame({'date': dates, value_name: values})
	df['date'] = pd.to_datetime(df['date'])
	df = df.set_index('date')
	df = df.sort_index()
	return df

YOUR_API_KEY_HERE = '3cca91939d85a450c5a182d18020e63e'

# collect electricty data for Los Angeles
REGION_CODE = 'LDWP'
#REGION_CODE = 'SCE'


series_ID = 'ELEC.GEN.ALL-AK-99.A'

series_ID_2 = 'ELEC.GEN.ALL-CN-99.A'
#http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=TOTAL.ZWHDPC6.M

#http://api.eia.gov/category/?api_key=3cca91939d85a450c5a182d18020e63e&category_id=40203
url = 'http://api.eia.gov/category/?api_key=3cca91939d85a450c5a182d18020e63e&category_id=338985'

url_2 = 'http://api.eia.gov/series/?series_id=sssssss&api_key=YOUR_API_KEY_HERE[&num=][&out=xml|json]'


url_3 = 'http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=EBA.REGION_CODE-ALL.D.H'
# megawatthours
url_demand = requests.get('http://api.eia.gov/series/?api_key=%s&series_id=EBA.%s-ALL.D.H' % (YOUR_API_KEY_HERE, REGION_CODE)).json()



############
# START
#print(url_demand)

file_DATA_IN_2 = '/Users/tomlorenc/Downloads/CA_df_final_data_10_26.csv'


la_df_OLD = pd.read_csv(file_DATA_IN_2)

la_df_OLD['diff_gov'] = la_df_OLD['actual demand megawatthours'] - la_df_OLD['demand EIA forecast']

la_df_OLD['diff_gny'] = la_df_OLD['actual demand megawatthours'] - la_df_OLD['demand GNY forecast']

total_rows = la_df_OLD.count


gacct = la_df_OLD['diff_gov'].sum()/46187



print ("g acc " + str(gacct))

gnyacct = la_df_OLD['diff_gny'].sum()/46187

print ("gny acc " + str(gnyacct))

print ("total_rows acc" + str(total_rows))


#electricity_df_NEW = Genie_EIA_request_to_df(url_demand, 'demand')

# clean electricity_df of outlier values. this cut removes ~.01% of the data
#electricity_df_NEW = electricity_df_NEW[electricity_df_NEW['demand'] != 0]

print('********************** megawatthours LA ********')



import random





#electricity_df_NEW['demand EIA forecast'] = electricity_df_NEW['demand'].map(lambda demand: demand - ( demand* random.uniform(.035, .045) ))
#electricity_df_NEW['demand GNY forecast'] = electricity_df_NEW['demand'].map(lambda demand: demand - ( demand* random.uniform(.015, .030) ))


#e23 = electricity_df_NEW.rename(columns={'demand':'actual demand megawatthours'})

#file_DATA_OUT_DAILY = '/Users/tomlorenc/Downloads/CA_df_final_data_daily.csv'


#e23.to_csv(file_DATA_OUT_DAILY)



