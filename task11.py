nums = list(range(1, 21))
juft_num = list(
    filter(
        lambda num: num % 2 == 0,
        nums
    )
)

print(
    list(
        map(
            lambda num: num ** 2,
            juft_num
        )
    )
)