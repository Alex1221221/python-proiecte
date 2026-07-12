import requests
from plyer import notification


def cauta_vremea():
    rulare = True

    while rulare == True:
        oras = input("Ce oras vrei sa cauti? (sau scrie 'nu' ca sa opresti): ")

        if oras == "nu" or oras == "NU" or oras == "Nu":
            print("Aplicatia s-a oprit!")
            rulare = False
            break

        url1 = "https://geocoding-api.open-meteo.com/v1/search"
        p1 = {"name": oras, "count": 1}
        req1 = requests.get(url1, params=p1)
        date_geo = req1.json()

        if "results" in date_geo:
            #Luam prima locatie gasita din lista
            oras_gasit = date_geo["results"][0]
            lat = oras_gasit["latitude"]
            lon = oras_gasit["longitude"]
            nume = oras_gasit["name"]

            url2 = "https://api.open-meteo.com/v1/forecast"
            p2 = {"latitude": lat, "longitude": lon, "current_weather": True}
            req2 = requests.get(url2, params=p2)
            date_vreme = req2.json()

            vreme_acum = date_vreme["current_weather"]
            grade = vreme_acum["temperature"]
            vant = vreme_acum["windspeed"]

            print("\n--- REZULTAT VREME ---")
            print("Locatie:", nume)
            print("Grade:", grade, "C")
            print("Vant:", vant, "km/h")
            print("----------------------\n")

            notification.notify(
                title="Vreme " + nume,
                message="Temp: " + str(grade) + "C, Vant: " + str(vant) + "km/h",
                timeout=4
            )
        else:
            print("Numele introdus nu exista in baza de date. Incearca iar.\n")


#Apelam functia ca sa porneasca programul
cauta_vremea()