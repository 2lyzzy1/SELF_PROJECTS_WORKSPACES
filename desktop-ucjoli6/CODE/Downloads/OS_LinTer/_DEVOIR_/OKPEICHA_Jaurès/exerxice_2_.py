
candidat_5_succesd_ = {
    "name_":
        ["ADE Lucas", "AGBO Ed", "AKO Anne", "AZA Yves", "OYO Jean", ],
    "moyennes_phases_ecrites":
        [15.33, 14.33, 14.67, 16.33, 17.25, ],
}   # matieres_ = ["Français", "Maths", "Informatiques"]

def main():
    print(f"\n")    # SPACE
    for nom_ in candidat_5_succesd_["name_"]:
        #   foreach( candidat ) ->
        print(f"\n{"-"*75}")
        for _candidatDatabaseLabel in candidat_5_succesd_.keys():
            print(f"| {_candidatDatabaseLabel.replace('_', ' '):>24} |", end="")
        #listeCandidatHeader = ""; #listeCandidatHeader += ( _C5S_ for _C5S_ in candidat_5_succesd_.keys() ); #(print(f" {_C5S_:>21} ", end="") for _C5S_ in candidat_5_succesd_.keys())
        print(f"\n{"-"*75}")
        for nom_, moy_ph_writen in\
                zip(candidat_5_succesd_["name_"], candidat_5_succesd_["moyennes_phases_ecrites"]):
            cData_ = f"| {nom_:>24} || {moy_ph_writen:>24} |"
            print(f"{cData_}")
            print(f"{"-"*(len(cData_)+2)}")
            #
        # MENU
        response_, essaies = '', 0
        #   if response_ not in system reserve
        # response_not_in_options_ = (response_ not in ['A', 'Q'])
        while response_ not in ['A', 'Q']:
            response_ = input(
            f" \n\
            Choisissez une opération \n\
            A : Ajouter une note d'entretien \n\
            Q : Quitter \n\
            A | Q \n ->\
            ")
            if essaies > 0 and response_ not in ['A', 'Q']:
                print(f"Essaie n°{essaies+1} passée.\n Veuillez réessayer !")
            essaies+=1
            #
        #
        #while response_ != "Q":
        if response_.upper() == "A":
            name_att_ = ""
            while name_att_ not in candidat_5_succesd_["name_"]:
                name_att_ = input("Entrez le nom et prénom du candidat auquel vous souhaitez ajouter une note \n -> ")
            #
            note_ = int( input("Quelle note voulez-vous ajouter ?\n -> ") )
            moyenne_generale_ = \
                (candidat_5_succesd_["moyennes_phases_ecrites"]\
                 [candidat_5_succesd_["name_"].index(name_att_)] \
                + note_) / 2
            #
            # VERDICT D'ADMISSION
            print(f"Opération effectuée. La moyenne générale de {name_att_} est de {moyenne_generale_}.")
            if moyenne_generale_ >= 15:
                print(f"-> {name_att_} est admis(e).")
            else:
                print(f"-> {name_att_} est refusé(e).")
        #
        elif response_ == "Q":
            break
        print(f"\n")
        #
    #
if __name__ == '__main__':
    main()

