from selenium import webdriver
from time import sleep
import datetime
import inspect
import os

def main():   
    ischecked = False    
    url_login = 'https://www.nike.com/kr/ko_kr/login'        
    xpath_size_header = '/html/body/section/section/section/article/article[2]/div/div[3]/div/div[2]/form/div[1]/div[2]/div[1]/div'
    xpath_buy = '//*[@id="btn-buy"]'
    xpath_license_agree = '//*[@id="btn-next"]'
    xpath_id = '//*[@id="j_username"]'
    xpath_password = '//*[@id="j_password"]'
    xpath_login_btn = '/html/body/section/section/div/div/div[2]/div/div[2]/div/button'
    xpath_btn_payment = '//*[@id="complete_checkout"]/button'
    xpath_checkbox_product_agree = '//*[@id="payment-review"]/div[1]/ul/li[2]/form/div/span/label/i'
    xpath_btn_check = 'button xlarge width-max'
    path_webdriver = os.path.dirname(inspect.stack()[1][1]) + '\\chromedriver.exe'    
    path_config = os.path.dirname(inspect.stack()[1][1]) + '\\config.txt'    

    str_config = ''
    str_temp = ''
    str_id = ''
    str_password = ''
    str_size = ''
    url_product_model = ''
    is_time_check = False
    file_config = open(path_config, mode='r')
    while (1):
        str_temp = file_config.readline()
        try:
            escape = str_temp.index('\n')
        except:
            escape = len(str_temp)     

        if str_temp:
            str_config = str_temp[0:escape]
            if str_config.find('nike_id=') >= 0:
                str_id = str_config.replace('nike_id=', '').strip()
            if str_config.find('nike_pw=') >= 0:
                str_password = str_config.replace('nike_pw=', '').strip()
            if str_config.find('shoes_size=') >= 0:
                str_size = str_config.replace('shoes_size=', '').strip()
            if str_config.find('shoes_url=') >= 0:
                url_product_model = str_config.replace('shoes_url=', '').strip()
            if str_config.find('is_time_check=') >= 0:
                if str_config.replace('is_time_check=', '') == 'True':
                    is_time_check = True
        else:
            break
    file_config.close()  

    if str_id == '':
        print('check config.txt file and id')
        return 0        
    if str_password == '':
        print('check config.txt file and password')
        return 0
    if str_size == '':
        print('check config.txt file and size')
        return 0
    if url_product_model == '':
        print('check config.txt file and url')
        return 0

    try:
        print('loading web driver')
        driver = webdriver.Chrome(path_webdriver)    
        driver.set_window_size(1300, 900)
        print('ready to web driver')
    except Exception as e:
        print(e)
        return 0    

    try:        
        driver.get(url_login)    
    except Exception as e:
        print(e)
        return 0   

    try:
        element_id = driver.find_elements_by_xpath(xpath_id)
        if len(element_id) > 0:      
            element_id[0].click()  
            element_id[0].send_keys(str_id)
        element_password = driver.find_elements_by_xpath(xpath_password)
        if len(element_password) > 0:      
            element_password[0].click()  
            element_password[0].send_keys(str_password)        
        element_login = driver.find_elements_by_xpath(xpath_login_btn)
        if len(element_login) > 0:      
            element_login[0].click()    
    except Exception as e:
        print(e)
        return 0  

    print('successed login')

    if is_time_check:
        #10시부터 동작.
        print('waiting.. AM 10:00')
        now = datetime.datetime.now()     
        while now.strftime('%H:%M') != '10:00':
            now = datetime.datetime.now()     
            sleep(0.1)  
        sleep(0.1)                        

    try:              
        driver.get(url_product_model)    
    except Exception as e:
        print(e)
        return 0

    print('load successed shoes model')
    
    idx_size = 0
    while idx_size < 20:
        idx_size = idx_size + 1
        url_size = xpath_size_header + '/span[{0}]'.format(idx_size)
        element_size_span = driver.find_elements_by_xpath(url_size)
        if len(element_size_span) > 0:          
            if element_size_span[0].text == str_size:
                element_size_span[0].click()      
                print('select shoes size')
                element_buy = driver.find_elements_by_xpath(xpath_buy)
                if len(element_buy) > 0:    
                    element_buy[0].click() 
                    print('check buy button')
                
                print('wait ship info browser')                
                while 1<100:                                           
                    element_license_agree = driver.find_elements_by_xpath(xpath_license_agree)
                    if len(element_license_agree) > 0:
                        element_license_agree[0].submit()
                        break
                    sleep(0.1)         

                print('wait payment info browser')                
                while 1<100:                                                          
                    element_checkbox_product_agree = driver.find_elements_by_xpath(xpath_checkbox_product_agree)
                    if len(element_checkbox_product_agree) > 0:
                        element_checkbox_product_agree[0].click()
                        while 1<100:
                            element_btn_payment = driver.find_elements_by_xpath(xpath_btn_payment)
                            if len(element_btn_payment) > 0:
                                class_name = element_btn_payment[0].get_attribute('class')
                                if len(class_name) > 0:
                                    if class_name == xpath_btn_check:                                        
                                        ischecked = True
                                        element_btn_payment[0].click()
                                        print('tyring buy product')
                                        break                    
                    if ischecked:
                        break                        
                    sleep(0.1)  
            
    while 1<100:
        sleep(1)

if __name__ == "__main__":
    main()