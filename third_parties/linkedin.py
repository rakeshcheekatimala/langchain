import os
from dotenv import load_dotenv
import requests

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """ scrape information from LinkedIn profiles,
        manually scrape the information from LinkedIn profile
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/rakeshcheekatimala/8f956552c232b1dbbfd2260025dc4fed/raw/541941918d1a182c0df44fbb82c6698a47338d1d/rakesh-cheekatimala.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        headers = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        params = {
            'linkedin_profile_url': linkedin_profile_url,
            'extra': 'include',
            'personal_contact_number': 'include',
            'personal_email': 'include',
            'inferred_salary': 'include',
            'skills': 'include',
            'use_cache': 'if-present',
            'fallback_to_cache': 'on-error',
        }
        response = requests.get(api_endpoint,
                                params=params,
                                headers=headers)
    data = response.json()
    return data


if __name__ == "__main__":
    print(scrape_linkedin_profile(linkedin_profile_url="https://linkedin.com/in/rakesh-cheekatimala/", mock=True))
