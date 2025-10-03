votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]
print(
    max(
        votes,
        key=lambda us: us['votes']
    )
)
