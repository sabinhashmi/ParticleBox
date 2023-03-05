#Packages
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import ROOT
import root_numpy
import seaborn as sns
sns.set({'figure.figsize':(12,8)})

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score,roc_curve



from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier


log=LogisticRegressionCV()
nb=GaussianNB()
knn=KNeighborsClassifier()
dt=DecisionTreeClassifier()
rf=RandomForestClassifier()
adaboost=AdaBoostClassifier()
bag=BaggingClassifier()
grad=GradientBoostingClassifier()
nn=MLPClassifier()

models=[log,nb,knn,dt,rf,adaboost,bag,grad,nn]


from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
ss=StandardScaler()
rs=RobustScaler()

from imblearn.over_sampling import SMOTE
smote=SMOTE()

import warnings
warnings.filterwarnings('ignore')



### User Defined Functions

#BASELINE BOOSTED DECISION TREE
def train_model():
    grad=GradientBoostingClassifier(n_estimators=100,verbose=True)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,shuffle=True)
    grad.fit(x_train,y_train)
    y_predict=grad.predict(x_test)
    return(f'Accuracy of the model is {accuracy_score(y_test,y_predict)}')


#To remove outliers based on IQR
def quantile_fun(col):

    q1=col.quantile(0.25)
    q3=col.quantile(0.75)
    iqr=q3-q1
    lw=q1-(1.5*iqr) #LowerWhisker
    uw=q3+(1.5*iqr) #UpperWhisker
    new_col=[]
    for i in col:
        if i<lw:
            i=lw
            new_col.append(i)
        elif i>uw:
            i=uw
            new_col.append(i)
        else:
            i=i
            new_col.append(i)
    return np.array(new_col)


data_path='datasets/Brunel_BdJPsiKs_MagU_30k.root'
root_file=ROOT.TFile(data_path)
root_file.cd("ToolSvc.PatDebugTTTruthTool")
tree = ROOT.gDirectory.Get("DownstreamSeedDebugTuple")
original_data=pd.DataFrame(root_numpy.tree2array(tree))

print('Working on the real data....')

#data=original_data.head(10000) #Restriction for easy calculations
data=original_data
print('Complete data dimension is {}\nSample Data Dimension is {} '.format(original_data.shape,data.shape))


x=data.drop(['has_MCParticle', 'is_downstream_reconstructible','has_MCParticle_not_electron','is_downstream_reconstructible_not_electron', 'is_true_seed','seed_mva_value'],axis=1)
y=data['is_downstream_reconstructible']



print('Independent Variables dimension is {} \nDependent Variables dimension is {}'.format(x.shape,y.shape))


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,shuffle=True)

##BASELINE BOOSTED DECISION TREE
grad=GradientBoostingClassifier(learning_rate=0.1, n_estimators=100, subsample=0.8, random_state=13,min_samples_leaf=100, max_depth=6, max_features=8, verbose = 3 )
fit=grad.fit(x_train,y_train)
y_predict=grad.predict(x_test)
print (f'Accuracy of the model is {accuracy_score(y_test,y_predict)}')


print(roc_auc_score(y_test, grad.predict_proba(x_test)[:, 1]))

##########################################################
print('Scaling is in Progress....')

x=np.abs(x)
print('Absolute Values Fetched')

x=x.apply(quantile_fun)
print('Quantile Function Applied')

x=pd.DataFrame(ss.fit_transform(x),columns=x.columns)
print('Standard Scaler Applied')

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,shuffle=True)


print('Transformed DataFrame Training in Progress ... ')

grad=GradientBoostingClassifier(learning_rate=0.1, n_estimators=100, subsample=0.8, random_state=13,min_samples_leaf=100, max_depth=6, max_features=8, verbose = 3 )
fit=grad.fit(x_train,y_train)
y_predict=grad.predict(x_test)
print (f'Accuracy of the model is {accuracy_score(y_test,y_predict)}')

print(roc_auc_score(y_test, grad.predict_proba(x_test)[:, 1]))


print('Code completed.!')