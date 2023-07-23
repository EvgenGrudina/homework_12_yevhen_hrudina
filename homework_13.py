import json
from pprint import pprint
from os import mkdir, chdir
from shutil import rmtree
import csv
from ganres_list import ganres
from films_data import films_data

root_folder = "ganres"


rmtree(root_folder)


mkdir(root_folder)
chdir(root_folder)


ganres_dict = json.loads(ganres)


for ganre in ganres_dict["results"]:
    mkdir(f"{ganre['ganre']}")


    csv_file_path = f"{ganre['ganre']}/films.csv"
    with open(csv_file_path, "w") as file_obj:
        csv_file = csv.writer(file_obj)
        csv_file.writerow(["title", "year", "rating", "type", "ganres"])


for film in films_data:
    film_ganres = ""

    for film_gen in film["gen"]:
        films_info = []
        film_ganres += film_gen['ganre'] + "; "

    for film_gen in film["gen"]:
        csv_file_path = f"{film_gen['ganre']}/films.csv"
        with open(csv_file_path, "a", newline="") as file_obj:
            headers = ["title", "year", "rating", "type", "gen"]
            csv_file = csv.DictWriter(file_obj, fieldnames=headers, extrasaction="ignore")
            film["gen"] = film_ganres
            csv_file.writerow(film)
