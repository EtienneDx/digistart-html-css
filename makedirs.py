import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='Creation des dossiers d\'une session digistart')
parser.add_argument('session', help="Session dans laquel créer les dossiers")

args = parser.parse_args()

apprenants = [
    "Axel_Nathia",
    "Faith_Ekuasemi",
    "Laetitia_Ngassa",
    "AUDREY_MEPIAYE",
    "LAILA_NEBBARI",
    "Chaima_Souli",
    "ERIC_YE",
    "Ovindu_Welathanthrige",
    "Laurent_CHEN",
    "Kalsoumi_Barry",
    "Souamaïla_Tamou"
]

apprenants.append("Konexio")

if not os.path.isdir(args.session):
    print("La session indiquée n'existe pas")
elif os.path.isdir("tmp"):
    print("Le dossier tmp doit être inexistant pour pouvoir utiliser ce script!")
else:
    shutil.move(args.session, "tmp")

    for n in apprenants:
        # os.mkdir(os.path.join(args.session, n))
        shutil.copytree("tmp", os.path.join(args.session, n))
    shutil.rmtree("tmp")