from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:/Users/dheem/Downloads/geckodriver.exe')
driver.get('http://web.whatsapp.com/')

name = input('Enter the name of the user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count'))

input('Enter anything after scanning QR code')

user = driver.find_elements_by_xpath('//span[@titile="{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('input_container')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
