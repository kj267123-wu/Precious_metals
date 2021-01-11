import requests
import parsel
import re

url = 'http://www.icbc.com.cn/ICBCDynamicSite/Charts/GoldTendencyPicture.aspx'
req = requests.get(url = url)
data = req.text
sel = parsel.Selector(data) 
forecast_name_all = sel.xpath('//*[@id="TABLE1"]/tbody')[0]
forecast_name_all = forecast_name_all.xpath('./tr')
forecast_all = []
#id_all = [901,903,905,907,801,803,805,807]

for forecast_id in enumerate(forecast_name_all):
    if forecast_id[0] == 0:
        continue
    forecast_one_data = {}
    forecast_one = forecast_name_all[forecast_id[0]]
    name = forecast_one.xpath('./td[1]/text()').get()
    name = re.sub(u"([^\u4e00-\u9fa5])","",name)     #提取汉字
    Selling_price = forecast_one.xpath('./td[4]/text()').get()
    Selling_price = re.findall(r"\d+\.?\d*",Selling_price)   #提取数字     
    buying_price = forecast_one.xpath('./td[3]/text()').get()
    buying_price = re.findall(r"\d+\.?\d*",buying_price)   #提取数字         
    forecast_one_data['品种'] = name
    forecast_one_data['银行卖出价'] = Selling_price[0]
    forecast_one_data['银行买入价'] = buying_price[0]
    forecast_all.append(forecast_one_data)

a = 1