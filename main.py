import os
from scrapers import glassdoor_scraper, ambitionbox_scraper

def write_dummy_file(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("Scraper run completed. Replace this with actual scraped content.")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    companies = [("Google", "SDE"), ("Amazon", "Data Analyst"), ("Anora", "Electronics")]

    for company, role in companies:
        print(f"[Glassdoor] Scraping {company} - {role} with login ***")
        try:
            glassdoor_scraper.scrape(company, role,
                os.environ.get("GLASSDOOR_USER"), os.environ.get("GLASSDOOR_PASS"))
        except Exception as e:
            print(f"[Glassdoor] Failed for {company}: {e}")
        
        print(f"[AmbitionBox] Scraping {company} - {role} (no login needed)")
        try:
            ambitionbox_scraper.scrape(company, role)
        except Exception as e:
            print(f"[AmbitionBox] Failed for {company}: {e}")

    # ✅ Force Git to detect a file inside data/
    write_dummy_file("data/success.txt")
