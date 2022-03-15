#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:12:58 2022

@author: malte
"""

import pandas as pd
henry = pd.DataFrame({'gender': ['male'], 'age': [47],
           'class': ['1st'],
           'embarked': ['Cherbourg'], 'fare': [25],
           'sibsp': [0], 'parch': [0]},
           index = ['Henry'])
import dalex as dx

titanic = dx.datasets.load_titanic()
X = titanic.drop(columns='survived')
y = titanic.survived

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

preprocess = make_column_transformer(
    (StandardScaler(), ['age', 'fare', 'parch', 'sibsp']),
    (OneHotEncoder(), ['gender', 'class', 'embarked']))

from sklearn.ensemble import RandomForestClassifier

titanic_rf = make_pipeline(
    preprocess,
    RandomForestClassifier(max_depth = 3, n_estimators = 500))
titanic_rf.fit(X, y)

titanic_rf_exp = dx.Explainer(titanic_rf, X, y, 
           label = "Titanic RF Pipeline")
