# Arduino-da

注意事項：

在Arduino端，用以判別是不是新進來的ODF value的變數 incomming_ODFname，其用以存放的字串陣列長度，必須為10 bytes。
For example:  char incomming[10]={'\0'};

而從Bridge中取回incomming_ODFname時，也要定義取出長度為10 bytes
For example:  Bridge.get("incomming_ODFname",  incomming, 10);

這是因為用起判定是否為新資料的變數incomming_ODFname，是一個序列數字介於 0~10000，序列數字不同時，代表ODFname內有新資料需取回。
