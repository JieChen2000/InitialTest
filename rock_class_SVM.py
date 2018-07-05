
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv('training_data.csv')
data.describe()
test_well = data[data['Well Name'] == 'SHANKLE']
data = data[data['Well Name'] != 'SHANKLE']


# In[2]:


features = ['GR', 'ILD_log10', 'DeltaPHI','PHIND','PE','NM_M', 'RELPOS']
feature_vectors = data[features]
facies_labels = data['Facies']
facies_labels.describe()


# In[3]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(feature_vectors)
scaled_features = scaler.transform(feature_vectors) #ndarray now. 


# In[4]:


from sklearn.cross_validation import train_test_split
X_train, X_cv, y_train, y_cv = train_test_split(scaled_features, facies_labels,test_size=0.05, random_state=42)
X_train


# In[5]:


from sklearn import svm
clf = svm.SVC(C=1, gamma='auto',decision_function_shape='ovr',kernel='poly',degree=5)
clf.fit(X_train, y_train)


# In[6]:


from sklearn.metrics import classification_report
target_names = ['SS', 'CSiS', 'FSiS', 'SiSh','MS', 'WS', 'D','PS', 'BS']


# In[7]:


y_cv_pred = clf.predict(X_cv) 
print(classification_report(y_cv, y_cv_pred,target_names=target_names))


# In[8]:


y_test = test_well['Facies']


# In[9]:


well_features = test_well.drop(['Facies','Formation','Well Name','Depth'],axis=1)
X_test = scaler.transform(well_features)
y_pred = clf.predict(X_test)
test_well['Prediction'] = y_pred


# In[10]:



print(classification_report(y_test, y_pred,target_names=target_names))


# In[14]:


lin_clf=svm.LinearSVC(C=1)
lin_clf.fit(X_train, y_train)


# In[15]:


y_pred = lin_clf.predict(X_test)
print(classification_report(y_test, y_pred,target_names=target_names))


# In[13]:


from sklearn.model_selection import GridSearchCV
parameters = {'C':[0.01, 100]}
lin_svc = svm.LinearSVC() 
lin_clf = GridSearchCV(lin_svc, parameters)
lin_clf.fit(X_train, y_train)
print(lin_clf.best_params_)

'''
for SVM, 
kernal function: linear, poly, rbgf (linear seems best on F1)
decision function shape ovr 
'''

