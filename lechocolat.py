import requests
import json
from bs4 import BeautifulSoup
from validation import Validation

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

def extract_json_from_ld_script(html):
    soup = BeautifulSoup(html, 'html.parser')
    json_data = []
    
    for script in soup.find_all('script', type='application/ld+json'):
        try:
            json_text = script.string
            data = json.loads(json_text)
            json_data.append(data)
        except json.JSONDecodeError:
            continue
    
    return json_data

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(json.dumps(item, indent=4))  
            file.write("\n\n")

def validate_data(data):
    validator = Validation(data)
    errors = validator.validate()
    if errors:
        print("Validation errors found:")
        for error in errors:
            print(f" - {error}")
    else:
        print("All validations passed!")

url = 'https://www.lechocolat-alainducasse.com/uk/signature-bar-dark-the-blend-75'
html = get_html(url)

if html:
    json_data = extract_json_from_ld_script(html)
    
    save_to_file(json_data, 'lechocolat.json')
    print(f"Extracted JSON objects have been saved to 'lechocolat.json'.")
   
    print(json_data) 
if json_data:
        for product in json_data:
            print(f"Validating product data...")
            validate_data(product)