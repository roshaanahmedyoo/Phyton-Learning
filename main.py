import requests
class UserApi : 
    def __init__(self,base_url):
        self.base_url = base_url

    def get_user(self,user_id):
        try:
            resp = requests.get(self.base_url, params={"id": user_id})
            resp.raise_for_status()
            data=resp.json()
            print(resp.status_code)
            return data
        except requests.RequestException as e:
            print("Invalid Failure.. ",e)


    def create_user(self,name,email,phone):
        user ={

            "name": name,
            "email": email,
            "phone":phone
        }
        try:
            resp= requests.post(self.base_url,json = user)
            resp.raise_for_status()
            data=resp.json()
            return data

        except requests.RequestException as e:
            print ("Error")

    def get_all_users(self):
        response=requests.get(self.base_url)
        data=response.json()
        return data


api = UserApi("https://jsonplaceholder.typicode.com/users")
user=1
byid=api.get_user(12345459)
print(byid)
created=api.create_user("roshaan","adhs",939457)
print(created)
all=api.get_all_users()
print(all)        