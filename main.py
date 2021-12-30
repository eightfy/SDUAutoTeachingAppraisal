from selenium import webdriver
import time
driver = webdriver.Chrome()    # Chrome浏览器，其他浏览器可以自行更改，注意webdriver驱动文件的版本和浏览器版本必须一致
driver.get("http://bkzhjx.wh.sdu.edu.cn/sso.jsp")
driver.find_element_by_id("un").send_keys("这里是账号")
driver.find_element_by_id("pd").send_keys("这里是密码")
driver.find_element_by_id("index_login_btn").click()
driver.get("https://bkzhjx.wh.sdu.edu.cn/jsxsd/xspj/xspj_list.do?pj0502id=300F24305CEF4E34971459031FE47844&pj01id=5B553149F48E455CA92D268FAA448A31&xnxq01id=2021-2022-1")
#这个链接这学期用完下学期就不能用了XD有空再改成通用的
for x in range(2,20):
    driver.find_element_by_xpath(f"/html/body/div/div[1]/form/table/tbody/tr[{x}]/td[9]/a").click()
    for y in range(3,40,2):         # 数目按照需要评价的科目数调整，从2开始
        driver.find_element_by_xpath(f"/html/body/div/div/form/table[1]/tbody/tr[{y}]/td[2]/label[1]/i").click()
    driver.find_element_by_xpath("//*[@id='table1']/tbody/tr[41]/td[2]/label[2]/i").click()
    driver.find_element_by_xpath("/html/body/div/div/form/table[1]/tbody/tr[42]/td[2]/span/label[3]/i").click()
    driver.find_element_by_xpath("/html/body/div/div/form/table[1]/tbody/tr[43]/td[2]/label[1]/i").click()
    driver.find_element_by_id("tj").click()
    al = driver.switch_to.alert
    al.accept()
    time.sleep(2)
    al = driver.switch_to.alert
    al.accept()
    time.sleep(2)