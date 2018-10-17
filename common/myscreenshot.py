import time
import os


def cappic(driver):
   pt=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
   #picname=os.path.dirname(os.path.abspath('.'))+'\\pic\\'+pt+'.png'

   picname = os.path.abspath('.') + '\\pic\\' + pt + '.png'
   driver.get_screenshot_as_file(picname)
