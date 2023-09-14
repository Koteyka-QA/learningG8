class PagePracticeForm:
    __URL = https://demoqa.com/automation-practice-form
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__state_city_wrapper_loc = '//div[@id="stateCity-wrapper"]'
        self.__state_dropdown_menu_loc = '//div{@id'
        #Загублений код, потім треба дописати із запису

    def open(self):
        self.__driver.get(self.__URL)
    def get_xpath_for_state_dropdown(self) -> str:
        wrapper = self.__state_city_wrapper_loc
        menu = self.__state_dropdown_menu_loc
        xpath = f'{wrapper}{menu}
        return xpath
    def select_state(self, name):
        self.__expand_states()
        self.__state_dropdown_menu_loc
