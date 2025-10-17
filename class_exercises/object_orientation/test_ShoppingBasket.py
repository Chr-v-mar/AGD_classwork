import pytest
from class_exercises.object_orientation.ShoppingBasket import  Item, ShoppingBasket
from class_exercises.object_orientation.main import blackOlives


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
    basket.addItem(gratedCheese, 25)

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

def test_update(setup_items_and_basket):
    basket, mozarella, *other = setup_items_and_basket
    basket.updateItem(mozarella,3)
    assert basket.items[mozarella] == 3
    assert mozarella.stock == 17

def test_update_False(setup_items_and_basket):
    basket, mozarella, *other = setup_items_and_basket
    with pytest.raises(ValueError):
        basket.updateItem(mozarella,-1)
    with pytest.raises(TypeError):
        basket.updateItem(mozarella,0.5)

def test_remove(setup_items_and_basket):
    basket, gratedCheese, *other = setup_items_and_basket
    basket.removeItem(gratedCheese)
    assert basket.items[gratedCheese] == 0
    assert gratedCheese.stock == 29

def test_remove_more_than_quantity(setup_items_and_basket):
    basket, blackOlives, *other = setup_items_and_basket
    with pytest.raises(TypeError):
        basket.removeItem(blackOlives,0.5)