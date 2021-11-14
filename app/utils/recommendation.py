import pandas as pd
from surprise import Dataset
from surprise import NormalPredictor
from surprise import Reader
from surprise import SVD
from surprise.model_selection import cross_validate


class Recommendation(object):

    def predict(self, df: pd.DataFrame, dataset_columns: list, item_id: int,
                user_id: str, limit: int, result_model):

        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(df[dataset_columns], reader)
        cross_validate(NormalPredictor(), data, cv=2)

        svd = SVD()
        trainset = data.build_full_trainset()
        svd.fit(trainset)

        items = df.copy()
        items['Predicted_Score'] = items[item_id].apply(
            lambda x: svd.predict(user_id, x).est)

        items = items.sort_values(by=['Predicted_Score'], ascending=False)
        items = items.drop_duplicates(subset=item_id)
        items.head(limit)

        return [result_model.init_from_df(x) for _, x in items.iterrows()]
