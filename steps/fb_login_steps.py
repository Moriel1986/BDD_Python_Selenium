from behave import given, when, then
from selenium import webdriver
from base.base_class import Base_class
from pages.fb_login_page import Fb_login_page


@given('user has launched browser')
def launch_browser(context):
    context.Facebook_Validation = Fb_login_page(driver=webdriver)
    context.Facebook_Validation.set_up()


@when('user enters username and password')
def login(context):
    context.Facebook_Validation.login_fb()


@when('user clicks login button')
def click_login(context):
    context.Facebook_Validation.login_btn()


@when('user clicks profile picture')
def click_profile_btn(context):
    context.Facebook_Validation.click_profile_btn()

@then('user should see profile image on screen')
def click_profile_btn(context):
    context.Facebook_Validation.verify_image()

@then('user cancels pop up window')
def cancel_popup(context):
    context.Facebook_Validation.alert_handle()

@then('user should land of profile page')
def validate_title(context):
    context.Facebook_Validation.tear_down()

@then('user verifies title')
def title_verification(context):
    context.Facebook_Validation.verify_title

@when('user clicks dropdown and selects option')
def select_drop_down_option(context):
    context.Facebook_Validation.drop_down()

@when('user enters data in search field')
def enter_data(context):
    context.Facebook_Validation.search_data("//input[@type='search']", "Darren Purnell", "xpath")