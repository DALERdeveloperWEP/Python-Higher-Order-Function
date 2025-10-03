text = ["apple", "34", "banana", "100", "abc", "75"]
print(
    list(
        filter(
            lambda elem: elem.isdigit(),
            text
        )
    )
)