import pandas as pd # manipulação de datasets
import numpy as np  # operações matemáticas 
import scipy

# sklearn é uma biblioteca de data science e machine learning
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

file_name = 'Prostate_GSE6919_U95B.csv'

if __name__ == '__main__':

    # usando a biblioteca pandas para abrir o arquivo .csv com os dados de expressão gênica
    data = pd.read_csv(file_name, delimiter=',', header=0, index_col=0) 
    #print(data)
    
    data_type = data['type']
    data_wo_type = data.drop('type', axis=1)
    classes = data['type'].unique()    

    #z-score
    #numeric_cols = data.select_dtypes(include=[np.number]).columns
    #non_numeric_cols = data.select_dtypes(include=object).columns
    #data = data[numeric_cols].apply(scipy.stats.zscore)
    #data = pd.concat([data_type,data],axis="columns")
    
    data_wo_type = data_wo_type.apply(scipy.stats.zscore)
    data = pd.concat([data_type,data_wo_type],axis="columns")

    #print("altered")
    #print(data)

    #split train and test
    [train,test] = train_test_split(data, test_size=0.3, train_size=0.7, random_state=None, shuffle=False, stratify=None)
    #print("train and test")
    #print(train.shape)
    #print(test.shape)

    #svm
    train_wo_type = train.drop('type', axis=1)
    train_type = train['type'] 

    clf = svm.SVC() # cria um modelo simples de SVM
    clf.fit(train_wo_type, train_type) # treina o SVM nos pares de entrada X e Y
    prediction = clf.predict(train_wo_type)
    #print(prediction)
    #print(np.size(prediction))
    #print(train_type.to_string())
    
    #metricas
    #(i)matriz de confusao
    cm = confusion_matrix(train_type, prediction, labels=classes)
    print('cm', cm)
    #(ii) a acurácia
    acs = accuracy_score(train_type,prediction,normalize=True)
    print('acs ',acs)
    #(iii) Sensitivity
    # (iv) Specificity
    # (v) F1-score.
    f1s = f1_score(train_type, prediction, labels=classes, pos_label='normal')
    print('f1s',f1s)

    
    

