from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep
from pages.main_page import MainPage
from app.application import Application
from pages.search_page import SearchPage


@given('Open Amazon main page')
def amazon_page(context):
    context.app.main_page.open_main_page()


@when('Search for {text}')
def search_mens_shoes(context, text):
    context.app.search_page.search_for_nike_shoes()


@then('Click on 5th item')
def click_fifth_product(context):
    context.app.search_page.click_sneakers()


@then('Open size options')
def select_size(context):
    context.app.search_page.click_size()


@then('Select size 10.5')
def correct_size(context):
    context.app.search_page.click_correct_size()


@then('Add to cart')
def add_to_cart(context):
    context.app.search_page.add_to_cart_item()


@then('Verify cart has the item')
def cart(context):
    context.app.cart_page.cart_verify()


