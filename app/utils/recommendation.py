import pandas as pd
from surprise import Dataset
from surprise import NormalPredictor
from surprise import Reader
from surprise import SVD
from surprise.model_selection import cross_validate


class Recommendation(object):

    def predict(self, df: pd.DataFrame, dataset_columns: list, item_id: int,
                user_id: str, rating_scale_st: int = 1, rating_scale_end: int = 5, 
                cross_validate_value: int = 2):

        reader = Reader(rating_scale=(rating_scale_st, rating_scale_end))
        data = Dataset.load_from_df(df[dataset_columns], reader)
        cross_validate(NormalPredictor(), data, cv=cross_validate_value)

        svd = SVD()
        trainset = data.build_full_trainset()
        svd.fit(trainset)

        predict_df = df.copy()
        predict_df['Predicted_Score'] = predict_df[item_id].apply(
            lambda x: svd.predict(user_id, x).est)

        predict_df = predict_df.sort_values(by=['Predicted_Score'], ascending=False)
        predict_df = predict_df.drop_duplicates(subset=item_id)
        return predict_df
