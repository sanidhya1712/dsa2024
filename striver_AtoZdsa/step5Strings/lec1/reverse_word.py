def reverse_words(s):
    words = s.split()
    reverse = words[::-1]
    result = ' '.join(reverse)
    return result
print(reverse_words("Hello World"))