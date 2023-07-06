import requests
import json

url = "https://us-central1-aipractice-interactivesl.cloudfunctions.net/identifytheme"

topics = [
    "0.018*stock + 0.017*advertisement + 0.010*data + 0.009*marketwatch + 0.008*retirement + 0.007*icon + 0.007*market + 0.007*inflation + 0.006*markets + 0.006*search",
    "0.021*market + 0.008*icon + 0.008*news + 0.007*stock + 0.006*word + 0.006*insider + 0.005*search + 0.005*business + 0.005*price + 0.005*apple",
    "0.019*disney + 0.006*martin + 0.004*belief + 0.004*dtc + 0.004*dis + 0.003*lucas + 0.003*library + 0.003*florida + 0.003*promised + 0.003*pixar",
    "0.032*best + 0.025*stock + 0.022*stocks + 0.019*fool + 0.016*motley + 0.014*market + 0.013*retirement + 0.013*return + 0.012*cards + 0.012*services",
    "0.019*stock + 0.013*powr + 0.008*trade + 0.008*stocks + 0.007*market + 0.007*options + 0.007*call + 0.007*put + 0.007*rated + 0.006*buy",
    "0.013*berkshire + 0.010*buffett + 0.006*stock + 0.006*house + 0.006*insurance + 0.005*bank + 0.005*china + 0.004*said + 0.004*committee + 0.004*mccarthy",
    "0.022*stock + 0.014*apple + 0.014*kiplinger + 0.011*market + 0.008*published + 0.007*today + 0.007*stocks + 0.007*buy + 0.006*debt + 0.006*may",
    "0.015*market + 0.012*exhibit + 0.010*stock + 0.007*penny + 0.007*stocks + 0.007*trade + 0.006*share + 0.006*data + 0.006*apple + 0.005*news",
    "0.024*new + 0.020*open + 0.010*access + 0.009*denied + 0.008*page + 0.008*please + 0.008*billion + 0.008*javascript + 0.008*cooky + 0.008*browser",
    "0.013*crypto + 0.011*investment + 0.009*buy + 0.009*stocksbest + 0.007*apple + 0.007*real + 0.007*invest + 0.007*trade + 0.007*alternative + 0.007*etfsbest"
]



results = []

for topic in topics:
    payload = json.dumps({
        "message": topic
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    results.append(response.text)

for result in results:
    print(result)
