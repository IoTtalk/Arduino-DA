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

    opkg update
    
    opkg install openssh-sftp-server
    
    opkg install python-pip
    
    pip install requests    (重開機後再執行，不然很容易記憶體不足而發生 Memory error)
