# Sorteer Algoritmes in Python

Voor je is een overzicht aan sorteer algoritmes in Python.
Dit document biedt uitleg over de manier waarop de verschillende algoritmes werken.
Daarnaast is de code van ieder algoritme voorzien van vele comments die uitleggen wat er gebeurt.

## Insertion Sort

De insertion sort is geschikt om kleine reeksen te sorteren.
Laten we als voorbeeld gebruik maken van de reeks: [4, 7, 5, 2, 3, 1, 6].
De eerste van het algoritme kijk naar de 7, deze wordt vergeleken met de 4.
We zien dat de 7 groter is dan de vier, dus we laten deze op z'n plek staan.
Vervolgens kijken we naar de 5. Deze is kleiner dan 7; dus verwisselen we de getallen.
Daar vergelijken we de 5 met de 4, de 5 is groter en blijft dus op z'n plek staan.
Op deze manier gaan we de hele reeks af tot deze gesorteerd is.

De eerste stap is het maken van een functie die over itereert over alle getallen in de reek, 
beginned bij het tweede item (index 1 in Python).

```python
def insertion_sort(array):
    for index in range(1, len(array)):
```

Vervolgens slaan we de sleutel (het getal dat wordt gesorteerd) op in een variabele.
Daarnaast maken we een variabele om bij te houden met welk getal we aan het vergelijken zijn.
In de eerste iteratie wordt de sleutel 7 en de index van het getal waarmee vergeleken wordt 0.
Dit omdat we het tweede getal in de array (index 1), willen vergelijken met het eerste getal uit de array (index 0).

```python
def insertion_sort(array):
    for index in range(1, len(array)):
        key = array[index]
        search_index = 0
```

We willen controleren of de twee getallen met elkaar verwisselt moeten worden.
Hiervoor kunnen we een voorwaarde toevoegen aan de code die hierop controleert.
Op het moment dat de sleutel kleiner is dan het getal waarmee we vergelijken, 
wordt het getal waarmee vergeleken wordt opgeschoven.

```python
def insertion_sort(array):
    for index in range(1, len(array)):
        key = array[index]
        search_index = 0

        if key < array[search_index]:
            array[search_index + 1] = array[search_index]
            search_index = search_index - 1
```

De enige stap die nu nog voor de eerste iteratie mist is het terugplaatsen van de sleutel.

```python
def insertion_sort(array):
    for index in range(1, len(array)):
        key = array[index]
        search_index = 0

        if key < array[search_index]:
            array[search_index + 1] = array[search_index]
            search_index = search_index - 1

        array[search_index + 1] = key
```

De eerste iteratie werkt nu, echter; de tweede iteratie nog niet.
Op dit moment wordt ieder getal vergeleken met het getal dat ervoor staat.
Echter is het de bedoeling dat het wordt vergeleken met alle getallen die ervoor staan.
Dit kunnen we oplossen door de voorwaarde in een herhaling te zetten

```python
def insertion_sort(array):
    for index in range(1, len(array)):
        key = array[index]
        search_index = 0

        while search_index >= 0:
            if key < array[search_index]:
                array[search_index + 1] = array[search_index]
                search_index = search_index - 1

        array[search_index + 1] = key
```

Om een aantal iteraties te besparen kunnen we de voorwaarde en de herhaling combineren.

```python
def insertion_sort(array):
    for index in range(1, len(array)):
        key = array[index]
        search_index = 0

        while search_index >= 0 and key < array[search_index]:
                array[search_index + 1] = array[search_index]
                search_index = search_index - 1

        array[search_index + 1] = key
```