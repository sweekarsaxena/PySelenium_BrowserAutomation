from config import Credentials, browser


# browser = webdriver.Chrome()
browser.get("https://github.com/")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

cred = Credentials()

cred.username()
# username_box = browser.find_element_by_id("login_field")
# username_box.send_keys("abc@gmail.com")

cred.password_submit()
# password_box = browser.find_element_by_id("password")
# password_box.send_keys("your_password")

# password_box.submit()

assert "username" in browser.page_source

profile_link = browser.find_element_by_class_name("user-profile-link")
page_source = profile_link.get_attribute("innerHTML")
assert "username" in page_source

browser.quit()
