
# #
# #app["Контрагенты"].Click()
# #click(path+"Kontragents.png") # Контрагенты найти
# #click(path+"Kontragents.png") # Контрагенты нажать
# # # wait(path+"KontragentsMenu.png", 2) # Maybe the Start menu is slow
# # click(path+"Prosmotr.png") # Просмотр

# # click(path+"FizLico.png") # Физическое лицо
# #app.child_window(best_match="Контрагенты").OK()
# #dlg.edit.type_keys("pywinauto Works!", with_spaces = True)
# #dlg.print_control_identifiers()
#
# #dlg.Properties.OK.click()
# #dlg.edit2.type_keys("pywinauto Works!", with_spaces = True)
#
# #print_control_identifiers()
# app = Application().Connect(title=u'AdInsure VSK-Test - \u0422\u0415\u0421\u0422-VSK', class_name='WindowsForms10.Window.8.app.0.cabf07_r9_ad1')
# main = app[u'AdInsure VSK-Test - \u0422\u0415\u0421\u0422-VSK']
# main2 = main.toolStrip1.Menu(u'\u041a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442\u044b')
#     #(title=u'\u041a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442\u044b')
# main2.click()

import time
from selenium import webdriver
import subprocess
#subprocess.Popen([r'C:\Users\maximk\Desktop\WiniumDesktopDriver\Winium.Desktop.Driver.exe', '--silent'])
#from keyboard import wait
from mouse import click
#from pywinauto.application import Application
#from lackey import *
#path = "C:\\Users\\maximk\\Desktop\\AutoGUI\\"

driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        "debugConnectToRunningApp": 'true',
        "app": r"C:\Users\maximk\Desktop\PROD\Program\Adacta.IIS.Client.exe"
    })
time.sleep(1)

window = driver.find_element_by_name('AdInsure VSK-PROD - ТЕСТ-VSK')
print ("Подключение к программе установлено")
time.sleep(1)
window.find_element_by_name('Контрагенты').click()
time.sleep(1)
window.find_element_by_name('Просмотр').click()
window.find_element_by_name('Добавить').click()
#click(path+"add.png") # Добавить
window.find_element_by_name('Физическое лицо').click()
