# 获取百度一下页面

# 导入 urllib
import urllib.request

# 1.  准备访问地址 http://baidu.com

url = " http://www.baidu.com/"

# 2. 模拟浏览器访问地址
response = urllib.request.urlopen(url)

# 3. 获取响应中的页面源码

content = response.read().decode('utf-8')

# 4. 打印数据
print(content)