from name_generator import CultureNameGenerator
from name_generator.cultures import HUMAN


def main():
    g = CultureNameGenerator(HUMAN)
    for _ in range(30):
        print(g.get_name(unique=True))


if __name__ == "__main__":
    main()
