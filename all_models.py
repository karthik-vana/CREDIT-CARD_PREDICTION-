import os
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

import warnings

from sklearn.metrics import accuracy_score

warnings.filterwarnings('ignore')
from log_code import setup_logging
logger = setup_logging('all_models')

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_curve,roc_auc_score
import pickle


def knn(X_train,y_train,X_test,y_test):
    try:
        global knn_reg
        knn_reg = KNeighborsClassifier(n_neighbors=5)
        knn_reg.fit(X_train,y_train)
        logger.info(f'knn Test Accuracy: {accuracy_score(y_test,knn_reg.predict(X_test))}')

    except Exception as e:
        error_type,error_msg,error_line =  sys.exc_info()
        logger.info(f'error in line no {error_line.tb_lineno} : due to  {error_msg}')

def nb(X_train,y_train,X_test,y_test):
    try:
        global nb_reg
        nb_reg = GaussianNB()
        nb_reg.fit(X_train,y_train)
        logger.info(f'Naive bayes Test Accuracy : {accuracy_score(y_test,nb_reg.predict(X_test))}')

    except Exception as e:
        error_type,error_msg,error_line =  sys.exc_info()
        logger.info(f'error in line no {error_line.tb_lineno} : due to  {error_msg}')

def lr(X_train,y_train,X_test,y_test):
    try:
        global lr_reg
        lr_reg = LogisticRegression()
        lr_reg.fit(X_train,y_train)
        logger.info(f'Logistic regression Test accuracy : {accuracy_score(y_test,lr_reg.predict(X_test))}')
    except Exception as e:
        error_type,error_msg,error_line =  sys.exc_info()
        logger.info(f'error in line no {error_line.tb_lineno} : due to  {error_msg}')

def dt(X_train,y_train,X_test,y_test):
    try:
        global dt_reg
        dt_reg = DecisionTreeClassifier()
        dt_reg.fit(X_train,y_train)
        logger.info(f'decision tree Test accuracy : {accuracy_score(y_test,dt_reg.predict(X_test))}')
    except Exception as e:
        error_type,error_msg,error_line =  sys.exc_info()
        logger.info(f'error in line no {error_line.tb_lineno} : due to  {error_msg}')

def rf(X_train,y_train,X_test,y_test):
    try:
        global rf_reg
        rf_reg = RandomForestClassifier()
        rf_reg.fit(X_train,y_train)
        logger.info(f'random forest Test accuracy : {accuracy_score(y_test,rf_reg.predict(X_test))}')
    except Exception as e:
        error_type,error_msg,error_line =  sys.exc_info()
        logger.info(f'error in line no {error_line.tb_lineno} : due to  {error_msg}')

def ada(X_train,y_train,X_test,y_test):
    try:
        global ada_reg
        ada_reg = AdaBoostClassifier()
        ada_reg.fit(X_train,y_train)
        logger.info(f'Adaboost  Test accuracy : {accuracy_score(y_test,ada_reg.predict(X_test))}')
    except Exception as e:
        error_type,error_msg,error_line =  sys.exc_info()
        logger.info(f'error in line no {error_line.tb_lineno} : due to  {error_msg}')

def gb(X_train,y_train,X_test,y_test):
    try:
        global gb_reg
        gb_reg = GradientBoostingClassifier()
        gb_reg.fit(X_train,y_train)
        logger.info(f'Gradient boost Test accuracy : {accuracy_score(y_test,gb_reg.predict(X_test))}')
    except Exception as e:
        error_type,error_msg,error_line =  sys.exc_info()
        logger.info(f'error in line no {error_line.tb_lineno} : due to  {error_msg}')


def common(X_train,y_train,X_test,y_test):
    try:
        logger.info('=================knn============')
        knn(X_train,y_train,X_test,y_test)
        logger.info('==============nb================')
        nb(X_train,y_train,X_test,y_test)
        logger.info('==============lr================')
        lr(X_train,y_train,X_test,y_test)
        logger.info('==============dt================')
        dt(X_train,y_train,X_test,y_test)
        logger.info('==============rf================')
        rf(X_train,y_train,X_test,y_test)
        logger.info('==============ada===============')
        ada(X_train,y_train,X_test,y_test)
        logger.info('==============gb================')
        gb(X_train,y_train,X_test,y_test)


        knn_predictions = knn_reg.predict_proba(X_test)[:, 1]
        nb_predictions = nb_reg.predict_proba(X_test)[:,1]
        lr_predictions = lr_reg.predict_proba(X_test)[:,1]
        dt_predictions = dt_reg.predict_proba(X_test)[:,1]
        rf_predictions = rf_reg.predict_proba(X_test)[:,1]
        with open('credit_card.pkl','wb') as f:
            pickle.dump(rf_reg,f)
        ada_predictions = ada_reg.predict_proba(X_test)[:,1]
        gb_predictions = gb_reg.predict_proba(X_test)[:,1]


        knn_fpr,knn_tpr,knn_thre = roc_curve(y_test,knn_predictions)
        nb_fpr,nb_tpr,nb_thre = roc_curve(y_test,nb_predictions)
        lr_fpr,lr_tpr,lr_thre =  roc_curve(y_test,lr_predictions)
        dt_fpr, dt_tpr, dt_thre = roc_curve(y_test, dt_predictions)
        rf_fpr, rf_tpr, rf_thre = roc_curve(y_test, rf_predictions)
        ada_fpr, ada_tpr, ada_thre = roc_curve(y_test, ada_predictions)
        gb_fpr, gb_tpr, gb_thre = roc_curve(y_test, gb_predictions)

        plt.figure(figsize = (5,3))
        plt.plot(knn_fpr,knn_tpr,label = 'knn')
        plt.plot(nb_fpr,nb_tpr,label = 'nb')
        plt.plot(lr_fpr,lr_tpr,label =  'lr')
        plt.plot(dt_fpr,dt_tpr,label = 'dt')
        plt.plot(rf_fpr,rf_tpr,label = 'rf')
        plt.plot(ada_fpr,ada_tpr,label = 'ada')
        plt.plot(gb_fpr,gb_tpr,label = 'gb')

        plt.xlabel('false positive rate')
        plt.ylabel('true positive rate')
        plt.title('ROC curve - All models')
        plt.legend(loc =  0)
        plt.show()

        return X_train, y_train, X_test, y_test

    except Exception as e:
        error_type,error_msg,error_line =  sys.exc_info()
        logger.info(f'error in line no {error_line.tb_lineno} : due to  {error_msg}')



