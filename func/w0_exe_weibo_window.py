import sys 
import time
#sys.path.append("/Users/leejunho/Desktop/git/python3Env/group_study/project_pre/func")
from w0_WEIBO_window import WEIBO

ID_junho = ""
PASSWD_junho = ""

weibo = WEIBO()
weibo.AWAKE_BROWSER(filename = "PM_20180401_test.txt")
weibo.LOGIN(ID=ID_junho,PASSWD=PASSWD_junho)

year = 2018
day = 31
month = 3
for i in range(30):
    INFO =  weibo.DATE_MAKER(year,month,day)
    for j in range(18):
        if(j<=8):
            LOC_NUM = j+1
        elif(j<=15):
            LOC_NUM = j+2
        else:
            LOC_NUM = j+12
        for PG in range(50):
            web_page = weibo.MAKE_WEIBO_URL(INFO,LOCAL_NUM = LOC_NUM ,PAGE=PG+1); #print(web_page)
            CONTI = weibo.ACCESS_URL(web_page)
            print ("!!!!! Until Current page, cumulated keyword number : ",weibo.COUNT)
            print ("!!!!! District Number : ", LOC_NUM)
            print ("!!!!! Page Number : ", PG+1)
            print (""); print ("")
            if(CONTI == 0):
                break
    print (" * TOTAL COUNT NUM OF PM WORD : ",weibo.COUNT)
    INFO_STR = weibo.MAKE_DATE_STR(INFO)
    INPUT_LIST = [INFO_STR[3], weibo.COUNT]
    weibo.CREATE_n_WRITE_INTO_TXT(INPUT_LIST)
    weibo.GERP_WORD_to_zero()
    month = INFO[1]
    day = INFO[2]+1
weibo.QUIT()

'''
weibo_test = WEIBO()
weibo_test.AWAKE_BROWSER()


weibo_test.QUIT()
'''