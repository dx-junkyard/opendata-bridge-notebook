from catboost import CatBoostRegressor
import numpy as np
import pandas as pd
import category_encoders as ce
import gc

class CatBoostRegressorModel:

    default_params = {
        'loss_function': 'MAE',
        'eval_metric': 'MAE',
        'learning_rate': 0.1,
        'num_boost_round': 10000,
        'random_state': 24,
    }

    def __init__(self, params={}):
        self.__y_train_pred = np.ndarray(0)
        self.__y_valid_pred = np.ndarray(0)
        self.__y_test_pred = np.ndarray(0)
        self.params = {}
        self.params.update(self.default_params)
        self.params.update(params)
    
    def train(
        self, 
        X_train: pd.DataFrame, 
        y_train: pd.DataFrame, 
        X_valid: pd.DataFrame, 
        y_valid: pd.DataFrame,
        X_test: pd.DataFrame,
        val_indices = [],
        ) -> None:

        model = CatBoostRegressor(
            **self.params,
            cat_features=[col for col in X_train.columns if X_train[col].dtype in ('category', 'bool')],
        )

        val_sets = [(X_train, y_train), (X_valid, y_valid)]
        for val in val_indices:
            val_sets.append(
                (X_valid[val], y_valid[val]) # type: ignore            
            )

        model.fit(
            X_train,
            y_train, 
            eval_set=val_sets,
            early_stopping_rounds=500)

        self.__y_train_pred = model.predict(X_train, ntree_end=model.best_iteration_)
        self.__y_valid_pred = model.predict(X_valid, ntree_end=model.best_iteration_)
        self.__y_test_pred = model.predict(X_test, ntree_end=model.best_iteration_)

        del model
        gc.collect()
    
    def get_train_pred(self) -> np.ndarray:
        return self.__y_train_pred
    
    def get_valid_pred(self) -> np.ndarray:
        return self.__y_valid_pred
    
    def get_test_pred(self) -> np.ndarray:
        return self.__y_test_pred