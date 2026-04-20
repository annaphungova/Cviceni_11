import random
import matplotlib.pyplot as plt


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


values = random_numbers(10)


def selection_sort(number_list):
    numbers = values.copy()

    for pozice_ukladani in range(len(numbers)):
        min_idx = pozice_ukladani
        for pozice_prochazena in range(pozice_ukladani+1, len(numbers)):
            if numbers[pozice_prochazena] < numbers[min_idx]:
                min_idx = pozice_prochazena

        numbers[pozice_ukladani], numbers[min_idx] = numbers[min_idx], numbers[pozice_ukladani]

    return numbers

def bubble_sort(numbers):

    numbers = values.copy()

    for serazeno_od_konce in range(len(numbers)):
        has_changed = False
        for pozice_porovnani in range(len(numbers) - 1 - serazeno_od_konce):
            if numbers[pozice_porovnani] > numbers[pozice_porovnani + 1]:
                has_changed = True
                numbers[pozice_porovnani], numbers[pozice_porovnani+1] = numbers[pozice_porovnani + 1]
            if not has_changed:
                break

    return numbers




















