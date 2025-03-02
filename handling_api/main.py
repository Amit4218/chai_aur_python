import requests
def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomuser/random"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        name = user_data["login"]["username"]
        location= user_data["location"]["country"]
        return name, location
    else:
        raise Exception("failed to fetch user data")
    

def main():
    try:
      username, country =   fetch_random_user()
      print(f"username: {username}, \ncountry: {country}")
    except Exception as e:
        print(str(e))



if __name__ == "__main__":

    main()