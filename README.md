###ML project in 2018

--Roc Classification Summary 

simple algorithm yield good enough result, adding more feature won't improve much. 

complicated algorithm needs more feature engnieering to get better result. 

adding adding IDL/phid as extra attributes helps on all cases(SVM(0.43-0.44), DNN+feature augmentation(0.5-0.56)) tested. 

---comparison for below ways of predictions, under same conditions, one change a time. 

rock_calss-DNN.ipynb  F1 score 0.54 

rock_calss-XGBoost.ipynb F1 score 0.51 

rock_calss-DNN-FeatureEng.ipynb  F1 score 0.50 

rock_calss-XGBoost-FeatureEng.ipynb  F1 score 0.59

rock_class-XGboost-FeatureEng-Jay_V1  F1 score 0.62 

---algorithm change doesn't matter much

rock_calss-DNN.ipynb  F1 score 0.54 

rock_calss-XGBoost.ipynb F1 score 0.51 

---DNN(1 hidden layer, 3 nodes) is not sensitive to feature engineer

rock_calss-DNN-FeatureEng.ipynb  F1 score 0.50 


---XGBoost(3 layer w/ 150 estimators) is sensitive to feature engineer

rock_calss-XGBoost-FeatureEng.ipynb  F1 score 0.59

---XGBoost w/ enhanced feature engineer, by adding IDL/phid as extra attributes. 

rock_class-XGboost-FeatureEng-Jay_V1  F1 score 0.62 

---DNN(1 hidden layer, 3 nodes) w/ enhanced feature engineer, by adding IDL/phid as extra attributes. 
rock_class-DNN-FeatureEng-Jay_V1.ipynb  F1 score 0.56 
