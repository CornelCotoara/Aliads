#run
import requests
from urllib.parse import urljoin

def grab_and_curate_alibaba_ads(url, output_file):
    """
    Fetches Alibaba ads data from the provided URL, removes "@ads" endings,
    and saves the curated data to a text file.

    Args:
        url (str): The URL of the Alibaba ads data on GitHub.
        output_file (str): The name of the output text file.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        with open(output_file, 'w') as outfile:
            for line in response.text.splitlines():
                curated_line = line.rstrip(" @ads")  # Remove "@ads" efficiently
                outfile.write(curated_line + '\n')

        print(f"Successfully curated Alibaba ads data to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")

if __name__ == '__main__':
    base_url = "https://raw.githubusercontent.com/v2ray/domain-list-community/refs/heads/master/data/"
    url = urljoin(base_url, "alibaba-ads")
    output_file = "curated_alibaba_ads.txt"

    grab_and_curate_alibaba_ads(url, output_file)
