from itertools import product

vowels = "ЕАИ"
non_vowels = "ВЛМПЙ"

fixed_part = "ПИЛАЕВА"

fixed_vowels_count = sum(1 for letter in fixed_part if letter in vowels)
fixed_consonants_count = len(fixed_part) - fixed_vowels_count

additional_vowels_needed = 4 - fixed_vowels_count
additional_non_vowels_needed = 5 - fixed_consonants_count


if additional_vowels_needed < 0 or additional_non_vowels_needed < 0:
    print(0)
else:
    total_count = 0
    for combination in product(vowels + non_vowels, repeat=9):
        if (sum(1 for letter in combination if letter in vowels) == additional_vowels_needed and
            sum(1 for letter in combination if letter in non_vowels) == additional_non_vowels_needed):
            total_count += 1

    print(total_count)
