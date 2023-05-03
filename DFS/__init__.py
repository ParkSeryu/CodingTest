def solution(numbers, direction):
    if direction == "left":
        temp = numbers[0]
        for i in range(len(numbers) - 1):
            numbers[i] = numbers[i + 1]
        numbers[len(numbers) - 1] = temp
    else:
        temp = numbers[len(numbers) - 1]
        for i in range(len(numbers) - 1, 0, -1):
            numbers[i] = numbers[i - 1]
        numbers[0] = temp

        print(numbers)


answer = [1, 2, 3]
solution(answer, "right")
