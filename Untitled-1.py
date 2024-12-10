def calculate_compability(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    combined_name = name1 + name2

    letter_count = {}
    for letter in combined_name:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    compatibility_score = sum(letter_count.values()) %100

    return compatibility_score

def main():
    print("Совместимость на свадьбу")
name1 = input("Первое имя")
name2 = input("Второе имя")

score = calculate_compability(name1, name2)

print(f"Совместимость имён '{name1} и '{name2}': {score}%")

if __name__ == "__main__":
    main()