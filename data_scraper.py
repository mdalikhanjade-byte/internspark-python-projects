import requests
import re

def run_simple_scraper():
    print("--- Web Data Scraping Tool (Task 3) ---")
    
    # Using a reliable public page meant for testing and scraping
    url = "https://example.com"
    print(f"Connecting and downloading HTML content from: {url}...\n")
    
    try:
        # Step 1: Send a request to fetch the webpage
        response = requests.get(url, timeout=5)
        
        # Exception Handling: Check if the webpage loaded successfully
        response.raise_for_status()
        
        # Get the raw HTML text
        html_content = response.text
        
        print("--- Extraction Successful! ---")
        
        # Step 2: Use Regular Expressions to parse out data fields cleanly
        # Extract the main title page header (<h1> tags)
        titles = re.findall(r'<h1>(.*?)</h1>', html_content)
        print("\n[Extracted Page Headers (H1)]:")
        for title in titles:
            print(f"-> {title.strip()}")
            
        # Extract the paragraph text (<p> tags)
        paragraphs = re.findall(r'<p>(.*?)</p>', html_content)
        print("\n[Extracted Paragraph Content]:")
        for p in paragraphs:
            # Clean up any raw HTML link tags inside the paragraph text
            clean_p = re.sub(r'<.*?>', '', p)
            print(f"-> {clean_p.strip()}")
            
    except requests.exceptions.Timeout:
        print("Error: The website took too long to respond. Connection timed out.")
    except requests.exceptions.RequestException as e:
        print(f"Scraping Error: Failed to retrieve data. Details: {e}")

if __name__ == "__main__":
    run_simple_scraper()