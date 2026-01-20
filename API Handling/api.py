import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        data = response.json()
        
        
    
    except:
        return "An error occurred while making the request."
    
    
    
    
    





url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"