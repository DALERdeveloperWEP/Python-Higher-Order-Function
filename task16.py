data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

print(
    list(
        filter(
            lambda word: isinstance(word, str) and len(word) > 5,
            data
        )
    )
)