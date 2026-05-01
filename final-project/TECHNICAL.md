# Technical Documentation

## Project Structure
project.py: The core executable script. Contains the main entry point, API interaction logic, and the Medicine class definition.

test_project.py: Contains the pytest suite. Utilizes mocking (via unittest.mock) to simulate API responses and user input without requiring a live connection or manual typing.

requirements.txt: Specifies the external dependencies (the requests library) needed to run the software.

README.md: The user-facing documentation covering installation, usage, and project rationale.

## Architecture Overview
The program follows a modular, linear flow managed by the main() function:

main(): Initializes preferences, resets output files, and orchestrates the loop.

get_drug_names(): Collects a list of strings from the user, handling "quit" and validation.

fetch_drug_info(): Performs a GET request to the openFDA API for each name.

validate_result(): Inspects the API's "results" array to find a record where the brand name matches the user's query.

Medicine() (Class): Instantiates an object that encapsulates the raw JSON, cleanses the text, and organizes it into med_info and caution_info dictionaries.

save_reports(): Appends the object's data to the selected CSV files based on user-defined flags.

## Key Functions
### get_drug_names()

Purpose: Interactive loop to gather medication names.

Input: None (User prompt).

Output: A list of strings.

Edge cases handled: Checks for non-alphanumeric input; uses continue to reprompt rather than crashing; correctly identifies 'q' to break the loop.

### fetch_drug_info(name)

Purpose: Retrieves drug label data from the FDA.

Input: name (string).

Output: A dict containing the JSON response.

Edge cases handled: Raises ValueError on 404 (Not Found) and ConnectionError on network failure.

### validate_result(json_response, requested_name)

Purpose: Ensures the API didn't return a generic or irrelevant result.

Input: Raw JSON dict and the user's string query.

Output: A single dict (the most relevant record).

Edge cases handled: Iterates through multiple results if the first one is a mismatch; raises ValueError if no specific brand match is found.

### Medicine.__init__(self, name, api_result)

Purpose: Transforms raw data into a clean, structured object.

Input: The medicine name and the validated API dictionary.

Output: An initialized Medicine instance.

Edge cases handled: Uses .get() with defaults ("N/A") to prevent KeyError if certain fields (like warnings) are missing in the FDA database.

## Data Flow
Input Phase: User inputs are stored in a list. Boolean flags are set for output preferences.

Retrieval Phase: For each name, a request is sent. The raw JSON is filtered for relevance.

Transformation Phase: The Medicine class "flattens" lists into strings and strips out API-specific prefixes (e.g., removing "Purpose: " from the start of a purpose string).

Persistence Phase:

Data Report: Data is written in a long, narrow format (one row per attribute).

User Report: Data is written in a vertical "block" format with visual separators (===).

## Known Limitations & Future Improvements
### Limitations

API Dependency: The program requires an active internet connection to fetch new data.

US-Centric: The data source is strictly the U.S. FDA; medications exclusively sold in other markets (like India) will not be found.

Fuzzy Matching: While validation exists, very common words might occasionally return a generic equivalent instead of the exact brand intended.

### Future Improvements

Local Caching: Implement a local SQLite database to store previously searched medicines to reduce API calls.

Interaction Checker: Add a feature to compare the "Active Ingredients" of multiple entered drugs to warn the user about potential duplications.

GUI Version: Transition the CLI into a simple desktop application using Tkinter or PyQt for non-technical users.