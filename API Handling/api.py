import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        data = response.json()
        if data['success'] and 'data' in data:
            print("Fetched Data:")
        # print(data)
        
    except:
        return "An error occurred while making the request."
    
    
    
    
    





url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"

fetch_data(url)