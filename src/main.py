from data_loader import load_data
from preprocessing import drop_columns, impute_numeric, impute_categorical, get_column_types
from model import train_catboost, predict
from submission import create_submission

# Update these paths as per your actual data location
train_path = "../notebooks/Train.csv"
test_path = "../notebooks/Test.csv"

train_df, test_df = load_data(train_path, test_path)

# Drop columns if they exist
for col in ['GpuNumberOfExecutionUnits']:
    if col in train_df.columns:
        train_df = drop_columns(train_df, [col])
    if col in test_df.columns:
        test_df = drop_columns(test_df, [col])

numeric_columns, categorical_columns = get_column_types(train_df)

train_df = impute_numeric(train_df, numeric_columns)
train_df = impute_categorical(train_df, categorical_columns)
test_df = impute_numeric(test_df, numeric_columns)
test_df = impute_categorical(test_df, categorical_columns)

X = train_df.drop(['FPS'], axis=1)
y = train_df['FPS']

cat_features = [col for col in [
    'CpuName', 'CpuMultiplierUnlocked', 'GpuName', 'GpuArchitecture',
    'GpuBus nterface', 'GpuDirectX', 'GpuMemoryType', 'GpuOpenCL',
    'GpuOpenGL', 'GpuShaderModel', 'GpuVulkan', 'GameName', 'GameSetting',
    'Dataset'
] if col in X.columns]

# Train model
model = train_catboost(X, y, cat_features)

# Prepare test data
if 'Index' in test_df.columns:
    Index = test_df['Index']
    test_df = test_df.drop(['Index'], axis=1)
else:
    Index = range(len(test_df))

y_test = predict(model, test_df)
create_submission(Index, y_test)