import requests

# The URL where the file is located
url = 'https://www.arvancloud.ir/en/ips.txt'

# Use the requests library to download the file
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the content of the response to a file named 'arvan.txt'
    with open('arvan.txt', 'wb') as file:
        file.write(response.content)
    print("File has been downloaded and saved as arvan.txt")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
