# THE MEDICATION GUIDE
  A batch-processing CLI tool that extracts safety-critical information for multiple medications using the openFDA API.
  
  #### Video Demo:  <URL HERE>

  ## Description
  The Medication Guide solves a common accessibility issue found on official medical databases. While the U.S. Food and Drug Administration (FDA) maintains extensive records, the official website (https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm) lacks a streamlined way for consumers to quickly cross-reference multiple medications. Platforms like DailyMed offer comprehensive data but require users to search for each medication individually, which can be time-consuming and overwhelming.

  This project provides a "distilled" view of medication data. It performs batch processing of user-provided medicine names and extracts only the most relevant sections: Purpose, Usage, and Warnings. By filtering out the dense clinical documentation intended for healthcare providers, this tool creates a more digestible experience for the everyday consumer.

  Technically, the software interfaces with the openFDA API, utilizing complex dictionary parsing and list flattening to transform raw JSON data into structured reports. It employs Object-Oriented Programming (OOP) to manage medicine data and provides flexible output options, allowing users to choose between machine-readable CSVs or human-friendly vertical reports.

  ## Features
  - Batch Processing: Enter multiple medication names in a single session to generate a consolidated report.

  - Relevance Validation: Includes a "fuzzy match" check to ensure fetched API data actually belongs to the brand name requested.

  - Dual-Format Output: - data_report.csv: A narrow, standardized format optimized for data analysis and CSV readers.

  - user_report.csv: A vertically structured, titled document designed for human readability in spreadsheet software.

  - User Preference Control: Interactive configuration allows users to toggle specific reports and toggle between "Primary Info" and "Caution Info."

  - Data Sanitization: Automatically cleans API data inconsistencies, removing redundant prefixes and flattening complex nested lists into readable strings.

  ## Requirements
  - Python 3.x
  - Libraries: requests (`pip install requests`), csv and sys (no installation needed)

  ## Installation
  Execute in the terminal: "pip install -r requirements.txt"

  ## Usage
  1. Run the program from your terminal by executing: "python project.py"

  2. Welcome Screen: You will see a welcome message and a mandatory medical disclaimer.

  3. Preference Setup: The program will ask four (y/n) questions to determine which files to create and what data to include.

  4. Medicine Entry: Type the names of your medicines one by one (e.g., "Advil", "Zyrtec"). Type 'q' when finished.

  5. Processing: The program will fetch data for each item. If a medicine is not found or the data is incomplete, it will skip that entry and notify you without crashing.

  6. Output: Once finished, check your project folder for data_report.csv and/or user_report.csv.

  ## API
  Uses openFDA Drug Label API (api.fda.gov)/(https://open.fda.gov/apis/drug/label/)
  No API key required.

  ## Additional Information - Technical Design Decisions

  🌍 Why openFDA and not an Indian API?

  While the project was conceptualized to serve a broad market, the openFDA API was selected as the primary data source due to its superior maturity, centralized structure, and developer-friendly accessibility. Several specific factors influenced this decision:

  - Standardization: Unlike the U.S. FDA, which manages a unified database for all approved drugs, pharmaceutical regulation in India is fragmented between the Central Drugs Standard Control Organisation (CDSCO) and various State Drug Control Organizations. This lack of a single "source of truth" makes unified data retrieval difficult.

  - API Accessibility: India currently lacks a single, free, government-run API equivalent to openFDA that provides structured JSON data for drug labels, warnings, and usage. Existing portals focus on regulatory filings and clinical trial licensing rather than consumer-facing lookups.

  - Data Granularity: The openFDA database is considered a global "gold standard" for open-access medical data. It provides highly granular, machine-readable sections (such as indications, dosage, and warnings) that are essential for the logic and batch-processing capabilities of this program.

  ⌨️ Why Manual Input over File Input?

  The option to upload a file (like a .txt list of medicines) was conceptualized but intentionally omitted to prioritize user experience and robustness. For a file input to work reliably, the user would have to follow strict formatting rules. Since the primary goal is a "quick check" for a consumer, a simple terminal-based loop allows for immediate entry and prevents errors caused by "dirty data" or misformatted files.

  🏗️ Why a Medicine Class?

  A Medicine class was implemented to replace the previous functional approach. This follows Object-Oriented Programming (OOP) principles, allowing the data and its formatting logic to live together.

  Encapsulation: The cleaning logic (_format_list) is hidden inside the class, making the main code much cleaner.

  Scalability: If the project grows to include more features (like unit conversions or drug-interaction checks), they can be added as methods to the class without breaking the main flow.

  📄 Why Two Output Formats?

  The program generates two distinct reports to serve two different needs:

  data_report.csv (Machine-Oriented): Uses a narrow, standardized layout that is perfect for developers or researchers who want to sort and filter data in a database or through a script.

  user_report.csv (Human-Oriented): Uses a vertical "block" layout with clear headers and separators, making it readable and "printable" for a regular consumer opening the file in Excel/Adjacent Software.

  🛡️ Why the Validation Check?

  API searches often return "best guesses." For example, searching for a specific brand might return a generic label that mentions that brand only in the fine print. The Validation Check ensures that the brand name requested by the user actually appears in the "openfda.brand_name" field of the result, preventing the storage of irrelevant or misleading information.

  ⚙️ Why User Choice (Flags)?

  Medical data is dense. A user might already know the generic name and only want to see the Caution Info (Warnings). Providing these choices prevents "information overload" and allows the user to generate a highly customized report that only contains the facts they care about.

  📊 Why CSV format?

  Comma-Separated Values (CSV) were chosen over formats like JSON or PDF because of their universal compatibility. A CSV can be opened by any spreadsheet software (Excel, Sheets, Numbers) or a plain text editor, and it requires no external libraries for the user to view the final results. It strikes the perfect balance between being "data-rich" and "user-accessible."

  ## Limitations
  - Database Scope: The tool currently only searches the U.S. FDA database.

  - Data Variability: Some prescription drugs or newer generics may have limited structured data available in the openFDA JSON response.

  - Brand Sensitivity: While validation logic is included, highly generic names may occasionally return broader results.

  - Regional Scope: Indian brand names (e.g. Cetzine, Dolo 650, Zedex) / any other Regional brand names may not be found as the FDA database covers U.S.-approved labels only.

  ## Disclaimer
  🚨 IMPORTANT: This tool is for informational purposes only. It is based on publicly available U.S. FDA information. Do not make medical decisions based on this report. Always consult a qualified physician or pharmacist before taking any action regarding your medication.

  ## Author
  Samarth Goradia

