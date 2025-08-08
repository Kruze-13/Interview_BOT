import os
from scrapers import glassdoor_scraper, ambitionbox_scraper

if __name__ == "__main__":
    # Make sure the data/ folder exists
    os.makedirs("data", exist_ok=True)

    companies = [
        ("Google", "SDE"),
        ("Amazon", "Data Analyst"),
        ("Anora", "Electronics")
    ]

    for company, role in companies:
        print(f"Scraping {company} - {role}")
        
        try:
            glassdoor_scraper.scrape(
                company, role,
                os.environ.get("GLASSDOOR_USER"),
                os.environ.get("GLASSDOOR_PASS")
            )
        except Exception as e:
            print(f"Glassdoor failed for {company}: {e}")
        
        try:
            ambitionbox_scraper.scrape(company, role)
        except Exception as e:
            print(f"AmbitionBox failed for {company}: {e}")

    # 🔧 Test file to ensure Git has something to commit
    with open("data/test_run.txt", "w") as f:
        f.write("Scraper ran successfully.")
