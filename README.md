<a href="url"><img src="https://github.com/GoliathReaper/JobSailor/assets/77969919/f3003461-ea38-4f35-9692-7925b24034af" align="centre" width="800" ></a>





# JobSailor

This project is an automated script that applies for jobs on Naukri.com and answers questions asked during the application process using the Gemini AI API. The script is written in Python and utilizes the Selenium WebDriver to navigate and interact with web pages.

## Introduction

This script automates the process of applying to jobs listed on Naukri.com. It uses Selenium WebDriver to navigate the Naukri website, locate job listings, and submit job applications. Additionally, it interacts with the Gemini AI to answer questions that may be part of the job application process.


## Video Showcase
[![YouTube](http://i.ytimg.com/vi/emFERSfJDAU/hqdefault.jpg)](https://www.youtube.com/watch?v=emFERSfJDAU)





## Features

- Automates job application on Naukri.com
- Skips already applied or expired job listings
- Answers questions during the application process using Gemini AI API
- Logs the count of successfully applied and failed job applications

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your local machine
- `selenium` library installed (`pip install selenium`)
- Firefox browser installed
- Geckodriver executable compatible with your Firefox version
- Gemini AI API credentials ([Gemini AI API](https://ai.google.dev/gemini-api/docs/api-key))

## Setup Instructions

1. **Install Python and Pip:**

   Clone the repository:

   ```bash
   git clone  https://github.com/GoliathReaper/JobSailor.git
  
   
   Download and install Python from the [official website](https://www.python.org/). Pip, the package installer for Python, is included in Python installations.

3. **Install Selenium:**

   Open your terminal or command prompt and run the following command:
   
   ```bash
   pip install selenium
   ```

4. **Download Geckodriver:**

   Download the Geckodriver from the [Geckodriver releases page](https://github.com/mozilla/geckodriver/releases) and extract the executable to a directory of your choice.

5. **Prepare Your Firefox Browser:**

   Ensure you have Firefox installed. Note the path to your Firefox executable and your Firefox profile path.

6. **Clone the Repository:**

   Clone or download this repository to your local machine.

7. **Configuration:**

   Update the following variables in your script with the correct paths and settings:

   ```python
   driver_path = "path_to_geckodriver_executable"
   binary = "path_to_firefox_executable"
   profile_path = "path_to_firefox_profile"
   ```

8. **Create CSV File:**

   Prepare a CSV file named `jobs.csv` containing job links. Each line in the CSV should be a relative link to a job on Naukri.com.

   Example `jobs.csv` content:
   ```csv
   /job-listings-python-backend-developer-adfolks-kochi-1-to-3-years-050624502539
   /job-listings-software-engineer-xyz-corp-bangalore-2-to-4-years-050624503123
   ```

9. **Run the Script:**

   Execute the script:

   ```bash
   python apply_jobs.py
   ```

   The script will read job links from `jobs.csv`, navigate to each job listing, and apply if not already applied or expired. It will also answer questions using the Bard AI API.

## Usage

- Ensure the CSV file (`jobs.csv`) is in the same directory as your script.
- Run the script and monitor the output for the status of job applications.
- The script logs the count of successfully applied and failed job applications.

## Notes

- Make sure to handle exceptions and errors gracefully.
- You might need to update XPaths and selectors based on changes in the Naukri.com website.
- Ensure the Bard AI API is set up correctly and accessible from your script.

## Disclaimer

Use this script responsibly and ensure compliance with Naukri.com's terms of service. Automating job applications may violate their policies and could result in account suspension or other consequences.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License
