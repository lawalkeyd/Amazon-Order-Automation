from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urlparse, parse_qs

def order_now(item_url, buyer_name, address1, address2, city, state, zip_code):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    action = ActionChains(browser)

    browser.get(item_url)
    time.sleep(3)

    login_menu = browser.find_element_by_xpath('//*[@id="nav-link-accountList"]')
    action.move_to_element(login_menu).perform()
    time.sleep(1)
    print('login menu')


    login_button = browser.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a')
    login_button.click()
    time.sleep(8)

    signinelement = browser.find_element_by_xpath('//*[@id="ap_email"]')
    signinelement.send_keys('')

    cont = browser.find_element_by_xpath('//*[@id="continue"]')
    cont.click()
    time.sleep(3)

    passwordelement = browser.find_element_by_xpath('//*[@id="ap_password"]')
    passwordelement.send_keys('')
    time.sleep(3)

    login = browser.find_element_by_xpath('//*[@id="signInSubmit"]')
    login.click()
    time.sleep(10)
    print('logged in')

    try:
        browser.find_element_by_partial_link_text("Used from").click()
    except NoSuchElementException:
        browser.find_element_by_partial_link_text("New from").click()

    print('item selescted')

    time.sleep(15)

    item_menu = browser.find_element_by_xpath('//*[@id="a-autoid-2-offer-1"]/span/input')
    item_menu.click()
    time.sleep(3)


    cancel_modal = browser.find_element_by_xpath('//*[@id="aod-close"]/span/span/i')
    cancel_modal.click()

    browser.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')

    proceed_menu = browser.find_element_by_xpath('//*[@id="sc-buy-box-ptc-button"]/span')
    proceed_menu.click()
    print('changing address')
    
    change_address = browser.find_element_by_xpath('//*[@id="addressChangeLinkId"]')
    change_address.click()
    time.sleep(5)

    address = browser.find_element_by_xpath('//*[@id="add-new-address-popover-link"]')
    address.click()
    time.sleep(3)


    fullname = browser.find_element_by_xpath('//*[@id="address-ui-widgets-enterAddressFullName"]')
    fullname.clear()
    fullname.send_keys(buyer_name)
    time.sleep(1)

    addresse1 = browser.find_element_by_xpath('//*[@id="address-ui-widgets-enterAddressLine1"]')
    addresse1.clear()
    addresse1.send_keys(address1)
    time.sleep(1)

    addresse2 = browser.find_element_by_xpath('//*[@id="address-ui-widgets-enterAddressLine2"]')
    addresse2.clear()
    addresse2.send_keys(address2)
    time.sleep(1)

    new_city = browser.find_element_by_xpath('//*[@id="address-ui-widgets-enterAddressCity"]')
    new_city.send_keys(city)
    stated = "//select[@name='address-ui-widgets-enterAddressStateOrRegion']/option[text()='{}']".format(state)
    new_state = browser.find_element_by_xpath(stated).click()

    zipcode = browser.find_element_by_xpath('//*[@id="address-ui-widgets-enterAddressPostalCode"]')
    zipcode.send_keys(zip_code)

    save_address = browser.find_element_by_xpath('//*[@id="address-ui-widgets-form-submit-button"]/span/input')
    save_address.click()

    save_address = browser.find_element_by_xpath('//*[@id="address-ui-widgets-form-submit-button"]/span/input')
    save_address.click()
    time.sleep(5)

    place_order = browser.find_element_by_xpath('//*[@id="submitOrderButtonId"]/span/input')
    place_order.click()

    time.sleep(3)
    url_redirect = browser.current_url
    purchase_id = parse_qs(urlparse(url_redirect).query)['purchaseId'][0]
    print(purchase_id)
    return purchase_id
