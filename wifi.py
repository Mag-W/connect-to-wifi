import pywifi
import time
import network
from pywifi import const
import win32api
from pymouse import PyMouse

wifi=pywifi.PyWiFi()
iface=wifi.interfaces()[0]
print(iface.name)

def check_connect():
    if iface.status() in [const.IFACE_CONNECTED,const.IFACE_INACTIVE]:
         print("connect successfully")
         return 1
    else:
        print("connect failed")
        return 0
iface.scan()
time.sleep(1)
'''
basewifi=iface.scan_results()
for i in basewifi:
    print('wifi扫苗结果:{}'.format(i.ssid)) # ssid 为wifi名称

    print('wifi设备MAC地址:{}'.format(i.bssid))
'''
profile=pywifi.Profile()
profile.ssid='scut-student'
profile.auth = const.AUTH_ALG_OPEN
#profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_NONE
#profile.key = ''


iface.remove_all_network_profiles()
tmp_profile = iface.add_network_profile(profile)

iface.connect(tmp_profile)
time.sleep(5)
assert iface.status() == const.IFACE_CONNECTED

'''
iface.disconnect()
time.sleep(1)
assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
'''
check_connect()

win32api.ShellExecute(0, 'open', 'https://s.scut.edu.cn/a79.htm?wlanuserip=172.28.138.37&wlanacname=dongxiqu%2DAC&wlanacip=172%2E26%2E79%2E253&usermac=0C-DD-24-8C-13-06', '','',1)
42

time.sleep(3)
m = PyMouse()
m.click(950, 580)
time.sleep(1)
m.click(1890,20)
