import pathlib


class File:
    def __init__(self, path):
        self._csv = None
        self._json = None
        self.data = None
        self.set_new_path(path)

    def set_new_path(self, path):
        if pathlib.Path(path).suffix == ".csv":
            self._csv = path
        if pathlib.Path(path).suffix == ".json":
            self._json = path

    @property
    def csv(self):
        return self._csv

    @property
    def json(self):
        return self._json


daily_latest_three_year_peak_backup_rate = File(
    "./required_data/backup/history/daily_latest_three_year_peak_backup_rate.csv")
daily_support_and_demand_2020 = File(
    "./required_data/backup/history/daily_support_and_demand_2020.csv")
yearly_peak_usage_and_backup_rate = File(
    "./required_data/backup/history/yearly_peak_usage_and_backup_rate.csv")
daily_peak_backup_rate_2021 = File(
    "./required_data/peak/history/daily_backup_rate_2021.csv")

adjust_history = File("./required_data/price/adjust/history/adjust.csv")

yearly_neighbor_price_comparison_2014 = File(
    "./required_data/price/neighborhood/yearly_comparison_2014.csv")
yearly_neighbor_price_comparison_2019 = File(
    "./required_data/price/neighborhood/yearly_comparison_2019.csv")

flow = File("./required_data/flow/flow.json")