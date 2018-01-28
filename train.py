
import time,os
import requests

headers = {"Accept":"*/*",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
"Host":"kyfw.12306.cn",
"If-Modified-Since":'0',
"Referer":"https://kyfw.12306.cn/otn/leftTicket/init",
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
"X-Requested-With":"XMLHttpRequest"
}
link = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-24&leftTicketDTO.from_station=KMM&leftTicketDTO.to_station=JBH&purpose_codes=ADULT'
#link = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-24&leftTicketDTO.from_station=JBH&leftTicketDTO.to_station=KMM&purpose_codes=ADULT'
def get_msg():
    try:
        response = requests.get(link, headers=headers, timeout=3)
        data = response.json().get('data')
        result = data.get('result')
        station = data.get('map')
        rel = []
        for line in result:
            item = line.split('|')

            if 'G1376'==item[3]:
                msg = '''    昆明 － 金华(1月24)
-----------------------
    车次:{3}
    时间:{8}-{9}
    历时:{10}
    特等座: {30}  
    一等座: {31}  
    二等座: {32}  '''.format(*item)
                rel.append(msg)
        return rel
    except:
        pass

def main():
    while 1:
        msgs = get_msg()
        if not msgs:
            continue
        for msg in msgs:
            # apt install gnome-osd
            os.system('''gnome-osd-client -f "<message id='bibi' osd_halignment='right' ><span color='#FFFFB9'>%s</span></message>"'''%msg)
        time.sleep(3)

if __name__ == '__main__':
    main()
