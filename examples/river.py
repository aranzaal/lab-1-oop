class River:
    all_rivers = []

    def __init__(self, name: str, length: int) -> None:
        self.name = name
        self.length = length
        River.all_rivers.append(self)

    # Метод
    def get_info(self) -> str:
        return f"Длина {self.name} равна {self.length} км"


def main() -> None:
    volga = River("Волга", 3530)
    seine = River("Сена", 776)
    nile = River("Нил", 6852)

    for river in River.all_rivers:
        print(f"Name: {river.name}, Length: {river.length}")
    print(f"\n {volga.get_info()}\n {seine.get_info()}\n {nile.get_info()}")


if __name__ == "__main__":
    main()