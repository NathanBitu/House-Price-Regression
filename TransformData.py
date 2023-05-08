import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

class transform_data:
    def __init__(self, path):
        self.path = path

    def get_data(self, train_or_analysis = 'train'):
        # Load data
        train_df = pd.read_csv(self.path)

        # Calculate percentage of null values in columns
        def pct_null_column(df):
            nulls = {}
            for column in df.columns:
                l = len(df)
                null = (df[column].isna()).sum()
                pct_null = (null / l) * 100
                nulls[column] = pct_null
            df = pd.DataFrame(index = ['pct_null_values'], data = nulls).T.sort_values(by = 'pct_null_values', ascending=False)
            return df.loc[(df.pct_null_values != 0)]

        nulls = pct_null_column(train_df.copy())

        # Fill null values
        def fill_nas(df):
            for column in df.columns:
                if column == 'PoolQC':
                    df[column] = df[column].fillna('No Pool')
                elif column == 'MiscFeature':
                    df[column] = df[column].fillna('No Misc')
                elif column == 'Alley':
                    df[column] = df[column].fillna('No Alley')
                elif column == 'Fence':
                    df[column] = df[column].fillna('No Fence')
                elif column == 'FireplaceQu':
                    df[column] = df[column].fillna('No Fireplace')
                elif column == 'GarageYrBlt': 
                    df[column] = df[column].fillna(0)
                elif column in ('GarageCond', 'GarageType', 'GarageFinish', 'GarageQual'):
                    df[column] = df[column].fillna('No Garage')
                elif column in ('BsmtFinType2', 'BsmtExposure', 'BsmtQual', 'BsmtCond', 'BsmtFinType1'):
                    df[column] = df[column].fillna('No Basement')
                elif column == 'LotFrontage':
                    df[column] = df[column].fillna(df[column].mean())
            #df.dropna(inplace = True)
            return df

        train_df = fill_nas(train_df)
        ## For analysis is better to have categorical columns instead of onehot encoded
        if train_or_analysis == 'analysis':
            return train_df
        # Log-transform numerical columns
        num_columns = []
        for column in train_df.columns:
            if train_df[column].dtype in ('int64', 'float64'):
                num_columns.append(column)
        
        for column in num_columns:
            if train_df[column].min() == 0:
                train_df[column] = np.log(train_df[column].astype(float) + 1)
            elif column == 'Id':
                continue
            else:
                train_df[column] = np.log(train_df[column].astype(float))

        # One-hot encode categorical columns
        cat_columns = [column for column in train_df.columns if train_df[column].dtype == 'O']

        train_cat = pd.DataFrame()
        encoder = OneHotEncoder()
        for i in cat_columns:
            cat = pd.DataFrame(data = encoder.fit_transform(train_df[[i]]).toarray(), columns = encoder.get_feature_names_out())
            if i == 'MSZoning':
                train_cat = cat
            else:     
                train_cat = train_cat.join(cat)

        train_df.drop(cat_columns, axis = 1, inplace = True)
        train_cat.reset_index(drop = True, inplace = True)
        train_df.reset_index(drop = True, inplace = True)

        # Join transformed columns
        train_df = train_df.join(train_cat)

        return train_df
