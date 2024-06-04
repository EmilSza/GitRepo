import matplotlib.pyplot as plt

def mergeSort(list_to_sort):
    """
    Sortiert eine Liste in aufsteigender Reihenfolge mithilfe des Merge-Sort-Algorithmus.

    Parameter:
    list_to_sort (list): Die zu sortierende Liste.

    Rückgabe:
    None: Die Funktion modifiziert die Eingangsliste direkt.

    """
    if len(list_to_sort) > 1:
        # Teile die Liste in zwei Hälften
        mid = len(list_to_sort) // 2
        left_half = list_to_sort[:mid]
        right_half = list_to_sort[mid:]

        # Sortiere beide Hälften der Liste (Rekursion)
        mergeSort(left_half)
        mergeSort(right_half)

         # Initialisiere die Indizes für die linke Hälfte, die rechte Hälfte und die sortierte Liste
        left_index = 0
        right_index = 0
        sorted_index = 0

        # Füge die Elemente der linken und rechten Hälften sortiert in die sortierte Liste ein
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                list_to_sort[sorted_index] = left_half[left_index]
                left_index += 1
            else:
                list_to_sort[sorted_index] = right_half[right_index]
                right_index += 1
            sorted_index += 1

        # Füge die restlichen Elemente der linken und rechten Hälften hinzu
        while left_index < len(left_half):
            list_to_sort[sorted_index] = left_half[left_index]
            left_index += 1
            sorted_index += 1

        while right_index < len(right_half):
            list_to_sort[sorted_index] = right_half[right_index]
            right_index += 1
            sorted_index += 1


# Erstelle eine Liste von Zahlen
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# Erstelle eine Liste von Indizes
x = range(len(my_list))

# Erstelle einen neuen Plot mit zwei Subplots
fig, axs = plt.subplots(2)

# Zeichne die ursprüngliche Liste als Balkendiagramm und füge Titel und Achsenbeschriftungen hinzu
axs[0].bar(x, my_list)
axs[0].set_title('Ursprüngliche Liste')
axs[0].set_xlabel('Index')
axs[0].set_ylabel('Wert')
#axs[0].grid(True)

# Sortiere die Liste
mergeSort(my_list)

# Zeichne die sortierte Liste als Balkendiagramm und füge Titel und Achsenbeschriftungen hinzu
axs[1].bar(x, my_list)
axs[1].set_title('Sortierte Liste')
axs[1].set_xlabel('Index')
axs[1].set_ylabel('Wert')
#axs[1].grid(True)

plt.tight_layout()
plt.show()
