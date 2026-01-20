import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check if the API call was successful
        if data['success'] and 'data' in data:
            user_data = data['data']
            users_list = user_data['data']  # This is a list of 10 users
            
            # Get the first user from the list
            first_user = users_list[0]
            print("=" * 50)
            print("FIRST USER DETAILS")
            print("=" * 50)

            for key, value in first_user.items():
                if isinstance(value, dict):
                    print(f"\n{key.upper()}:")
                    for sub_key, sub_value in value.items():
                        if isinstance(sub_value, dict):
                            print(f"  {sub_key.upper()}:")
                            for sub_sub_key, sub_sub_value in sub_value.items():
                                print(f"    {sub_sub_key}: {sub_sub_value}")
                        else:
                            print(f"  {sub_key}: {sub_value}")
                else:
                    print(f"\n{key}: {value}")
            
            print("=" * 50)
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    
    
    
    





url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"

fetch_data(url)