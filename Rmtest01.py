import logging

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import json
from config import cookie
from selenium.webdriver.support.wait import WebDriverWait
from log import logdef


#创建驱动对象
wb = webdriver.Chrome()

wb.get('http://sb-ope.moyuai.com.cn/login')

cookie = wb.get_cookies()
cookie1 = json.dumps(cookie)
print(cookie1)
# with open(r'D:\pyselenium\testcase\text.txt','w') as f:
#     f.write(cookie1)

#wb.switch_to.frame("iframe_name_or_id")
# input1 = WebDriverWait(wb, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="account"]'))
# )

#通过ID获取账号输入框
input1 = WebDriverWait(wb, 10).until(
    EC.presence_of_element_located((By.ID, 'account'))
)
time.sleep(10)

#input1 = wb.find_elements(By.XPATH,'//*[@id="account"]')
print(input1)
input1.click()
input1.send_keys('zhanghao1')

#通过id获取密码输入框password
inpt_sec = wb.find_element(By.ID,'password')
inpt_sec.click()
inpt_sec.send_keys('secret')

#通过xpath定位登录按钮
log_button = wb.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/form/button/span')
log_button.click()

time.sleep(1)
#获取弹窗信息 /div/div/div/span[2]
#错误：用户名或密码错误
e_info = wb.find_element(By.XPATH,'/html/body/div[2]/div/div/div/span[2]')
print(e_info)
print(e_info.text)
assert e_info.text =='用户名或密码错误'
print('登录失败')
log_info1 = 'Case1:登录失败，pass'
logdef.print_log(log_info1)



#获取当前页面的URL
url = wb.current_url
print('url=',url)

#刷新页面
wb.refresh()
#成功登录,输入账号
input2 = WebDriverWait(wb, 10).until(
    EC.presence_of_element_located((By.ID, 'account'))
)
time.sleep(10)
#input1 = wb.find_elements(By.XPATH,'//*[@id="account"]')
print(input2)
input2.click()
input2.send_keys('tester2')

#通过id获取密码输入框password
inpt_sec1 = wb.find_element(By.ID,'password')
inpt_sec1.click()
inpt_sec1.send_keys('ope123456')

#点击登录
log_button = wb.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/form/button/span')
log_button.click()
time.sleep(1)

#获取当前登录成功的弹窗跳转的url
e_info1 = wb.find_element(By.XPATH,'/html/body/div[2]/div/div/div/span[2]')
print(e_info1)
print(e_info1.text)
su_info = e_info1.text
time.sleep(10)

url1 = wb.current_url
print('跳转后url=',url1)

assert su_info == '登录成功' and url1 == "http://sb-ope.moyuai.com.cn/"
print('成功登录')
log_info2 = 'Case2:登录成功，pass'
logdef.print_log(log_info2)

time.sleep(3)

wb.quit()