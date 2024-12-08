def calculate_above_average_percentage(grades):
    average = sum(grades) / len(grades)
    above_average_count = sum(1 for grade in grades if grade > average)
    return round(above_average_count / len(grades) * 100, 3)

if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        n = list(map(int, input().split()))
        num_students = n[0]
        grades = n[1:]
        percentage = calculate_above_average_percentage(grades)
        print(f"{percentage:.3f}%")
