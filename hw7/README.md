# HW7

## P1
### Description
請利用TrialHandler產生一個三因子的實驗嘗試列表，
三個因子分別為聲調高低、聲音長短 、聲音大小，
每個情況的組合有20個嘗試，為每個嘗試隨機填入反應選擇 (高音／低音)以及反應時間後，
最後將所有資料存入一個資料檔。
### Thought Process
1. 先建立stim_list，並且放入trial_handler之中
2. 把每隔trial利用Mock跑過一遍
3. 儲存檔案

## P2
### Description
請利用前一題之Trial列表設定搭配psychopy，實際呈現Trial list中每個嘗試的聲音，讓受試者作判斷。
### Thought Process
1. Extending from HW6，因為有了TrialHandler的幫忙，我將BaseTrial這個Model改寫為負責管控psychopy object的controller
