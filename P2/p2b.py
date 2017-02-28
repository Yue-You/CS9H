#!/usr/bin/env python
import requests
print("Input a city in a state, and get a list of ZIP codes")
city = input("City:\n")
state = input("State:\n")
url = "https://www.zipcodeapi.com/rest/zEeWXr9JOYekqVyxs5XQKb0hnQ4C1ieAWsxTUHDIGS26NADgGB6rN7IaXMNY41z1/city-zips.json/"\
      + city + "/" + state
t = requests.get(url)
data = t.json()
print(data)