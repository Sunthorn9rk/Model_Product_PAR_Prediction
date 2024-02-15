# API_Implemen_Data_Par.py

import json
import requests

url = 'http://127.0.0.1:8000/data_par_prediction'

input_data_for_model_data_par = {
    "pr_dpcode": 5,
    "brcode": 1044,
    "parqty": 3,
    "sh_daysmin": 450,
    "sd_t_qty_30": 1,
    "on_promotion": 1.25,
    "Parqty_Cal": 0
}


response_data_par = requests.post(url, json=input_data_for_model_data_par)


print(response_data_par.json())

# http://127.0.0.1:8000/docs

# {
#     "pr_dpcode": 1,
#     "brcode": 1016,
#     "parqty": 5,
#     "sh_daysmin": 365,
#     "sd_t_qty_30": 4,
#     "on_promotion": 0,
#     "Parqty_Cal": 0
# }
