from selenium import webdriver
from sys import platform
import requests
import wget
import zipfile
import os

def install_chromedriver(driver_version, os_platform, drivers_path):
    if os_platform == 'linux':
        os_platform += '64'
        if os.path.exists(drivers_path + '/chromedriver'):
            os.remove(drivers_path + '/chromedriver')
            print('Старый драйвер удален')
    else:
        if os.path.exists(drivers_path + '/chromedriver.exe'):
            os.remove(drivers_path + '/chromedriver.exe')
            print('Старый драйвер удален')
    print(os_platform)
    download_url = "https://chromedriver.storage.googleapis.com/" + driver_version + f"/chromedriver_{os_platform}.zip"
    latest_driver_zip = wget.download(download_url, 'chromedriver.zip')

    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        print('Распаковка', latest_driver_zip)
        print(drivers_path)
        zip_ref.extractall(path=drivers_path)
    os.remove(latest_driver_zip)

def get_latest_driver_version():
    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    return response.text

def init_driver(browser, vision = False):
    """
    Инициализация драйвера
    :param browser: Название браузеров GoogleChrome Firefox
    :return:
    """
    path = os.getcwd().split('/drivers/')[0]
    full_path_chrome = path + '/chromedriver/chromedriver'
    full_path_to_drivers = path + '/chromedriver'

    if platform == "win32":
        full_path_chrome += '.exe'

    full_path_fire = os.path.abspath('geckodriver')
    if browser == "GoogleChrome":
        options_chr = webdriver.ChromeOptions()
        if not vision:
            options_chr.add_argument('headless')
        #options_chr.add_experimental_option('prefs',{'geolocation': True})
        version_number = get_latest_driver_version()
        if not os.path.exists(full_path_chrome):
            print('Такого файла нет')
            install_chromedriver(version_number, platform, full_path_to_drivers)
        driver = webdriver.Chrome(full_path_chrome, options=options_chr)
        print(driver.capabilities['browserVersion'], version_number)
        if driver.capabilities['browserVersion'] != version_number:
            print('Версия драйвера устарела')
            try:
                install_chromedriver(version_number, platform, full_path_to_drivers)
                driver = webdriver.Chrome(full_path_chrome, options=options_chr)
            except PermissionError as e:
                print(e)

    if browser == "Firefox":
        options_fier = webdriver.FirefoxOptions()
        options_fier.profile('/home/al/.mozilla/firefox/yysvauj1.default-release')
        # options_fier.set_headless()
        # assert options_fier.headless
        driver = webdriver.Firefox(executable_path=full_path_fire, options=options_fier)

    return driver


def init_drivers(browser="GoogleChrome", kol=1, vis = False):
    drivers=[]
    for i in range(kol):
        drivers.append(init_driver(browser, vis))
    return drivers

def init_driver_my(browser="GoogleChrome", vision=False):
    """
    Инициализация драйвера
    :param brauser: Название браузеров GoogleChrome Firefox
    :return:
    """
    full_path=os.path.abspath('/home/al/Projects_My/NLP-russian-language/NLP_gansior/professions/get_information/chromedriver/chromedriver')
    if browser=="GoogleChrome":
        chrome_options = webdriver.ChromeOptions()
        if not vision:
            chrome_options.add_argument('headless')
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        driver = webdriver.Chrome(full_path, options=chrome_options)
    if browser == "Firefox":
        print("Firefox not here.")
    return driver


# def geoloc():
#     # access_token = '123456789abc'
#     # handler = ipinfo.getHandler(access_token)
#     # details = handler.getDetails()
#     # print(details.city)
#     import socket
#     import fcntl
#     import struct
#     name = socket.gethostname()
#     id_address = socket.gethostbyname(name)
#     print("id_address = {0}".format(id_address))
#     ifname='eth0'
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.connect(("8.8.8.8", 80))
#     print(s.getsockname()[0])
#     print(s.getsockname()[1])
#     from subprocess import check_output
#     ips = check_output(['hostname', '--all-ip-addresses'])
#     print(ips)
#     f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
#     print('your_ip =', f.read())
#     ipv4 = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
#     ipv6 = os.popen('ip addr show eth0').read().split("inet6 ")[1].split("/")[0]
#     print('ipv4 = ',ipv4)
#     print('ipv6 = ', ipv6)


#
# import pymysql
# def config_mysql():
#     con = pymysql.connect('localhost', 'root', 'GANsiBR586!', 'helpify_ml')
#     cur = con.cursor()
#     return con,cur

# block test
if __name__ == "__main__":
    # driver = init_drivers()[0]
    print(install_chromedriver('91.0.4472.101', 'linux', r'C:\Users\Vbano\PycharmProjects\online_observation_sistem_business\app\drivers\chromedriver'))
    # driver.get('https://www.google.com')
    # print("Without visiual")
    # driver.close
    # driver = init_drivers(vis=True)[0]
    # driver.get('https://www.google.com')
    # driver.quit()

