def ierakstisanafaila(nosaukums, saturs):
    try:
        with open(nosaukums, 'w', encoding='utf8') as fails:
            fails.write(saturs)
        print(f"Ierakstīts veiksmīgi failā '{nosaukums}'.")
    except FileNotFoundError:
        print(f"Kļūda notika, fails '{nosaukums}' nav atrasts.")
    except PermissionError:
        print(f"Kļūda ir notikusi, nav atļaujas rakstīt failā '{nosaukums}'.")
    except Exception as e:
        print(f"Kļūda notika un neizdevās ierakstīt failā. Detaļas: {str(e)}")

def main():
    vards = input("Ieraksti savu vārdu: ")
    faila_nosaukums = "vardusaraksts.txt"
    ierakstisanafaila(faila_nosaukums, vards)
if __name__ == "__main__":
    main()