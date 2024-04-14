from sklearn.utils import shuffle
import numpy as np
import pandas as pd
np.random.seed(12345)

dataPar = pd.read_csv('.\DataSet\Data_Par_qty.csv')
dataPar


# Shuffle ข้อมูล

# Shuffle ข้อมูล
shuffled_data = shuffle(dataPar, random_state=42)

shuffled_data.to_csv('shuffle_Data_Par_qty.csv', index=False)
