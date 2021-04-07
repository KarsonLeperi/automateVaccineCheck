from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

def webCheck(info):

	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument('log-level=3')
	driver = Chrome(options=chrome_options)

	[costco_return_values, success_costco] = costcoCheck(driver)
	[vaxx_max_values, success_vaxMax] = vaxMaxCheck(info, driver)
	driver.quit()
	
	return vaxx_max_values, costco_return_values, success_costco, success_vaxMax
def vaxMaxCheck(info, driver):
	#Check vaxxmax for vaccine slots
	urls = info.urls
	df_column_names = ['store', 'city', 'state', 'zip',
                   'county', 'last_updated', 'became_available',
                   'distance']
	df_column_names_short = ['store', 'city', 'zip', 'distance']

	df_rows = []

	for i, url in enumerate(urls):
		# Open URL
		driver.get(url)
		driver.get(url) # You have to call it twice...

		# Select state
		if 'cvs' in url:
			name = 'cvs'
		elif 'walgreens' in url:
			name = 'walgreens'
		elif 'riteaid' in url:
			name = 'rite-aid'
		elif 'walmart' in url:
            name = 'walmart'
		
		
		selector = Select(driver.find_element_by_xpath(
			'//*[@id="state-select-'+name+'"]'))
		try:
			selector.select_by_value(info.state)
		except:
			continue
		time.sleep(2) #necessary buffer time

		# Access table
		table = driver.find_element_by_xpath('//*[@id="locations"]/tbody')
		rows = table.find_elements_by_tag_name('tr')

		# Iterate through rows of table and parse
		for row in rows:
			entries = row.find_elements_by_tag_name('td')
			entries_text = [entry.text.strip() for entry in entries]
			if len(entries_text) == 1:
				break

			# Reorder Rite-Aid and Walgreens columns to match CVS
			new_entries_text = [None]*len(df_column_names)
			if name == 'rite-aid':
				new_entries_text[1] = entries_text[3]
				new_entries_text[2] = entries_text[4]
				new_entries_text[3] = entries_text[5]
				new_entries_text[4] = None
				new_entries_text[5] = entries_text[6]
				new_entries_text[6] = entries_text[7]
				new_entries_text[7] = entries_text[-1]
			elif name == 'walgreens':
				new_entries_text[1] = entries_text[1]
				new_entries_text[2] = entries_text[2]
				new_entries_text[3] = entries_text[3]
				new_entries_text[4] = None
				new_entries_text[5] = entries_text[4]
				new_entries_text[6] = entries_text[5]
				new_entries_text[7] = entries_text[-1]
			elif name == 'walmart':
                new_entries_text[1] = entries_text[2] # town/city
                new_entries_text[2] = entries_text[3] # state
                new_entries_text[3] = entries_text[4] # zip
                new_entries_text[4] = entries_text[5] #county
                new_entries_text[5] = entries_text[6] # last updated
                new_entries_text[6] = entries_text[7] # became available
                new_entries_text[7] = entries_text[-1] # distance
			else:
				new_entries_text = entries_text

			# Clean up entry text
			new_entries_text[0] = name
			new_entries_text[3] = int(new_entries_text[3].split('Copy')[0].strip())
			new_entries_text[7] = int(new_entries_text[7])

			# Add to list of row info
			df_rows.append(new_entries_text)
    # Send out the winners
	if df_rows:
		# Construct DataFrame
		df = pd.DataFrame(df_rows, columns=df_column_names)
		df = df.sort_values('distance')
		df_close = df[df['distance'] <= info.max_distance]
		df_close = df_close[df_column_names_short]

		# If there are shots, notify!
		if len(df_close) > 0:
			return df_close, True
		else:
			return "Nothing Available", False
	
	
def costcoCheck(driver):
	#This check is based on the costco url redirecting to certain URLs when vaccines are available and when not. This specifically checks the locations based on my prefered ordering.
	locations = {
				"Aloha": "https://book-costcopharmacy.appointment-plus.com/ctnqxln8/?e_id=5363#/book-appointment/select-a-location",
				"Clackamas": "https://book-costcopharmacy.appointment-plus.com/ctns2ceq/?e_id=5377#/book-appointment/select-a-location",
				"Roseberg":"https://book-costcopharmacy.appointment-plus.com/ctnrctsx/?e_id=5381/#book-appointment/select-a-location"
				}
			
	for city, url in locations.items():
		driver.get(url)
		time.sleep(20)
		itt = 0
		new_url = driver.current_url
		if "select-staff" not in new_url:
			return [city, url], True
	
	return "Nothing Available", False