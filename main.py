def analyze_numbers(numbers):
    result = []
    for number in numbers:  # Vòng lặp
        if number % 2 == 0:  # Lệnh rẽ nhánh
            result.append(f"{number} là số chẵn")
        else:
            result.append(f"{number} là số lẻ")
    return "\n".join(result)

if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5]
    print(analyze_numbers(sample))
