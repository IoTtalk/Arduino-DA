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


在AR9331上面的OpenWRT上安裝Python套件 requests 的指令(依序)


    opkg update                 #updates the available packages list

    opkg install distribute     #it contains the easy_install command line tool

    opkg install python-openssl #adds ssl support to python

    easy_install https://files.pythonhosted.org/packages/ae/e8/2340d46ecadb1692a1e455f13f75e596d4eab3d11a57446f08259dee8f02/pip-10.0.1.tar.gz#sha256=f2bd08e0cd1b06e10218feaf6fef299f473ba706582eb3bd9d52203fdbd7ee68

    pip install requests

    opkg install openssh-sftp-server
