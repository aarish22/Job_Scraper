# 🕵️‍♂️ Job Scraper Script

## About the Project

This project is a Python-based web scraper designed to help job seekers find relevant job postings on TimesJobs.com. The script allows users to input their skills and fetches job listings that match those skills and have been posted recently.

## Features

- **Skills Matching**: The script filters job postings based on the skills provided by the user.
- **Recent Job Listings**: It retrieves only those job listings that were posted a few days ago, ensuring that the job opportunities are current.
- **Automation**: The script runs in a loop, fetching new results at regular intervals (every 2 seconds).

## Technologies Used

- **Python**: The core programming language used for the script.
- **BeautifulSoup**: For parsing HTML and extracting information from web pages.
- **Requests**: To make HTTP requests and fetch the web page content.
- **LXML**: The parser used by BeautifulSoup for processing HTML.

## How It Works

1. **Input Skills**: The user is prompted to enter their skills in a comma-separated format.
2. **Fetch Job Listings**: The script sends a request to TimesJobs.com and retrieves job listings that match the specified criteria.
3. **Filter and Display**: It filters the jobs based on the user's skills and the posting date, then displays the relevant job details, including company name, required skills, and the job link.
4. **Loop**: The script runs continuously, updating the results every 2 seconds.

## Usage

1. **Clone the Repository**: 
    ```bash
    git clone https://github.com/yourusername/job-scraper.git
    cd job-scraper
    ```

2. **Install Dependencies**:
    Ensure you have `requests` and `BeautifulSoup` installed. If not, install them using:
    ```bash
    pip install requests beautifulsoup4 lxml
    ```

3. **Run the Script**:
    ```bash
    python job_scraper.py
    ```

4. **Enter Skills**:
    When prompted, enter the skills you are familiar with, separated by commas.

5. **View Results**:
    The script will continuously fetch and display job postings that match your skills and are posted recently.

## Example Output

```plaintext
Enter the skills you are familiar with (in comma separated way): Python, SQL

Company Name: ABC Corp
Skills Needed: ['Python', 'Django', 'SQL']
Job Link: https://www.timesjobs.com/job-detail/software-developer-abc-corp-bangalore-2-5-years-xyz123.html

Please Wait

Company Name: XYZ Ltd
Skills Needed: ['Python', 'Flask', 'PostgreSQL']
Job Link: https://www.timesjobs.com/job-detail/backend-developer-xyz-ltd-mumbai-3-7-years-abc456.html

Please Wait
