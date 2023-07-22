import os
import shutil
from string import ascii_uppercase
from hp_titles import films_titles
from hp_awards import films_awards


root_folder = "Harry Potter"

shutil.rmtree(root_folder)

os.mkdir(root_folder)
os.chdir(root_folder)

for film_name in films_titles["results"]:
    os.mkdir(film_name["title"])


    for letter in ascii_uppercase:
        os.mkdir(f"{film_name['title']}/Folder_{letter}")


    film_awards = []
    for results in films_awards:
        for movie in results["results"]:
            if movie["movie"]["title"] == film_name["title"]:
                film_award = {
                    "type": movie["type"],
                    "award_name": movie["award_name"],
                    "award": movie["award"],
                    }
                film_awards.append(film_award)


            film_awards_sorted = sorted(film_awards, key=lambda award: award['award_name'])


            for event in film_awards_sorted:
                txt_file = f"{film_name['title']}/Folder_{event['award_name'][0].upper()}/{event['award_name']}.txt"
                txt_obj = open(txt_file, "w")
                txt_obj.close()


            for event in film_awards_sorted:
                txt_file = f"{film_name['title']}/Folder_{event['award_name'][0].upper()}/{event['award_name']}.txt"
                txt_obj = open(txt_file, "a")
                txt_obj.write(f"{event['award']}\n")
                txt_obj.close()