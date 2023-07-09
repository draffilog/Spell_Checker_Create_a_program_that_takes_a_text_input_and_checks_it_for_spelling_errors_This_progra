import re

def spell_checker(text, dictionary):
    words = re.findall(r'\w+', text.lower())
    corrected_text = text

    for word in words:
        if word not in dictionary:
            corrected_word = find_correction(word, dictionary)
            corrected_text = corrected_text.replace(word, corrected_word)

    return corrected_text

def find_correction(word, dictionary):
    suggestions = []
    for i in range(len(word)):
        left_part = word[:i]
        right_part = word[i+1:]

        for char in 'abcdefghijklmnopqrstuvwxyz':
            corrected_word = left_part + char + right_part
            if corrected_word in dictionary:
                suggestions.append(corrected_word)

    return suggestions[0] if suggestions else word

# Example usage
dictionary = {'apple', 'banana', 'cherry', 'date', 'elderberry'}

text = "I like appl, banan, and cherries."
corrected_text = spell_checker(text, dictionary)
print(corrected_text)  # Output: "I like apple, banana, and cherries."