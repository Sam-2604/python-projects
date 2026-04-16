# Ask the user repeatedly for a score between 0 and 100 until they type "done" 
# — reject non-numeric input and out-of-range values with specific messages. 
# At the end print the average, highest, and lowest score formatted to 2 decimal places.

def main():
    scores = []
    
    while True:
        user_input = input("Enter a score between 0 and 100 (or 'done' to finish): ")
        
        if user_input.lower() == "done":
            break
        
        try:
            score = float(user_input)
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Invalid input. Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    if scores:
        average_score = sum(scores) / len(scores)
        highest_score = max(scores)
        lowest_score = min(scores)
        
        print(f"Average score: {average_score:.2f}")
        print(f"Highest score: {highest_score:.2f}")
        print(f"Lowest score: {lowest_score:.2f}")
    
main()