from time import sleep
from drivers.init_drivers import init_driver_my
from time import sleep


def get_set_prof(driver, url_http:str) -> set:
    driver.get(url_http)
    key_go = True
    set_prof = set()
    k = 0
    while key_go :
        l_tr = driver.find_elements_by_xpath('//table//tr')
        for row in l_tr[1:]:
            l_col = row.find_elements_by_xpath('.//*')
            print(l_col[2].text)
            set_prof.add(l_col[2].text.strip())
        try:
            k +=1
            print('page = ', str(k))
            butt = driver.find_element_by_xpath('//div[@id = "pager-nav"]//li[@class="next"]/a')
            butt.click()
            sleep(7)
            
        except Exception:
            key_go = False
    return set_prof


def write_result(set_prof:set):
    f_r = open('list_slug.csv', 'w')
    for line in set_prof:
        f_r.write(line+'\n')
        
        
if __name__ == "__main__":
    
    driver = init_driver_my()
    set_prof = get_set_prof(driver, 'https://etks.info/okpdtr/office')
    write_result(set_prof)