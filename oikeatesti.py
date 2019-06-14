from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
while(True):
    #opening the site / refreshing it
    driver.get("https://www.crownboards.com/collections/royaltribe")


    #Wanted deck
    element = driver.find_elements_by_xpath("//img[@alt='Royal Tribe - Print #86']")

    #Checks the lenght of element list if it found any of the wanted elements
    if (len(element) != 0):

        #clicks the element
        element[0].click()

        #Options menu ID
        el = driver.find_element_by_id('SingleOptionSelector-0')

        #Selects menu from options menu
        for option in el.find_elements_by_tag_name('option'):
            if option.text == "Medium":
                option.click() # select() in earlier versions of webdriver
                break

        #Finds cart button
        element3 = driver.find_elements_by_xpath("//button[@class='btn product-form__cart-submit']")

        #Clicks it
        element3[0].click()

        break;

    #If none found script pauses for 1 second and continues refreshing page
    else:
        time.sleep(1)
