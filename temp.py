# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#
import xlwt
import datetime
import mysql.connector
from bs4 import BeautifulSoup
import urllib.request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
#
mydb = mysql.connector.connect(
  host="10.1.205.224",
  port="3306",
  user="lxc",
  passwd="lxc",
  database="irpa"
)
#
# SMTP
mail_host = "smtp.163.com" # 设置服务器
#发送方邮箱
mail_user = "m13261740842@163.com" #用户名
mail_pass = "ASDURZJJOGVTGFBQ" # 口令

sender = 'm13261740842@163.com' #发送者名称
receivers = '2499714067@qq.com'  # 接收邮件地址
#
Excel_name = datetime.datetime.now().date().isoformat() + '外汇牌价.xls'
#


#
array = {'货币名称':'','现汇买入价':'','现钞买入价':'',
                 '现汇卖出价':'','现钞卖出价':'','中行折算价':'',
                 '发布日期':'','发布时间':''}

def write_mysql(tables):
    for i in tables:
        mycursor = mydb.cursor()
        sql = "INSERT INTO test (name, exchange_buy, cash_buy, exchange_sell, cash_sell, conversion_price, time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (i['货币名称'], i['现汇买入价'], i['现钞买入价'], i['现汇卖出价'], i['现钞卖出价'], i['中行折算价'], i['发布日期'])
        mycursor.execute(sql, val)
        mydb.commit()

def web_download():
    tables = []
    url = "https://www.boc.cn/sourcedb/whpj/index.html"
    response1 = urllib.request.urlopen(url)
    html = response1.read()
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding = 'utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    #soup = BeautifulSoup(open(r'C:\Users\mobvoi\.spyder-py3\中国银行_金融市场_外汇牌价.html','rb'))
    soup = BeautifulSoup(html,features="lxml")
    soup1 = soup.select('table[align="left"]')
    x = soup1[0].text
    #print (x)
    list1 = x.splitlines()
    del list1[0:2]
    for i in range(0,len(list1),10):
        for j,k in zip(range(8),array):
            worksheet.write(int(i/10),j, label = list1[i+j])
            array[k] = list1[i+j]
        if i !=0:
            tables.append(array.copy())
      
    workbook.save(Excel_name)
    return tables        
def smtp_send():
    #创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header(sender, 'utf-8')
    message['To'] =  Header(receivers)
    subject = '外汇牌价表格'
    message['Subject'] = Header(subject, 'utf-8')
    #邮件正文内容
    message.attach(MIMEText('外汇牌价表格发送邮件', 'plain', 'utf-8'))
    # 构造附件1，传送当前目录下的 Excel 
    file_excel = open(Excel_name, 'rb')
    att1 = MIMEText(file_excel.read(), 'base64', 'utf-8')
    file_excel.close()
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="Excel_test.xls"'
    message.attach(att1)
     
    
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.connect(mail_host, 465) # SMTP端口号
        smtpObj.login(mail_user, mail_pass) #会返回(状态码, "字符串解释")元组信息
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
        
def airtask():
    write_mysql(web_download())
    smtp_send()
        
if __name__ == '__main__':
    write_mysql(web_download())
    smtp_send()


	
