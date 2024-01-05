import lightgbm as lgbm
import numpy as np
import pandas as pd
import category_encoders as ce
from lightgbm import early_stopping, log_evaluation
import gc

from typing import List

class LightGBMRegressorModel:

    default_params = {
        'learning_rate': 0.01,
        'objective': 'regression',
        'metric': 'mae',
        'random_seed': 42,
        'n_jobs': -1,
        'force_col_wise': True,
        'boosting_type': 'gbdt',
        'feature_pre_filter': False,
        'n_estimators': 10000,
        'verbose': -1,
    }

    def __init__(self, params={}, use_tuning=False, use_log=True):
        self.__y_train_pred = np.ndarray(0)
        self.__y_valid_pred = np.ndarray(0)
        self.__y_test_pred = np.ndarray(0)
        self.params = {}
        self.params.update(self.default_params)
        self.params.update(params)
        self.__tuning = use_tuning
        self.__use_log = use_log
        # self.model = None
    
    def train(
        self, 
        X_train: pd.DataFrame, 
        y_train: pd.DataFrame, 
        X_valid: pd.DataFrame, 
        y_valid: pd.DataFrame,
        X_test: pd.DataFrame,
        val_indices = [],
        ) -> None:

        ohe = ce.OneHotEncoder(
            cols=[col for col in X_train.columns if X_train[col].dtype == 'category'],
            handle_unknown='value', 
            handle_missing='value', 
            verbose=1,
            use_cat_names=True)
            
        X_train = ohe.fit_transform(X_train)
        X_valid = ohe.transform(X_valid)
        X_test = ohe.transform(X_test)

        cols = X_train.T.drop_duplicates().dropna(axis=1, how='all').T.columns
        X_train = X_train[cols]
        X_valid = X_valid[cols]
        X_test = X_test[cols]

        train_set = lgbm.Dataset(X_train, label=y_train)
        val_set = lgbm.Dataset(X_valid, label=y_valid)

        val_sets = [train_set, val_set]
        for val in val_indices:
            val_sets.append(
                lgbm.Dataset(X_valid[val], label=y_valid[val])
            )

        model = lgbm.train(
            self.params,
            train_set,
            valid_sets=val_sets,
            verbose_eval=False,
            callbacks=[early_stopping(500), log_evaluation(500)],
        )

        self.__y_train_pred = model.predict(X_train, num_iteration=model.best_iteration)
        self.__y_valid_pred = model.predict(X_valid, num_iteration=model.best_iteration)
        self.__y_test_pred = model.predict(X_test, num_iteration=model.best_iteration)

        del model
        gc.collect()
    
    def get_train_pred(self) -> np.ndarray:
        return self.__y_train_pred # type: ignore
    
    def get_valid_pred(self) -> np.ndarray:
        return self.__y_valid_pred # type: ignore
    
    def get_test_pred(self) -> np.ndarray:
        return self.__y_test_pred # type: ignore