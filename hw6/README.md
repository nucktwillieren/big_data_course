# HW6

## P1
### Description
將螢幕任意劃分為八個不相重疊的區域，當滑鼠游標移到某個區域時，在螢幕正中內顯示該區域的編號。
### Thought Process
1. 八個不相重疊的區域，我認為可以直接利用RectShape的方式做方塊區域切割
2. 先設計演算法自動演算各個區塊所相對應的位置，並且建立RectShape到該位置上
3. 最後利用eventloop的方式去抓Shape Contains Mouse的條件表達，偵測游標是否滑動到某區塊了
4. 若是滑動到某個區塊，即可改變中心顯示之數值。

## P2
### Description
備一個雙字詞列表，其中有五個動物名稱、五個水果名稱；
安排一個作業，共有十個嘗試(trial)；
每個嘗試會在螢幕正中央呈現一個上述列表中的詞（每個表中的詞都會被呈現），
受試者在每個嘗試中需判斷該詞彙是動物或水果，反應時間與正確率會被記錄，
於完成 十個嘗試後即結束作業，並且將結果輸出至檔案中留存。
### Thought Process
1. 我認為可以利用mixins design pattern讓整個Trial有順序架構
2. 順序是load trial data -> setup -> hint -> 
run though all turns and save all single turns-> save_all -> analyze -> save analysis
### About result files
- data.json存放的是每個turn的結果，包含反應時間、正確答案、題目內容、題目的種類及正確與否
- success_rate_analysis是存放正確率的地方，他會在所有turn的result算完才開始算。
