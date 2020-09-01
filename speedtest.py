# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Internet speed analysis
# Check the internet speeds at regular intervals to determine peak usage times around the neighbourhood, and how this afects our speeds.
# 
# Try correlating the speeds with times of day, days of the week, etc, or with big live streams or new show releases.

# %%
# Import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import datetime
import time
import os


# %%
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=/Users/gardnerone/Library/Application\ Support/Google/Chrome/Profile\ 1')


# %%
# Open Chrome at Ookla Speedtest
driver = webdriver.Chrome(options=options)
driver.get('https://www.speedtest.net')


# %%
# Run speedtest
btn_go = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
btn_go.click()

# Save current time
dt = datetime.datetime.now()


# %%
# Wait x seconds for test to complete
time.sleep(60)


# %%
# Close speedtest desktop ad, if it exists
btn_close = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
try:
    btn_close.click()
except:
    pass


# %%
# Get ping
lbl_ping = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
# Get download
lbl_download = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
# Get upload
lbl_upload = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')

# Store vals
ping = lbl_ping.text
download = lbl_download.text
upload = lbl_upload.text


# %%
# Save data to array
data = [ping, download, upload, dt]
df = pd.DataFrame([data], columns=['Ping', 'Download', 'Upload', 'Datetime'])


# %%
# Save to file, with headers if first save
out_path = 'results.csv'
df.to_csv(out_path, mode='a+', header=(not os.path.exists(out_path)), index=False)


# %%
test = pd.read_csv('results.csv')
test


