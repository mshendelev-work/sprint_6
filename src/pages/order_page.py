import allure

from src.constants import ConstantsUserData
from src.locators.order_page_locators import OrderPageLocators
from src.pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Наследование драйвера')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнение тестовыми данными №1 первой страницы заказа')
    def filling_first_order_page_first_data(self):
        input_first_name = self.find_element(OrderPageLocators.INPUT_FIRST_NAME)
        input_first_name.send_keys(ConstantsUserData.USER_DATA['first_name'])
        input_last_name = self.find_element(OrderPageLocators.INPUT_LAST_NAME)
        input_last_name.send_keys(ConstantsUserData.USER_DATA['last_name'])
        input_address = self.find_element(OrderPageLocators.INPUT_ADDRESS)
        input_address.send_keys(ConstantsUserData.ADDRESS_ONE)
        list_stations = self.find_element(OrderPageLocators.INPUT_SUBWAY)
        list_stations.click()
        choose_subway = self.find_element(OrderPageLocators.CHOOSE_SUBWAY_STATION_CULTURE_PARK)
        self.scroll_to_element(choose_subway)
        self.find_element_to_be_clickable(choose_subway)
        choose_subway.click()
        input_phone = self.find_element(OrderPageLocators.INPUT_PHONE_NUMBER)
        input_phone.send_keys(ConstantsUserData.PHONE_NUMBER_ONE)
        button_further = self.find_element(OrderPageLocators.BUTTON_FURTHER)
        button_further.click()

    @allure.step('Заполнение тестовыми данными №1 второй страницы заказа')
    def filling_second_order_page_first_data(self):
        input_date_order = self.find_element(OrderPageLocators.INPUT_DATE_ORDER)
        self.find_element_to_be_clickable(input_date_order)
        input_date_order.send_keys(ConstantsUserData.DATE_ONE)
        text_modal_window = self.find_element(OrderPageLocators.TEXT_MODAL_WINDOW)
        text_modal_window.click()
        choose_rental = self.find_element(OrderPageLocators.CHOOSE_RENTAL_PERIOD)
        choose_rental.click()
        choose_rental_two_days = self.find_element(OrderPageLocators.CHOOSE_RENTAL_PERIOD_TWO_DAYS)
        choose_rental_two_days.click()
        choose_black_color = self.find_element(OrderPageLocators.CHOOSE_BLACK_COLOR_SCOOTER)
        choose_black_color.click()
        input_for_comment = self.find_element(OrderPageLocators.INPUT_COMMENT_FOR_COURIER)
        input_for_comment.send_keys(ConstantsUserData.COMMENT_FOR_COURIER_ONE)
        button_order_page = self.find_element(OrderPageLocators.BUTTON_ORDER)
        button_order_page.click()

    @allure.step('Заполнение тестовыми данными №2 первой страницы заказа')
    def filling_first_order_page_second_data(self):
        input_first_name = self.find_element(OrderPageLocators.INPUT_FIRST_NAME)
        input_first_name.send_keys(ConstantsUserData.USER_DATA['first_name'])
        input_last_name = self.find_element(OrderPageLocators.INPUT_LAST_NAME)
        input_last_name.send_keys(ConstantsUserData.USER_DATA['last_name'])
        input_address = self.find_element(OrderPageLocators.INPUT_ADDRESS)
        input_address.send_keys(ConstantsUserData.ADDRESS_SECOND)
        list_stations = self.find_element(OrderPageLocators.INPUT_SUBWAY)
        list_stations.click()
        choose_subway = self.find_element(OrderPageLocators.CHOOSE_SUBWAY_STATION_TULSKAYA)
        self.scroll_to_element(choose_subway)
        self.find_element_to_be_clickable(choose_subway)
        choose_subway.click()
        input_phone = self.find_element(OrderPageLocators.INPUT_PHONE_NUMBER)
        input_phone.send_keys(ConstantsUserData.PHONE_NUMBER_SECOND)
        button_further = self.find_element(OrderPageLocators.BUTTON_FURTHER)
        button_further.click()

    @allure.step('Заполнение тестовыми данными №2 второй страницы заказа')
    def filling_second_order_page_second_data(self):
        input_date_order = self.find_element(OrderPageLocators.INPUT_DATE_ORDER)
        self.find_element_to_be_clickable(input_date_order)
        input_date_order.send_keys(ConstantsUserData.DATE_SECOND)
        text_modal_window = self.find_element(OrderPageLocators.TEXT_MODAL_WINDOW)
        text_modal_window.click()
        choose_rental = self.find_element(OrderPageLocators.CHOOSE_RENTAL_PERIOD)
        choose_rental.click()
        choose_rental_two_days = self.find_element(OrderPageLocators.CHOOSE_RENTAL_PERIOD_FOUR_DAYS)
        choose_rental_two_days.click()
        choose_black_color = self.find_element(OrderPageLocators.CHOOSE_GREY_COLOR_SCOOTER)
        choose_black_color.click()
        input_for_comment = self.find_element(OrderPageLocators.INPUT_COMMENT_FOR_COURIER)
        input_for_comment.send_keys(ConstantsUserData.COMMENT_FOR_COURIER_SECOND)
        button_order_page = self.find_element(OrderPageLocators.BUTTON_ORDER)
        button_order_page.click()

    @allure.step('Принятие заказа и возврат кнопки «Отменить заказ»')
    def filling_second_order_page(self):
        button_yes = self.find_element(OrderPageLocators.BUTTON_YES)
        button_yes.click()
        button_view_status = self.find_element(OrderPageLocators.BUTTON_VIEW_STATUS_ORDER)
        button_view_status.click()
        button_cancel_order = self.find_element(OrderPageLocators.BUTTON_CANCEL_ORDER)
        return button_cancel_order
