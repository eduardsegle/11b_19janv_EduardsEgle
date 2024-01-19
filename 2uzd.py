import csv
def kollona(csv_fails):
    with open(csv_fails, 'r', newline='', encoding='utf-8') as f:
        lasītājs = csv.reader(f)
        for rinda in lasītājs:
            if len(rinda) > 1:  
                print(rinda[1])
if __name__ == "__main__":
    csv_fails = 'eglescsv.csv'
    kollona(csv_fails)

