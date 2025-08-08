# Interview Auto Scraper (Public Resource)

This repository **automatically collects interview questions** from platforms like Glassdoor and AmbitionBox for various companies and roles.

## 🔄 How it works
- Scrapers fetch interview questions for each company/role
- Glassdoor requires login (credentials stored securely in GitHub Actions)
- AmbitionBox is public and requires no login
- GitHub Actions runs weekly and updates the repo with new data

## 📁 Folder Structure
- `/data/` - Raw questions by company and role
- `/output/` - Summary reports (PDFs, CSVs, etc.)
- `/scrapers/` - Scraping logic for each site
- `/main.py` - Entry point to run everything
- `.github/workflows/` - GitHub Actions automation

## ✅ How to Use (as a visitor)
- Just explore the `/data` or `/output` folders
- No setup, login, or installation needed!

## 🔐 Maintainer Instructions (for Kishan only)
1. Add your secrets in GitHub:
   - `GLASSDOOR_USER`
   - `GLASSDOOR_PASS`
2. GitHub Actions will use your creds to pull latest data weekly
3. Data gets pushed to the repo for public access

## 🧠 Want to Contribute?
Pull Requests welcome for:
- New platforms
- Improved formatting
- More company/role pairs

---
Made with ❤️ to help job seekers everywhere.