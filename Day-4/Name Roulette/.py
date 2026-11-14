names_string = "Yash, Divya, kirti, Surta"
names = names_string.split(", ")

import random

num_items = len(names)

random_choice = random.randint(0, num_items - 1)
print(names[random_choice])



#Program of Cities of Rajasthan

cities_of_rajasthan = [
    "Ajmer", "Alwar", "Anupgarh", "Balotra", "Banswara", "Baran", 
    "Barmer", "Beawar", "Bharatpur", "Bhilwara", "Bikaner", "Bundi", 
    "Chittorgarh", "Churu", "Dausa", "Deeg", "Dholpur", "Didwana", 
    "Dudu", "Dungarpur", "Gangapur City", "Hanumangarh", "Jaipur", 
    "Jaisalmer", "Jalore", "Jhalawar", "Jhunjhunu", "Jodhpur", 
    "Karauli", "Kekri", "Khairthal", "Kishangarh", "Kota", "Kotputli", 
    "Kuchaman City", "Mount Abu", "Nagaur", "Neem Ka Thana", "Pali", 
    "Phalodi", "Pratapgarh", "Rajsamand", "Salumber", "Sanchore", 
    "Sawai Madhopur", "Shahpura", "Sikar", "Sirohi", "Sri Ganganagar", 
    "Sujangarh", "Tonk", "Udaipur"
]

total_states = len(cities_of_rajasthan)
import random

random_state = random.randint(0, total_states - 1)

print(cities_of_rajasthan[random_state])
