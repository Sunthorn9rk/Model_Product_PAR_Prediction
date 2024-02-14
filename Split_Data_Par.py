from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
np.random.seed(12345)

dataPar = pd.read_csv('.\DataSet\shuffle_Data_Par_qty.csv')

dataPar


# แบ่งข้อมูลเป็น train และ test
train_data, test_data = train_test_split(
    dataPar, test_size=0.3, random_state=42)

train_data.to_csv('Train_shuffle_Data_Par_qty.csv',
                  index=False)  # 70%

test_data.to_csv('Test_shuffle_Data_Par_qty.csv', index=False)  # 30%
