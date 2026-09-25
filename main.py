from name_generator import NameGenerator
from name_generator.cultures import ELF

def main():
    g = NameGenerator(ELF)
    for _ in range(10):
        print(g.get_persone_name())


if __name__ == "__main__":
    main()
