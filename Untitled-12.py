def calculate_compability(name1, name2):
    return 50
def main():
    print("Совместимость на свадьбу")
name1 = input("Первое имя")
name2 = input("Второе имя")

score = calculate_compability(name1, name2)

print(f"Совместимость на свадьбу '{name1} и '{name2}': {score}%")

if __name__ == "__main__":
    main()
