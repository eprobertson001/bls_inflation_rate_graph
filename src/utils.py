import requests
import requests_cache

class APIClient:
    def __init__(self, path, headers=None, auth=None, timeout=10, cache_name='api_cache', cache_expire=600):
        self.session = requests_cache.CachedSession(cache_name, expire_after=cache_expire)
        self.path = path.rstrip("/")
        self.headers = headers
        self.auth = auth
        self.timeout = timeout

    # GET request
    def get_api(self, endpoint, params=None):
        try:
            if endpoint:
                endpoint = endpoint.lstrip('/')
            response = self.session.get(
                f"{self.path}/{endpoint.lstrip("/")}",
                headers=self.headers,
                params=params,
                auth=self.auth,
                timeout=self.timeout
            )
            if response.from_cache:
                print("Response served from cache")
                response.raise_for_status()
                return response.json()
            
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Connection Error: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")


    def post_api(self, endpoint=None, json=None, data=None, params=None, files=None):
        try:
            if endpoint:
                endpoint = endpoint.lstrip('/')
            response = self.session.post(
                f"{self.path}/{endpoint}",
                headers=self.headers,
                json=json,
                data=data,
                params=params,
                files=files,
                auth=self.auth,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
                
        except requests.exceptions.HTTPError as errh:
            print(f"Oops, GET request failed. HTTP Error: {errh}")
            return None
        except requests.exceptions.ConnectionError as errc:
            print(f"Oops, GET request failed.Connection Error: {errc}")
            return None
        except requests.exceptions.Timeout as errt:
            print(f"Oops, GET request failed.Timeout Error: {errt}")
            return None
        except requests.exceptions.RequestException as err:
            print(f"Oops, GET request failed.Request Exception: {err}")
            return None