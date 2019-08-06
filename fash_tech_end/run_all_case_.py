# encoding: utf-8

# encoding: utf-8

import unittest
import time
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

def add_case(case_path):

    discover=unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    return discover

def run_case(all_case,report_path):

    '''执行所有的用例，并把结果写入测试报告'''
    # 把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）
    # 转化为格式化的时间字符串
    now=time.strftime("%Y_%m_%d_%H_%M_%S")
    report_abspath=os.path.join(report_path,now+"report.html")
    fp=open(report_abspath,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'fash_tech自动化报告',description=u'用例执行情况：')
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    '''获取最新的测试报告'''
    # os.listdir指定所有目录下所有的文件和目录名,
    # 以列表的形式全部列举出来，其中没有区分目录和文件。
    lists=os.listdir(report_path)
    # 重新按时间对目录下的文件进行排列
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
    print(u'最新测试生产的报告：' + lists[-1])
    report_file=os.path.join(report_path,lists[-1])
    return report_file


def send_email(sender,psw,receiver,smtpserver,report_file,):
    '''发送最新的测试报告内容'''
    # 读取测试报告的内容
    #-----------写邮件的主题------------
    with open(report_file,"rb") as f:
        mail_body=f.read()


    msg=MIMEMultipart('related')
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    msg["subject"]=u"fash-tech自动化测试报告(web)"+now
    boby = MIMEText(mail_body,'html','uft-8')
    msg["from"]=sender
    msg["to"]=receiver


    #正文
    msg["date"] = time.strftime('%a,%d %b %Y %H_%M_%S %z')
    msg.attach(boby)

    #附件
    att=MIMEText(open(report_file,"rb").read(),"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="report.html"'
    msg.attach(att)


    #---------发送邮件---------
    try:
        smtp=smtplib.SMTP()
        smtp.connect(smtpserver,25)#连接服务器
        smtp.login(sender,psw)#登录
    except:
        smtp=smtplib.SMTP_SSL(smtpserver,port)
        smtp.login(sender, psw)
    smtp.sendmail(sender,receiver,msg.as_string())#发送
    smtp.quit()#关闭
    print('test report email has send out!')



if __name__=="__main__":
    # case_dir = r"D:\Test\fash_tech\fash_tect_case"#用例路径
    case_path = r"D:\Test\fash_tech_end\TestCase"
    # report_path=r"D:\Test\fash_tech\fash_report_"# 生成测试报告的路径
    report_path = r"D:\Test\fash_tech_end\fash_report"  # 生成测试报告的路径
    all_case = add_case(case_path)  # 加载用例
    run_case(all_case, report_path)  # 执行用例
    report_file = get_report_file(report_path)  # 3.获叏最新的测试报告
    # ------------1.跟发文件相关的参数----------
    smtpserver = "smtp.qq.com"
    sender = "103779****@qq.com"
    psw = "eubwblfcy****"
    receiver="lar****ndial-d.com"
    port=0

    send_email(sender, psw, receiver, smtpserver, report_file)
















