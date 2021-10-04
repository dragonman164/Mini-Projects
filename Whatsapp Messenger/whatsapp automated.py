from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")

name = input("Enter Name of Group/Contact : ")
message_to_spam = input("Enter Message to Send : ")
num_of_messages = int(input("Enter Number of Messages to Send : "))

driver.implicitly_wait(1.0)

driver.find_element_by_xpath(f"//span[@title='{name}']").click()

for _ in range(num_of_messages):
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(message_to_spam)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()

    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(message_to_spam)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()
