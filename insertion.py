'''
Insertion sort is een algoritme dat een array sorteert zoals wij een hand kaarten zouden sorteren.
Op de tafel liggen de kaarten die gesorteerd moeten worden. 
De rechterhand pakt steeds een kaart van de tafel en de linkerhand bevat de gesorteerde stapel kaarten.
Iedere keer pakken we een kaart van de tafel en leggen deze op de juiste plek in de gesorteerde stapel.
'''


# Insertion sort
def insertion_sort(array):
    # Loop over alle elementen in de array, beginnen bij het tweede element
    for index in range(1, len(array)):
        # De key is het getal dat moet worden gesorteerd, sla dit op
        key = array[index]

        # De search_index is de index van het getal waarmee de key vergeleken wordt
        search_index = index - 1

        # Herhaal de volgende opdrachten zolang er getallen voor de key zijn en de key kleiner is dan het getal waar we mee vergelijken
        while search_index >= 0 and key < array[search_index]:
            # Het getal waar we mee vergelijken moet een plek naar rechts om plaats te maken voor de key
            array[search_index + 1] = array[search_index]

            # We gaan door met vergelijken van het volgende getal
            search_index -= 1

        # Leg de key op de juiste plek in de gesorteerde stapel
        array[search_index + 1] = key


# Create a random arrays with numbers and sort it
numbers = [5, 2, 4, 6, 1, 3]
insertion_sort(numbers)
print(numbers)
