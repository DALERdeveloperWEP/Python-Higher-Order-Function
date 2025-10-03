sentence = "Functional programming in Python is very powerful and elegant"
sort = sorted(
    sentence.split(),
    key=lambda word: len(word),
    reverse=True
)

print(sort[:3])
