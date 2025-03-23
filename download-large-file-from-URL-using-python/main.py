import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def download_file(url, local_filename, session):
    try:
        with session.get(url, stream=True, timeout=10) as response:
            response.raise_for_status()  # Raise an error on bad status codes
            with open(local_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):  # 8KB chunks
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
        print(f"Downloaded {local_filename} successfully.")
    except Exception as e:
        print(f"Error downloading {local_filename}: {e}")

def create_session_with_retries():
    session = requests.Session()
    # Configure retries: 5 attempts with exponential backoff
    retries = Retry(
        total=5,
        backoff_factor=0.3,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET", "POST"]
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

if __name__ == "__main__":
    # Example URL and filename
    url = "https://example.com/largefile.zip"
    local_filename = "largefile.zip"
    
    # Create a session with retries enabled
    session = create_session_with_retries()
    
    # Download the file
    download_file(url, local_filename, session)
