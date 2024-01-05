import optuna
import numpy as np
from sklearn.metrics import mean_absolute_error
from typing import List

class EmsembleRegressorModel:
    def __init__(self) -> None:
        self.__weights : List[float] = []
        self.__train_pred = None
        self.__val_pred = None
        self.__test_pred = None

    def train(
        self,
        train: List[np.ndarray],
        val: List[np.ndarray],
        test: List[np.ndarray],
        y
        ) -> None:
        num_weights = len(val)

        def objective(trial):
            weights = []
            pred = None
            for idx in range(1, num_weights):
                weight = trial.suggest_float(f'weight_{idx}', 0.0, 1.0)
                weights.append(weight)
            weights.append(1 - sum(weights))

            for idx, weight in enumerate(weights):
                pred = (val[idx] * weight) \
                    if pred is None else (pred + val[idx] * weight)
            
            return mean_absolute_error(y, pred)

        optuna.logging.disable_default_handler()
        study = optuna.create_study(sampler=optuna.samplers.RandomSampler(seed=123))
    
        for idx in range(1, num_weights):
            study.enqueue_trial({f'weight_{idx}': 1 / (num_weights)})
        
        study.optimize(objective, n_trials=1000)

        weights = []
        for idx in range(1, num_weights):
            weights.append(study.best_params[f'weight_{idx}'])
        weights.append(1 - sum(weights))

        for idx, weight in enumerate(weights):
            self.__weights.append(weight)
            self.__train_pred = train[idx] * weight \
                if self.__train_pred is None else self.__train_pred + train[idx] * weight
            self.__val_pred = val[idx] * weight \
                if self.__val_pred is None else self.__val_pred + val[idx] * weight
            self.__test_pred = test[idx] * weight \
                if self.__test_pred is None else self.__test_pred + test[idx] * weight
    
    def get_train_pred(self) -> np.ndarray:
        return self.__train_pred  # type: ignore

    def get_val_pred(self) -> np.ndarray:
        return self.__val_pred  # type: ignore
    
    def get_test_pred(self) -> np.ndarray:
        return self.__test_pred  # type: ignore

    def get_weights(self) -> List[float]:
        return self.__weights