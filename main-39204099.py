from classes import SakClass, Game


def guidelines():
    """
    Οδηγίες για το παιχνίδι Srabble:


    1. Κλάσεις υλοποιημένες:
       - SakClass: Αναπαριστά το σακουλάκι με τα γράμματα και τις λειτουργίες του.
       - Player: Γενική κλάση για τους παίκτες του παιχνιδιού.
       - Human: Υποκλάση του Player που αναπαριστά τον ανθρώπινο παίκτη.
       - Computer: Υποκλάση του Player που αναπαριστά τον υπολογιστή.
       - Game: Κλάση για τη λειτουργία του παιχνιδιού.
       - FileHandler: Κλάση για την διαχείριση των αρχείων.

    2. Κληρονομικότητα:
       - Η κλάση Player είναι η βασική και οι κλάσεις Human και Computer την κληρονομούν.

    3. Επέκταση Μεθόδων:
       - Η κλάση Human επεκτείνει την κλάση Player με τον έξυπνο αλγόριθμο "smart_teach".
       - Η κλάση Computer επεκτείνει την κλάση Player με τους αλγορίθμους "min", "max", "smart"

    4. Δομή Δεδομένων:
       - Οι λέξεις της γλώσσας οργανώνονται σε λεξικό (dictionary) μέσω της κλάσης SakClass.
       Όταν ο χρήστης ή ο υπολογιστής δώσουν μια λέξη ως απάντηση, αυτή ελέγχεται μέσω της is_accepted_word η οποία με
       τη σειρά της καλεί την accepted_words.get(word) (dictionary). Αν η λέξη είναι αποδεκτή, υπολογίζεται η αξία της
       μέσω της calculate_value. Χρησιμοποιείται ενα dictionary γιατί υλοποιείται μέσω ενός πίνακα κατακερματισμού,
       δηλαδή η πολυπλοκότητα για το search μια λέξης εΟ(1) (σταθερός χρόνος), πράγμα πολύ γρήγορο απο το αντίστοιχο
       search σε λίστα

    5. Αλγόριθμος Η/Υ:
       - Ο υπολογιστής υλοποιεί τους αλγόριθμους ΜΙΝ, ΜΑΧ, SMART καθώς και τον αλγόριθμο SMART_TEACH.

    Ο κώδικας περιέχει εκτενή σχόλια στις κλάσεις και τις μεθόδους του.
    """
    print(guidelines.__doc__)
    pass


if __name__ == "__main__":
    response = str(input("Καλωσήρθατε! Πληκτρολογήστε help(guidelines) για εμφάνιση οδηγιών ή run για Έναρξη του παιχνιδιού\n"))
    while response != 'help(guidelines)' and response != 'run':
        print("ΜΗ ΕΠΙΤΡΕΠΤΗ ΕΠΙΛΟΓΗ, ΕΠΙΛΕΞΕ ΞΑΝΑ")
        response = input()

    if response == "help(guidelines)":
        guidelines()
        input("Πατήστε οποιοδήποτε πλήκτρο για συνέχεια στο παιχνίδι:")
        sak = SakClass()
        game = Game()
    elif response == "run":
        sak = SakClass()
        game = Game()