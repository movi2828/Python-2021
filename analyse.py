import sys
import json
from collections import Counter

# Vérifiez s'il y a au moins un argument passé
if len(sys.argv) < 2:
    print("Error: Please provide the filename as an argument.")
    print("Usage: python script.py <filename>")
    sys.exit(1)

# Récupérez le nom du fichier à partir des arguments de la ligne de commande
filename = sys.argv[1]

# Initialiser un compteur pour stocker le nombre d'occurrences de chaque adresse IP
ip_counter = Counter()

try:
    with open(filename, 'r') as file:
        
       
             # Lire chaque ligne du fichier
                for line in file:
                    # Diviser la ligne en parties en utilisant l'espace comme séparateur
                    parts = line.strip().split(' ')
                    
                    # Extraire la première partie, qui est l'adresse IP
                    ip = parts[0]
                    
                    # Mettre à jour le compteur d'adresse IP
                    ip_counter[ip] += 1

    # Trier les adresses IP par nombre d'occurrences dans l'ordre décroissant
    sorted_ips = ip_counter.most_common()

    # Enregistrer les adresses IP triées dans un fichier JSON
    with open('results.json', 'w') as json_file:
        sorted_ips_dict = {ip: count for ip, count in sorted_ips}
        json.dump(sorted_ips_dict, json_file, indent=4)

    # Afficher les adresses IP triées par nombre d'occurrences
    for ip, count in sorted_ips:
        print(f'{ip}: {count}')


except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)
except IOError as e:
    print(f"Error: {e}")
    sys.exit(1)


