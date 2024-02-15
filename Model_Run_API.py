# Model_run_API.py
from joblib import load
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np

app = FastAPI()


class ModelInput(BaseModel):
    pr_dpcode: int
    brcode: int
    parqty: int
    sh_daysmin: int
    sd_t_qty_30: float
    on_promotion: float
    Parqty_Cal: int


# Loading the saved model
data_par_model_find_Parqty_Cal = load(
    "./resultsfiles/RF_Model_Product_PAR_1.pkl")


data_par_model_find_Parqty_Adj = load(
    "./resultsfiles/RF_Model_Product_PAR_2.pkl")


@app.post('/data_par_prediction')
def data_par_prediction(input_parameters: ModelInput):
    input_data = input_parameters.dict()

    dp = input_data['pr_dpcode']
    br = input_data['brcode']
    par = input_data['parqty']
    shdays = input_data['sh_daysmin']
    sdt = input_data['sd_t_qty_30']
    onpro = input_data['on_promotion']

    input_list = [dp, br, par, shdays, sdt, onpro]

    try:
        # ทำการ predict ด้วยโมเดล data_par_model_find_Parqty_Cal
        Parqty_Cal = data_par_model_find_Parqty_Cal.predict([input_list])[0]
        Parqty_Cal = Parqty_Cal
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error during prediction: {str(e)}")

    # เพิ่มค่า Parqty_Cal เข้าไปใน input_data
    input_data['Parqty_Cal'] = Parqty_Cal

    input_list2 = [dp, br, par, shdays, sdt, onpro, Parqty_Cal]

    try:
        # ทำการ predict ด้วยโมเดล data_par_model_find_Parqty_Adj
        Parqty_Adj = data_par_model_find_Parqty_Adj.predict([input_list2])[0]
        Parqty_Adj = Parqty_Adj
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error during prediction: {str(e)}")

    return {"Parqty_Cal": Parqty_Cal, "Parqty_Adj": Parqty_Adj}


# -------------------------------------------------------------------------------------------------
# cd /d D:/
# cd D:\CODE\DataScience\Model_Product_PAR_Prediction
# uvicorn Model_Run_API:app

# {
#     "pr_dpcode": 1,
#     "brcode": 1016,
#     "parqty": 5,
#     "sh_daysmin": 365,
#     "sd_t_qty_30": 4,
#     "on_promotion": 0,
#     "Parqty_Cal": 0
# }
