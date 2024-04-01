airport = [
     {
        "name": "Beijing Capital International Airport",
        "code": "PEK",
        "country": "China"
    },
    {
        "name": "Los Angeles International Airport",
        "code": "LAX",
        "country": "United States"
    },
    {
        "name": "London Heathrow Airport",
        "code": "LHR",
        "country": "United Kingdom"
    }
]

for air in airport:
    print(f"{air['name']} ({air['code']}) is in {air['country']}.")