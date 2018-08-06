# Arduino-da

注意事項：

Arduino那邊取完ODF數值後，要會回填 "" 到DF去覆蓋。  每次檢查ODF字串若為 "" 則表示數值沒更新。

For example  (Arduino的取資料端範例)

    Bridge.get(StrBuf,  valueStr, 3);
    
    if (strcmp(valueStr,"") != 0){
     
        
        //邏輯程式碼....


        Bridge.put(StrBuf, "");  //<--- 做完後，要回填 "" 覆蓋。
    }
