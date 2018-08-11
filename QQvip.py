import selenium
from selenium import webdriver
import time

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
driver.find_element_by_id('u').send_keys('760832791')
driver.find_element_by_id('p').clear()
#密码
driver.find_element_by_id('p').send_keys('******')
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
#退出窗口
driver.quit()