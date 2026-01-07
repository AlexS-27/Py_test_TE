from re import match

import pytest
from articles import ajouter_article

def test_add_normal_article():

    # Arrange
    name = "pomme"
    price = 2.0
    quantity = 2

    # Act
    article = ajouter_article(name, price, quantity)

    # Assert
    assert article is True

def test_quantiy_zero():

    name = "pomme"
    price = 2.0
    quantity = 0

    with pytest.raises(ValueError, match="Quantité inférieur ou égale à zéro"):
        ajouter_article(name, price, quantity)

def test_price_zero():

    name = "pomme"
    price = 0.0
    quantity = 2

    with pytest.raises(ValueError, match="Prix inférieur ou égale à zéro"):
        ajouter_article(name, price, quantity)

def test_add_article():

    name = "pomme"
    price = 2.0
    quantity = 2

    article = ajouter_article(name, price, quantity)

    assert "Quantité ajoutée"