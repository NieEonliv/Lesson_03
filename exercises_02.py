from operator import index

evolutions = [
    "Дриопитек",
    "Австралопитек",
    "Человек умелый",
    "Человек прямоходящий",
    "Неандертальц",
    "Человек разумный"
]

correctAnswerCount = 0

for index, evolution in enumerate(evolutions):
    answer = input(f"Название {index + 1} эволюции человека: ")
    if answer != evolution:
        correctAnswerCount += 1

print(f"Вы ответили правильно на {correctAnswerCount}/{len(evolutions)}")
print(" => ".join(evolutions))