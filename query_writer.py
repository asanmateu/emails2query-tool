from constants import np, pd


class QueryWriter:
    def __init__(self, file_path, output_path):
        self.data = self._load_data(file_path)
        self.export = self._export_result(output_path)

    def _load_data(self, path):
        """Loads the template data into the main object for further manipulation.

        :param path:
        :return: pandas DataFrame with imported excel template.
        """
        return pd.read_excel(path)

    def _export_result(self, path):
        """Exports a results file with the desired fields in query format ready to copy and paste into query template.

        :param path: Absolute path including file name where the ready file will be placed.
        :return:
        """
        return pd.to_excel(path)

    def clean_nan_values(self, df):
        """Formats native excel null values into empty strings to avoid errors during validation logics.

         :param df: pandas DataFrame resulting from excel spreadsheet import.
         :return: same DataFrame object with NaN values replaced by empty strings.

         """
        df = df.replace('nan', np.nan, inplace=True)
        df = df.fillna("", inplace=True)
        return df
