class TestPracticeForm:
    def test_select_state(self, chrome):
        state = 'Rajesthan'
        page = PagePracticeForm(driver=chrome)
        page.open()
        page.select_state(state_name)
        pass