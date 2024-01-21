import requests

url = "https://hub.vong.earth/draftfile.php/1144/user/draft/561493929/event17.jpg"
filename = "avn.jpg"  # You can specify the filename you want to save

response = requests.get(url)

if response.status_code == 200:
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"File '{filename}' downloaded successfully.")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
    print(f"Response content: {response.text}")
