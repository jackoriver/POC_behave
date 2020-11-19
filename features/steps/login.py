from behave import *

from features.pages.login import LoginPage
from features.utils.botstyle import type_textfield

use_step_matcher('re')


@step('I type my username')
def type_username(context):
    page = LoginPage(context)
    type_textfield(page.username, context.config.userdata.get('standard_username'))


@step('I type my password')
def type_password(context):
    page = LoginPage(context)
    type_textfield(page.password, context.config.userdata.get('common_password'))


@step('I click on login')
def click_login_button(context):
    page = LoginPage(context)
    assert page.login_button.is_displayed(), "Login button is not displayed"
    page.login_button.click()
