# string_manipulation.py

sentence = input("Enter a sentence: ")

# Convert to uppercase
upper_sentence = sentence.upper()
print("\nUppercase:", upper_sentence)

# Reverse sentence
reversed_sentence = sentence[::-1]
print("Reversed:", reversed_sentence)

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)

# Replace spaces with hyphens
hyphen_sentence = sentence.replace(" ", "-")
print("Hyphenated:", hyphen_sentence)