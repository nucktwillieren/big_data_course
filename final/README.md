# TaiPower Analysis

## To-dos
### Goals
動機：儘量把期末教的東西和自身經歷都可以放進來。

分析：
- 本來會的：
  - Web / Service
  - 繪圖
  - 資料處理
- 這學期學的：
  - Data Pipeline(老師剛好在討論區提到相關議題)
  - ML
企劃發想：最近缺電。擁有更多的資訊才能更加理性討論這項議題，並且防範。
原始企劃內容：希望先了解近年來的用電尖峰趨勢及備載量，並了解各區域發電量及南電北送等問題之原因，最後推估未來用電標準及相關問題。

系統架構：
![](https://i.imgur.com/9Y74MDL.png)


## Data Table
### 過去電力供需資訊
- Fields: 日期,淨尖峰供電能力(MW),尖峰負載(MW),備轉容量(MW),備轉容量率(%),工業用電(百萬度),民生用電(百萬度),核一#1(萬瓩),核一#2(萬瓩),核二#1(萬瓩),核二#2(萬瓩),核三#1,核三#2,林口#1,林口#2,林口#3,台中#1,台中#2,台中#3,台中#4,台中#5,台中#6,台中#7,台中#8,台中#9,台中#10,興達#1,興達#2,興達#3,興達#4,大林#1,大林#2,和平#1,和平#2,麥寮#1,麥寮#2,麥寮#3,汽電共生,大潭 (#1-#6),通霄 (#1-#6),興達 (#1-#5),南部 (#1-#4),大林(#5-#6),海湖 (#1-#2),國光 #1,新桃#1,星彰#1,星元#1,嘉惠#1,豐德(#1-#2),協和 (#1-#4),氣渦輪,離島,德基,青山,谷關,天輪,馬鞍,萬大,大觀,鉅工,大觀二,明潭,碧海,立霧,龍澗,卓蘭,水里,其他小水力,風力發電,太陽能發電
- During: 20200101 - 20210430
- Time Resolution: day
### 本年度每日尖峰備轉容量率
- Fields: 日期,備轉容量(萬瓩),備轉容量率(%)
- During: 20210101 - 20210615
- Time Resolution: day
### 近三年每日尖峰備轉容量率
- Fields: 日期,備轉容量(萬瓩),備轉容量率(%)
- During: 2018 - 2020
- Time Resolution: day
### 用電統計資料
- Fields: 年度,電燈售電量(度),電力售電量(度),售電量合計(度),電燈用戶數(戶),電力用戶數(戶),用戶數合計(戶),電燈(非營業用)用戶數(戶),電燈(營業用)用戶數(戶),電燈平均電價(元),電力平均電價(元),平均電價合計(元)
- During: 1951 - 2020
- Time Resolution: year
### 行業別用電
- Fields: 行業別大類,行業別中類,行業別小類,1月,2月,3月,4月,5月,6月,7月,8月,9月,10月,11月,12月
- During: 2016 - 2020
- Time Resolution: month
### 我國與鄰近國家電價比較-2014
- Fields: 國別,平均電價
- During: 2014
- Time Resolution: year
### 我國與鄰近國家電價比較-2019
- Fields: 年度,住宅用電-排名,住宅用電-國別,住宅用電-電價(台幣元/度),工業用電-排名,工業用電-國別,工業用電-平均電價(台幣元/度)
- During: 2019
- Time Resolution: year
### 國內歷次調整之電價
- Fields: 調整日期,項目,單位,數量
- During: 1979 - 2018
- Time Resolution:  year
### 各區域間過去電力潮流量
- Fields: 時間,流向,流量
- During: 20201101 - 20210131 
- Time Resolution: 10 mins
### 用電戶數
### 用電度數
### 南部科學園區用電
### 歷年尖峰負載與備用容量率

### Condition
- 供電充裕(綠燈): 備轉容量率大於10%
- 供電吃緊(黃燈): 備轉容量率10&~6%
- 供電警戒(橘燈): 備轉容量率小於6%
- 限電警戒(紅燈): 備轉容量90萬千瓦以下
- 限電準備(黑燈): 備轉容量50萬千瓦以下

### 期末學習的項目
- [x] Pandas
- [x] Matplotlib/Seaborn -> Plotly
- [x] WebScrapping(requests)
- [ ] Feature Engineering
- [ ] Natural Language Processing
- [ ] Linear Regression
- [ ] Random Forest
- [ ] SVM
- [ ] Model Validation
- [ ] Hyper-Parameters
### 可分析項目與可執行項目
- [ ] Auto Sync From Opendata
- [x] Auto Sync To Database
- [x] 三年尖峰備轉容量疊圖分析
- [x] Web Site
- [x] 用電度數與電費、戶數Correlation分析(HeatMap)
- [ ] 2016 - 2020各月行業比例(Bar Chart)
- [ ] 2014電費與他國比較(Bar Chart)
- [ ] 電費調整歷史曲線(Line Chart)
- [ ] 各電廠每日發電配比(Stacked Histogram)
- [ ] 電力流向地圖(Geographic)
- [ ] 利用2020整年的資料訓練結果Fit至2021年預估發電量與附載量，看準度
  - Goals: 移動的Window(Time Series)預測下一天
  - Data: 採下方Data Table的
  - Models:
    - [ ] SVM Regression
    - [ ] Linear Regression
    - [ ] Random Forest Regression
    - [ ] Cluster
    - [ ] LSTM(課外)
  - Problems:
    - [ ] 移動的Window(Time Series)怎麼放進Model?
- [ ] 爬取輿料 + JeiBa
### 困難的點(打勾是已解決)
- [x] 資料前處理與Pipeline設計
- [ ] 對ML不那麼熟悉
- [ ] 時間QQ

## Future Work
### 天氣影響用電量
- 因素：
  - 溫度 -> 冷暖氣
- 作法與可能性：
  - 將天氣要素列入考量，使得天氣要素能夠影響模型結果
### 工業區影響用電量
- 因素：
  - 工業區可能包含台積電等等大廠，他們的用電量可能將受季度影響。
- 做法與可能性：
  - 能將工業區的資料挑選出來分別分析、分類與預測
