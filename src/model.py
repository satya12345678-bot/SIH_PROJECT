from catboost import CatBoostRegressor

def train_catboost(X, y, cat_features):
    cb = CatBoostRegressor(
        iterations=2000,
        random_seed=42,
        eval_metric='RMSE',
        early_stopping_rounds=50,
        learning_rate=0.05,
        depth=8,
        task_type='GPU',
        l2_leaf_reg=7,
        border_count=256,
        subsample=0.8,
        grow_policy='SymmetricTree',
        sampling_frequency='PerTree',
        bootstrap_type='Bernoulli'
    )
    cb.fit(X, y, cat_features=cat_features, verbose=500, early_stopping_rounds=50)
    return cb

def predict(model, X):
    return model.predict(X)