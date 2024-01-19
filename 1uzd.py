def fails(nosaukums):
    try:
        with open(nosaukums, 'r', encoding='utf8') as fails:
            saturs = fails.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Ir notikusi kļūda, fails '{nosaukums}' nav atrasts.")
    
faila_nosaukums = 'eglesfails.txt'
fails(faila_nosaukums)