import requests

def lookup(frm):
    response = requests.get(f"https://api.exchangeratesapi.io/latest?base={frm}")
    ans = response.json()
    print(ans)


frm = input("Enter Currency: ")
lookup(frm)
