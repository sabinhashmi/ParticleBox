import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
sys.path.append('/home/hashmi/Files/DataFolder/Models')
import Classifier

fileName=input('Enter Test File Name ? ')
# fileName='Test'
data=pd.read_csv(fileName+'.csv')
model_Out=[]
for index,rowValue in data.iterrows():
    rawOutput=Classifier.apply_catboost_model(rowValue.values)
    probabilityOut= np.exp(rawOutput)/(1+np.exp(rawOutput))
    model_Out.append(probabilityOut)
data['Probability']=model_Out
data['Label']=np.where(data['Probability']<0.5,0,1)
data['Label'].value_counts()
print(data.head().T)


