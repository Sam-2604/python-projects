# Reads this CSV data from a file called scores.csv
# Print the name of the highest scorer and 
# the class average formatted to 2 decimal places 
# — use `csv.DictReader`

import csv


with open("scores.csv") as file:
    reader = csv.DictReader(file)
    highest_scorer = None
    highest_score = 0.0
    total = 0.0
    count = 0
    
    for row in reader:
        score = float(row["score"])
        total += score
        count += 1
        if score > highest_score:
            highest_score = score
            highest_scorer = row["name"]
            
    average_score = total / count if count > 0 else 0.0       

    print(f"Highest Scorer: {highest_scorer}")
    print(f"Class Average: {average_score:.2f}")