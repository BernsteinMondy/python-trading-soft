import pandas as pd


class DataLoader:
    @staticmethod
    def from_csv(path: str) -> pd.DataFrame:
        """
        Loads data from CSV file and sets column 'Date' as index.
        :param path: path to CSV file with data.
        :return: pd.DataFrame with indexed data.
        """
        df = pd.read_csv(path, sep='\t', encoding="utf-8")

        if "Date" not in df.columns:
            raise ValueError("Column 'Date' not found in CSV file.")
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)

        return df
