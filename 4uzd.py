def fails2(nosaukums):
    try:
        with open(nosaukums, 'r', encoding='utf8') as fails:
            saturs = fails.read()
        return saturs
    except FileNotFoundError:
        print(f"Kļūda ir notikusi, fails '{nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda notika un neizdevās nolasīt failu. Detaļas: {str(e)}")
    return None

def main():
    nosaukums = input("Ievadiet faila nosaukumu: ")
    paplasinajums = input("Ievadiet faila formātu (paplašinājumu): ")
    pilns_nosaukums = f"{nosaukums}.{paplasinajums}"
    faila_saturs = fails2(pilns_nosaukums)
    if faila_saturs is not None:
        print(f"Faila '{pilns_nosaukums}' saturs:\n{faila_saturs}")
    

if __name__ == "__main__":
    main()