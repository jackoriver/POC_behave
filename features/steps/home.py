from behave import *

from features.pages.home import HomePage

use_step_matcher('re')


@step('Verify the homepage loaded successfully')
def home_page_loaded(context):
    page = HomePage(context)
    assert page.menu_button.is_displayed(), "Menu button is not displayed"
    assert page.cart.is_displayed(), "Cart button is not displayed"
    assert page.inventory_section.is_displayed(), "The inventory section is missing."
