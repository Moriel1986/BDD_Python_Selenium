from base.base_class import Base_class


class Fb_login_page(Base_class):
    user_name = "demoriel24@comcast.net"
    password = "Kobelastgame60$"
    login_btn_id = "u_0_b"

    def __init__(self, driver):
        super().__init__(driver)

    def login_fb(self):
        self.send_keys_to("email", "demoriel24@comcast.net", "id")
        self.send_keys_to("pass", "Kobelastgame60$", "id")

    def login_btn(self):
        self.click_on_element("u_0_b", "id")

    def click_profile_btn(self):
        self.click_on_element("//span[@class='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7'][contains(text(),"
                              "'Demoriel Purnell')]", "xpath")

    def verify_image(self):
        self.is_element_visible("//div[@class='_42b6 _1zet _403j']"
                                "//i[@class='img _1-yc profpic']", "xpath")

    def alert_handle(self):
        self.driver.switch_to_alert().dismiss()

    def drop_down(self):
        self.drop_down_handle("", "", "", "")

    def search_data(self, data_locator, data, data_locator_type):
        self.enter_search_data(data_locator, data, data_locator_type)


