import pandas as pd
import requests
from bs4 import BeautifulSoup

# Specify the path to your CSV file
csv_file_path = r"alphavantage\apple\apple_march.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Create a new column for the content
df['content'] = ""

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    url = row['url']
    content = ""

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        lines = soup.get_text().splitlines()
        content = ' '.join(line.strip() for line in lines if line.strip())
    except Exception as e:
        print(f"Error occurred while scraping {url}: {str(e)}")

    # Assign the scraped content to the 'content' column
    df.at[index, 'content'] = content

# Save the updated DataFrame to a new CSV file
output_csv_file_path = r'alphavantage\apple\apple_march_with_content.csv'
df.to_csv(output_csv_file_path, index=False)

print("Data saved to CSV file:", output_csv_file_path)
