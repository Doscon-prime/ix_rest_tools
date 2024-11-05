#%%
from IPython import get_ipython
ip = get_ipython()
ip.magic("reload_ext autoreload")  # these will enable module autoreloading
ip.magic("autoreload 2")
#%%
from ix_rest_tools import get_tags,get_values,set_values
import requests

#%%
server = "10.1.1.164" # replace with your IP

session = requests.Session()

#%% Get all tags
tags = get_tags(server,session)
print(tags)

#%% Get values

values = get_values(server,tags,session)
print(values) 

#%% Set values of some tags

insert_values = {"sensor1":1,"sensor2":2,"sensor3":3}
response = set_values(server,insert_values,session)
print(response) 