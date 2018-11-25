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


針對 ArduinoYun (第一版)，在OpenWRT上安裝Python套件 requests 的指令(依序) (使用Yun第一版前，需要把韌體刷到1.5.3版)


    opkg update                 #updates the available packages list

    opkg install distribute     #it contains the easy_install command line tool

    opkg install python-openssl #adds ssl support to python

    easy_install https://files.pythonhosted.org/packages/ae/e8/2340d46ecadb1692a1e455f13f75e596d4eab3d11a57446f08259dee8f02/pip-10.0.1.tar.gz#sha256=f2bd08e0cd1b06e10218feaf6fef299f473ba706582eb3bd9d52203fdbd7ee68

    pip install requests

    opkg install openssh-sftp-server

針對 ArduinoYun Rev2，在OpenWRT上安裝Python套件 requests 的指令(依序) (Rev2拿到後直接可以使用，無須刷韌體)

    For Rev2:
    opkg update
    opkg install python-pip
    pip install requests    (斷電重開機後執行，不然一定會發生記憶體不足 Memory error)
    opkg install openssh-sftp-server

    註：上述順序不可改。 如果裝requests時一直發生memory error記憶體不足，
    可試著手動依序安裝 idna, urllib3, chardet, certifi, requests 
    一旦遭遇記憶體不足就斷電重開機後執行後再繼續裝，
    如果怎樣都裝不起來，只能Factory reset後再試試看。
