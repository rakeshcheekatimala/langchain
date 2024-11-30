import requests
if __name__ == "__main__":
    api_endpoint = 'https://gist.githubusercontent.com/rakeshcheekatimala/8f956552c232b1dbbfd2260025dc4fed/raw/541941918d1a182c0df44fbb82c6698a47338d1d/rakesh-cheekatimala.json'
    response = requests.get(api_endpoint,
                            params={},
                            headers={})
    print(response.json())
