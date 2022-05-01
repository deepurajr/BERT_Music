from .base import AbstractDataset

import pandas as pd

from datetime import date


class MLSDataset(AbstractDataset):
    @classmethod
    def code(cls):
        return 'mls'

    @classmethod
    def url(cls):
        return ''

    @classmethod
    def zip_file_content_is_folder(cls):
        return True

    @classmethod
    def all_raw_file_names(cls):
        return ['listenbrainz.csv']

    def load_ratings_df(self):
        folder_path = self._get_rawdata_folder_path()
        file_path = folder_path.joinpath('listenbrainz.csv')
        df = pd.read_csv(file_path)
        df.columns = ['uid', 'sid', 'rating', 'timestamp']
        return df


