students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
    'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

name = input("Entrez le nom de l’étudiant :  ")

if name in students.keys():
    print(f"Notes de {name} :  ")
    notes = []
    for matiere, note in students.get(name).items():
        print(f"{matiere} : {note}")
        notes.append(note)
    print(f"Moyenne de {name} : {round(sum(notes)/len(notes), 2)}")

else:
    print(f"L'étudiant {name} n'existe pas dans la liste.")
