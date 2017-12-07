"""

selenium中文文档:        http://selenium-python-zh.readthedocs.io/en/latest/index.html

阅读延伸---虫师的博客:     http://www.cnblogs.com/fnng/

本笔记涉及的内容有:
1.selenium介绍
2.selenium快速入门
3.窗口与框架
4.等待页面加载
5.待续

"""

from selenium import webdriver


###############
# 1.selenium介绍
###############

"""

Selenium是一个Web的自动化测试工具, 最初是为网站自动化测试而开发的,
但是由于ajax等动态加载html技术的兴起, selenium也被各位大佬用在了爬取网页数据的用途上,
Selenium可以直接运行在浏览器上, 可以支持所有主流的浏览器(包括无界面浏览器),
可以接受指令, 让浏览器自动加载页面, 获取需要的数据, 甚至页面截屏

无界面浏览器: PhantomJS, 会把网站加载到内存并执行页面上的javascript, 因为在内存中加载并无法显示出效果

"""


###################
# 2.selenium快速入门
###################

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 发起请求
driver.get('http://www.baidu.com')

# 保存快照
driver.save_screenshot('baidu.png')

# 定位到节点输入--也就是在百度搜海贼王
driver.find_element_by_id("kw").send_keys("海贼王")   # 能输入的节点才可以使用send_keys,
driver.find_element_by_id("su").click()

# 关闭浏览器
driver.close()     # 退出界面
driver.quit()      # 退出浏览器

"""

webdriver可以创建许多浏览器对象, 但是必须要先下载浏览器驱动
因为我们写的脚本是去操作驱动, 让驱动去操纵浏览器, 而不是直接操纵浏览器

浏览器对象的方法
1.查看请求信息
driver.page_source     # 获取源码
driver.get_cookies     # 获取浏览器中存储的cookies
driver.current_url     # 查看当前的url

2.退出
driver.close()          # 退出当前页面
driver.quit()           # 退出浏览器

3.页面元素定位
find_element_by_id                  # 使用id值定位一个元素
find_element_by_xpath               # 使用xpath值定位一个元素
find_element_by_link_text           # 使用文本定位一个元素
find_element_by_partial_link_text   # 使用部分文本定位一个元素
find_element_by_tag_name            # 使用标签名定位一个元素
find_element_by_class_name          # 使用class属性值定位一个元素
find_element_by_css_selector        # 使用css选择器定位一个元素
(同时还有find_elements_by_xxxx)

element 和 elements  的区别是 返回一个数据, 和返回一列表数据
by_link_text 和 by_partial_link_text 的区别是    全部文本和包含某个的文本
如果从定位到的节点中获取属性和文本的方法:
1.get_attribute()   获取属性值
2.text              获取标签名

4.cookies
driver.get_cookies()       可以获取所有cookies,返回一个列表
for cookie in cookies:      能够遍历获取所有cookie, 通过键值对取出 {cookie['name']:cookie['value']}

driver.delete_cookie('CookieName')     根据cookie名删除单个cookie
driver.delete_all_cookies()            删除所有cookies

"""


############
# 3.窗口与框架
############

"""

对于弹出页面的处理:
driver.window_handles      获取所有的窗口列表
driver.switch_to           切换到某一窗口

有些html源码会放进iframe框架中
Iframe框架的处理:
el = driver.find_element_by_xpath()    定位到框架中
driver.switch_to_frame(el)              进入框架

"""


##############
# 4.等待页面加载
##############


"""

如果一个网站使用了动态html技术, 那么页面上的部分元素出现时间不确定
而为了精确定位到元素, 需要进行页面等待

强制等待:   time.sleep()

显式等待:   指定一个条件设置等待时间, 如果没有找到或者等待超过设置的时间会抛出一个异常
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )

隐式等待:   设置一个等待时间期限, 超出等待时间后再去寻找元素, 单位为秒
driver.implicitly_wait(10)

"""