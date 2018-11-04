# -*- coding: UTF-8 -*-
from m0_BAIDU_py3_Firefox_LINUX  import BAIDU_INDEX

ID = "manggny"
PW = "ljg0707"
#KEYWORD = "%CE%ED%F6%B2"
KEYWORD = "%C9%A4%D7%D3%CC%DB"
outFILE = "BAIDU_SangZiTeng2014-18.txt"


URL="http://index.baidu.com/?tpl=trend&type=0&area=514&time=13&word="+KEYWORD
#start_year="2018"
#start_month="05"
#end_month="08"
xposition=73
yposition=282
endx=1500
baidu = BAIDU_INDEX()
baidu.AWAKE_BROWSER(filename=outFILE)
baidu.SEARCH_test()
baidu.LOGIN_BAIDU(ID, PW)
#baidu.ACCESS_URL(URL,"2014","01","04",xposition,yposition,endx)
#baidu.ACCESS_URL(URL,"2014","05","08",xposition,yposition,endx)
#baidu.ACCESS_URL(URL,"2014","09","12",xposition,yposition,endx)
#baidu.ACCESS_URL(URL,"2015","01","04",xposition,yposition,endx)
#baidu.ACCESS_URL(URL,"2015","05","08",xposition,yposition,endx)
baidu.ACCESS_URL(URL,"2015","09","12",xposition,yposition,endx)
#baidu.ACCESS_URL(URL,"2016","01","04",xposition,yposition,endx)
#baidu.ACCESS_URL(URL,"2016","05","08",xposition,yposition,endx)
#baidu.ACCESS_URL(URL,"2016","09","12",xposition,yposition,endx)
#baidu.ACCESS_URL(URL,"2017","01","04",xposition,yposition,endx)
#baidu.ACCESS_URL(URL,"2017","05","08",xposition,yposition,endx)
#baidu.ACCESS_URL(URL,"2017","09","12",xposition,yposition,endx)
#baidu.ACCESS_URL(URL,"2018","01","04",xposition,yposition,endx)
#baidu.ACCESS_URL(URL,"2014","01","04",xposition,yposition,endx)



#baidu.QUIT()

