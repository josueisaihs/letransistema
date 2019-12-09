import requests

form = {
    'ci': '98050920900', 
    'rasp': 'Rasp1',
}

con = requests.post(
    'localhost:8000/docencia/grouplist/assistence/rasp', 
    data=form
)

print(con)