import pytest
from class_exercises.object_orientation.ShoppingBasket import  Item, ShoppingBasket

@pytest.fixture
def setup_items_and_basket():
    # Create items
    tomatoSoup = Item("Tomato Soup", "200mL can", 0.70, 20)
    spaghetti = Item("Spaghetti", "500g pack", 1.10, 20)
    blackOlives = Item("Black Olives Jar", "200g Jar", 2.10, 20)
    mozarella = Item("Mozarella", "100g", 1.50, 20)
    gratedCheese = Item("Grated Cheese", "100g", 2.20, 29)


    basket = ShoppingBasket()
    basket.addItem(tomatoSoup, 4)
    basket.addItem(blackOlives, 1)
    basket.addItem(mozarella, 2)
    basket.addItem(tomatoSoup, 6)

    return basket, tomatoSoup, spaghetti, blackOlives, mozarella, gratedCheese

def test_shopping_basket_setup(setup_items_and_basket):

    basket, tomatoSoup, *other = setup_items_and_basket
    assert basket.items[tomatoSoup] == 10
    assert tomatoSoup.stock == 10

def test_add_more_than_stock(setup_items_and_basket):

    basket, tomatoSoup, *other = setup_items_and_basket
    basket.addItem(tomatoSoup, 12)
    assert basket.items[tomatoSoup] == 20
    assert tomatoSoup.stock == 0