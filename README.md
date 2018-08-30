# Arduino-da

2018.8.30: 加入SSL通訊、Device認證程序

注意事項：

Arduino那邊取完ODF在bridge的數值後，要會回填 "" 到ODF對應的bridge去覆蓋。  是以之後每次檢查bridge中ODF字串值若為 "" 則表示數值沒更新。

For example  (Arduino的取資料端範例)

    Bridge.get(ODF_name,  valueStr, 3);
    
    if (strcmp(valueStr,"") != 0){
     
        
        //邏輯程式碼....


        Bridge.put(ODF_name, "");  //<--- 做完後，要回填 "" 覆蓋。
    }
