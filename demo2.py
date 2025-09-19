import requests


url = "https://bambooblitz-413ec-default-rtdb.asia-southeast1.firebasedatabase.app/scores.json"

# Add new player
new_player = {
    "player8": 10
}

# Use PATCH to add without overwriting existing data
response = requests.patch(url, json=new_player)

if response.status_code == 200:
    print("Player added successfully!")
else:
    print("Error:", response.text)
