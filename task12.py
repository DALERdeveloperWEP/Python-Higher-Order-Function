students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]

print(
    list(
        sorted(
            students,
            key=lambda p: p['grade']
        )
    )
)