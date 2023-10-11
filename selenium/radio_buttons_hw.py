from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RadioButtonPage:
    __URL = 'https://demoqa.com/radio-button'

    def __init__(self, driver):
        self.__driver = driver
        self.__radio_buttons = (By.XPATCH, "//input[@type='radio']")
        self.__text_info = (By.XPATCH, "//p[@class='mt-3']")
        self.__no_radio_button = (By.XPATCH, "//label[text()='No']//preceding-sibling::input")

    def open_page(self):
        self.__driver.get(self.__URL)

    def click_on_selected_radio_button(self):
        radio_buttons = self.__driver.find_elements(*self.__radio_buttons)
        selected_radio_buttons = next((radio for radio in radio_buttons if radio.is_selected()), None)
        selected_radio_buttons.click()

    def assert_text_info(self):
        text_element = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located(self.__text_info)
        )
        assert "You have selected" in text_element.text

    def click_no_radio_button_with_js(self):
        no_radio_button = self.__driver.find_element(*self.__no_radio_button)
        self.__driver.execute_script("arguments[0];", no_radio_button)

    def is_no_radio_button_selected(self):
        radio_button_info = {}
        for radio_button in radio_button:
            label_text = radio_button.find_element(By.XPATCH, "..").text
            is_enabled = radio_button.is_enabled()
            is_selected = radio_button.is_selected()
            radio_button_info[label_text] = {'enabled': is_enabled, 'selected': is_selected}
        return self.__driver.find_element(By.XPATCH, locator).is_selected()



