import pandas as pd
import numpy as np
import tensorflow as tf
def smape(y_true, y_pred):
    temp = pd.DataFrame()
    temp['y_true'] = y_true
    temp['y_pred'] = y_pred
    temp.dropna(inplace=True)
    if len(temp) != 0:
        smape = 2.0 * np.mean(np.abs(temp['y_pred'] -temp['y_true']).values / np.maximum(np.abs(temp['y_pred']).values + np.abs(temp['y_true']).values, np.finfo(np.float32).eps)) * 100
        return np.round(smape, 2)
    else:
        return np.nan

    
def mape(y_true, y_pred, thre=1000):
    temp = pd.DataFrame()
    temp['y_true'] = y_true
    temp['y_pred'] = y_pred
    temp.dropna(inplace=True)
    temp = temp[temp['y_true'] > thre]
    y_true = temp['y_true'].values
    y_pred = temp['y_pred'].values
    if len(temp) != 0:
        mape = np.mean(np.abs((y_true-y_pred)/y_true)) * 100
        return np.round(mape, 2)
    else:
        return np.nan

if __name__ == "__main__":
    print(333)
    print(666)
    pass