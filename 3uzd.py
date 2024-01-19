def rinda(nosaukums):
    try:
        with open(nosaukums, 'r', encoding='utf8') as fails:
            rindas = fails.readlines()
            if len(rindas) >= 3:
                tresa_rinda = rindas[2]
                print("Trešā rinda no faila:", tresa_rinda)
    except FileNotFoundError:
        print("Norādītais fails nav atrasts.")
rinda('eglesfails.txt')