import pandas as pd
from genpipes import declare, compose
from constants import *
import requests as req
import json


base_url = "http://127.0.0.1:8000/api/taipower/"
#base_url = "127.0.0.1:8099/"


@declare.datasource(inputs=[daily_latest_three_year_peak_backup_rate.csv])
def daily_latest_three_year_peak_backup_rate_source(path):
    df = pd.read_csv(path)
    return df


@declare.generator()
@declare.datasource(inputs=[daily_support_and_demand_2020.csv])
def daily_peak_powerplant_2020_source(path):
    df = pd.read_csv(
        path,
        usecols=[
            '日期',
            '核一#1(萬瓩)', '核一#2(萬瓩)',
            '核二#1(萬瓩)', '核二#2(萬瓩)',
            '核三#1', '核三#2',
            '林口#1', '林口#2', '林口#3',
            '台中#1', '台中#2', '台中#3', '台中#4',
            '台中#5', '台中#6', '台中#7', '台中#8',
            '台中#9', '台中#10',
            '興達#1', '興達#2', '興達#3', '興達#4',
            '大林#1', '大林#2', '和平#1', '和平#2', '麥寮#1', '麥寮#2', '麥寮#3',
            '汽電共生', '大潭 (#1-#6)', '通霄 (#1-#6)', '興達 (#1-#5)',
            '南部 (#1-#4)', '大林(#5-#6)',
            '海湖 (#1-#2)', '國光 #1',
            '新桃#1', '星彰#1', '星元#1', '嘉惠#1', '豐德(#1-#2)',
            '協和 (#1-#4)', '氣渦輪', '離島', '德基',
            '青山', '谷關', '天輪', '馬鞍', '萬大', '大觀',
            '鉅工', '大觀二', '明潭', '碧海', '立霧', '龍澗', '卓蘭', '水里', '其他小水力',
            '風力發電', '太陽能發電',
        ])

    return df


@declare.processor()
def daily_peak_powerplant_2020_processor(stream, url):
    for df in stream:
        client = req.session()
        # yield client
        print(df.to_dict("records"))
        resp = req.post(url, json=df.to_dict("records"))
        print(resp.content)
        yield True


@declare.generator()
@declare.datasource(inputs=[daily_support_and_demand_2020.csv])
def daily_support_and_demand_2020_source(path):
    df = pd.read_csv(
        path,
        usecols=[
            '日期', '淨尖峰供電能力(MW)', '尖峰負載(MW)',
            '備轉容量(MW)', '備轉容量率(%)', '工業用電(百萬度)',
            '民生用電(百萬度)'
        ])

    df.columns = [
        "time",
        "peak_support",
        "peak_demand",
        "backup_volume",
        "backup_volume_rate",
        "industry",
        "domestic",
    ]

    df.time = pd.to_datetime(df.time, format="%Y%m%d")
    df.time = df.time.dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    print(df)
    return df


@declare.processor()
def daily_support_and_demand_2020_processor(stream, url):
    for df in stream:
        client = req.session()
        # yield client
        print(df.to_dict("records"))
        resp = req.post(url, json=df.to_dict("records"))
        print(resp.content)
        yield True


@declare.datasource(inputs=[yearly_peak_usage_and_backup_rate.csv])
def yearly_peak_usage_and_backup_rate_source(path):
    df = pd.read_csv(path)
    return df


@declare.datasource(inputs=[flow.csv])
def flow_source(path):
    df = pd.read_csv(path)
    return df


@declare.datasource(inputs=[daily_peak_backup_rate_2021.csv])
def daily_peak_backup_rate_2021_source(path):
    df = pd.read_csv(path)
    return df


@declare.datasource(inputs=[adjust_history.csv])
def adjust_history_source(path):
    df = pd.read_csv(path)
    return df


@declare.datasource(inputs=[yearly_neighbor_price_comparison_2014.csv])
def yearly_neighbor_price_comparison_2014_source(path):
    df = pd.read_csv(path)
    return df


@declare.datasource(inputs=[yearly_neighbor_price_comparison_2019.csv])
def yearly_neighbor_price_comparison_2019_source(path):
    df = pd.read_csv(path)
    return df


def main():
    pipe = compose.Pipeline(
        steps=[
            ("source", daily_support_and_demand_2020_source, {}),
            ("test", daily_support_and_demand_2020_processor,
             {"url": base_url + "peak/history/"})
        ]
    )
    pipe.run()

    inputs = [
        daily_support_and_demand_2020_source,

    ]


if __name__ == '__main__':
    main()
