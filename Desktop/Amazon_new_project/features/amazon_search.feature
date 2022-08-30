# Created by ellaoroz at 8/28/22
Feature: # Items inside the cart tests

  Scenario: # User can add and see number of items in the cart
    Given Open Amazon main page
    When Search for 'Nike Men's Shoes'
    Then Click on 5th item
    And Open size options
    And Select size 10.5
    And Add to cart
    And Verify cart has the item
