import selenium
from selenium import webdriver
import time
import re

qq=input('请输入qq:')
key=input('请输入密码:')
driver = webdriver.Firefox()

#设置浏览器大小
driver.maximize_window()

#打开页面
driver.get('http://vip.qq.com/club/act/2018/2000296038/b1323a462c.html')
#点击登陆
driver.find_element_by_id('menu-login-btn').click()
time.sleep(2)

#执行登录
iframe=driver.find_element_by_xpath("//iframe[contains(@src,'xui')]")
driver.switch_to.frame(iframe)
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').clear()
#账号
driver.find_element_by_id('u').send_keys(qq)
driver.find_element_by_id('p').clear()
#密码
driver.find_element_by_id('p').send_keys(key)
driver.find_element_by_id('login_button').click()
driver.switch_to.default_content()
time.sleep(2)
#点击领取
driver.find_element_by_id('cmp33482').click()
#选择区角色
driver.find_element_by_class_name('area_select').find_element_by_xpath("//option[@value='19']").click()
driver.find_element_by_class_name('svr_select').find_element_by_xpath("//option[@value='95']").click()
driver.find_element_by_class_name('role_select').find_element_by_xpath("//option[@value='8003226']").click()
driver.find_element_by_class_name('btn_fit_em_pop ').click()
driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/a').click()
#累计天数奖励
driver.find_element_by_xpath('//*[@id="cmp33511"]').click()
time.sleep(2)
daystext=driver.find_element_by_xpath('/html/body/div[11]/div/div[2]/div/p').get_attribute('textContent')
days=re.findall(r'[0-9]+',daystext)
days=int(days[0])
driver.find_element_by_xpath('/html/body/div[11]/div/div[3]/a').click()
if days>=20:
    driver.find_element_by_xpath('//*[@id="cmp33487"]').click()
    driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/a[1]').click()
    driver.find_element_by_xpath('/html/body/div[11]/div/div[3]/a').click()
elif days>=15:
    driver.find_element_by_xpath('//*[@id="cmp33486"]').click()
    driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/a[1]').click()
    driver.find_element_by_xpath('/html/body/div[11]/div/div[3]/a').click()
elif days>=10:
    driver.find_element_by_xpath('//*[@id="cmp33485"]').click()
    driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/a[1]').click()
    driver.find_element_by_xpath('/html/body/div[11]/div/div[3]/a').click()
elif days>=6:
    driver.find_element_by_xpath('//*[@id="cmp33484"]').click()
    driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/a[1]').click()
    driver.find_element_by_xpath('/html/body/div[11]/div/div[3]/a').click()
elif days>=3:
    driver.find_element_by_xpath('//*[@id="cmp33483"]').click()
    driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/a[1]').click()
    driver.find_element_by_xpath('/html/body/div[11]/div/div[3]/a').click()
#退出窗口
driver.quit()