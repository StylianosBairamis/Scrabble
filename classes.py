import json
import uuid
from random import choices
from itertools import permutations


# 1) Πρώτη τιμή = πλήθος γραμμάτων στο παιχνίδι
# 2) Δεύτερη τιμή = αξία γράμματος στο παιχνίδι

# Ο έλεγχος εγκυρότητας της κάθε προτεινόμενης λέξης μπορεί να γίνεται με αναζήτηση στις αποδεκτές λέξεις («Λεξικό γλώσσας»)

# python magic methods start and end with __, also called dunder methods. They are defined by build in classes

def guidelines():
    """
    Εμφανίζει τις οδηγίες και την τεκμηρίωση για το παιχνίδι Scrabble.

    Usage:
        help(guidelines)
    """
    pass
    # Καλώντας τη συνάρτηση guidelines, θα εμφανιστούν οι οδηγίες σου μέσω του help()
    guidelines.__doc__ = f"""Οδηγίες και τεκμηρίωση για το παιχνίδι Scrabble.
Χρησιμοποίησε `help(guidelines)` για να δεις αυτό το μήνυμα.
"""


help(guidelines)


def get_accepted_words() -> dict:
    """
        Επιστρέφει ένα λεξικό με τις αποδεκτές λέξεις από το αρχείο "greek7.txt".

        Returns:
        dict: Το λεξικό με τις αποδεκτές λέξεις.
        """
    words = {}  # Χρησιμοποιώ ενα dictionary γιατί υλοποιείται μέσω ενός πίνακα κατακερματισμού,
    # δηλαδή η πολυπλοκότητα για το search μια λέξης εΟ(1) (σταθερός χρόνος), πράγμα πολύ γρήγορο απο το αντίστοιχο
    # search σε λίστα

    with open('greek7.txt', 'r', encoding='utf-8') as file:
        for line in file:
            words[line.strip('\n')] = '_'

    return words


class SakClass:
    """
        Η κλάση SakClass αναπαριστά το σακουλάκι με τα γράμματα και τις απαραίτητες λειτουργίες.

        Attributes:
        accepted_words (dict): Το λεξικό με τις αποδεκτές λέξεις.
        lets (dict): Το λεξικό με τα γράμματα και τις τιμές τους.
        letters_left (int): Το πλήθος των γραμμάτων που απομένουν στο σακουλάκι.
        """
    accepted_words = get_accepted_words()

    def __init__(self):

        self.lets = {'Α': [12, 1], 'Β': [1, 8], 'Γ': [2, 4], 'Δ': [2, 4], 'Ε': [8, 1],
                     'Ζ': [1, 10], 'Η': [7, 1], 'Θ': [1, 10], 'Ι': [8, 1], 'Κ': [4, 2],
                     'Λ': [3, 3], 'Μ': [3, 3], 'Ν': [6, 1], 'Ξ': [1, 10], 'Ο': [9, 1],
                     'Π': [4, 2], 'Ρ': [5, 2], 'Σ': [7, 1], 'Τ': [8, 1], 'Υ': [4, 2],
                     'Φ': [1, 8], 'Χ': [1, 8], 'Ψ': [1, 10], 'Ω': [3, 3]}

        self.letters_left = sum([self.lets[key][0] for key in self.lets.keys()])

    def get_letters(self, n: int) -> list[str]:
        """
        Επιστρέφει n τυχαία γράμματα από το σακουλάκι με επανατοποθέτηση.

        Args:
        n (int): Το πλήθος των γραμμάτων που θέλουμε να επιστραφούν.

        Returns:
        list: Μια λίστα με τα τυχαία επιλεγμένα γράμματα.
        """

        if self.letters_left < n:
            num_of_letters = self.letters_left
        else:
            num_of_letters = n

        letters = choices([letter for letter in self.lets.keys() if self.lets[letter][0] > 0], k=num_of_letters)

        self.letters_left -= num_of_letters

        for letter in letters:
            self.lets[letter][0] -= 1

        return letters

    def return_letters(self, letters: list[str]):
        """
        Επιστρέφει γράμματα στο σακουλάκι.

        Args:
        letters (list): Η λίστα με τα γράμματα προς επιστροφή στο σακουλάκι.

        """
        for letter in letters:
            self.lets[letter][0] += 1

    def is_accepted_word(self, word: str) -> bool:

        """
        Έλεγχος εάν μια λέξη είναι αποδεκτή.

        Args:
        word (str): Η λέξη προς έλεγχο.

        Returns:
        bool: Επιστρέφει True αν η λέξη είναι αποδεκτή, αλλιώς False.
        """

        result = self.accepted_words.get(word, '404')

        return result != '404'

    def calculate_value(self, word: str) -> int:
        """

        Υπολογίζει την αξία μιας λέξης βάσει των γραμμάτων της.

        Args:
        word (str): Η λέξη για την οποία θα υπολογιστεί η αξία.

        Returns:
        int: Η αξία της λέξης.

        """

        return sum([self.lets[letter][1] for letter in word])


class Player:
    """
       Η γενική κλάση για τους παίκτες του παιχνιδιού.

       Attributes:
       name (str): Το όνομα του παίκτη.
       score (int): Οι βαθμοί του παίκτη.
       letters (list): Τα γράμματα που διαθέτει ο παίκτης.
       """

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.letters = None

    def print_general_details(self):
        print('*' * 20)
        print(f'*** Παίκτης: {self.name} *** Σκορ: {self.score}', f'Γράμματα: {self.letters}', sep='\n')
        print('*' * 20)

    def print_word_choice_details(self, choice, increasement, sak):

        self.score += increasement

        print(f'ΣΤΟ ΣΑΚΟΥΛΑΚΙ ΥΠΑΡΧΟΥΝ {sak.letters_left} ΓΡΑΜΜΑΤΑ')
        print(f'ΛΕΞΗ: {choice}')
        print(f'ΑΠΟΔΕΚΤΗ ΛΕΞΗ - ΒΑΘΜΟΙ: {increasement} - ΣΚΟΡ: {self.score}')

    def check_word_letters(self, word: str):
        for letter in word:
            if letter not in self.letters:
                return False

        return True

    def add_letters(self, new_letters):
        self.letters.extend(new_letters)

    def remove_letters(self, word: str):
        for letter in word:
            if letter in self.letters:
                self.letters.remove(letter)

    def algorithm_smart(self, sak):

        max_value = -999

        best_permutation = None

        for i in range(2, 8):

            i_permutations = self.calculate_permutations(i)

            for permutation in i_permutations:

                permutation = ''.join(permutation)

                if sak.is_accepted_word(permutation):

                    current_value = sak.calculate_value(permutation)

                    if current_value > max_value:
                        max_value = current_value

                        best_permutation = permutation

            return best_permutation

    def calculate_permutations(self, num_of_letters):
        return permutations(self.letters, num_of_letters)


class Human(Player):
    """
       Η υποκλάση Human αναπαριστά τον ανθρώπινο παίκτη.

       Methods:
       algorithm_smart: Έξυπνος αλγόριθμος για την ενημέρωση του παίκτη για την καλύτερη δυνατή απάντηση που θα μπορούσε να δώσει .
       """


class Computer(Player):
    """
        Η υποκλάση Computer αναπαριστά τον υπολογιστή.

        Methods:
        algorithm_min: Αλγόριθμος που επιλέγει τη μικρότερη δυνατή λέξη.
        algorithm_max: Αλγόριθμος που επιλέγει τη μεγαλύτερη δυνατή λέξη.
        algorithm_smart: Ένας έξυπνος αλγόριθμος που επιλέγει τη βέλτιστη λέξη για να παίξει ο υπολογιστής.
        """

    def algorithm_min(self, sak):

        for i in range(2, 8):

            i_permutations = self.calculate_permutations(i)

            for permutation in i_permutations:

                permutation = ''.join(permutation)

                if sak.is_accepted_word(permutation):
                    return permutation

    def algorithm_max(self, sak):

        for i in range(7, 1, -1):

            i_permutations = self.calculate_permutations(i)

            for permutation in i_permutations:

                permutation = ''.join(permutation)

                if sak.is_accepted_word(permutation):
                    return permutation


class Game:
    """
       Η κλάση Game αναπαριστά το παιχνίδι Scrabble.

       Attributes:
       ph (Human): Ο ανθρώπινος παίκτης.
       pc (Computer): Ο υπολογιστής.
       sak (SakClass): Το σακουλάκι με τα γράμματα.
       algorithm_chosen (str): Ο αλγόριθμος που επιλέγεται για τον υπολογιστή.
       moves (int): Ο αριθμός των γύρων που έχουν παιχτεί.
       """

    algorithms = ['MIN', 'MAX', 'SMART', 'SMART_TEACH']

    def __init__(self):
        self.ph = Human("ΣΤΕΛΙΟΣ")
        self.pc = Computer("Η/Υ")
        self.sak = SakClass()
        self.file_handler = FileHandler()
        self.algorithm_chosen = None
        self.moves = 0

        self.setup()

    def setup(self):
        """Ρυθμίζει τις αρχικές παραμέτρους του παιχνιδιού."""

        while True:

            values = ['***** SCRABBLE *****', '--------------------', '1: Σκορ',
                      '2: Ρυθμίσεις', '3: Παιχνίδι', 'q: Έξοδος', '--------------------']

            print(*values, sep='\n')

            responce = str(input()).strip()

            while int(responce) not in range(1, 4) and responce != 'q':
                print("ΜΗ ΕΠΙΤΡΕΠΤΗ ΕΠΙΛΟΓΗ, ΕΠΙΛΕΞΕ ΞΑΝΑ")
                responce = str(input()).strip()

            if responce == '2':

                values = ['ΔΙΑΛΕΞΕ ΕΝΑΝ ΑΛΓΟΡΙΘΜΟ: ', '1: MIN', '2: MAX', '3: SMART', '4: SMART_TEACH']

                print(*values, sep='\n')

                choice = str(input()).strip()

                while int(choice) not in range(1, 5):
                    print("ΜΗ ΕΠΙΤΡΕΠΤΗ ΕΠΙΛΟΓΗ, ΕΠΙΛΕΞΕ ΞΑΝΑ")
                    choice = str(input()).strip()

                self.algorithm_chosen = self.algorithms[int(choice) - 1]
            elif responce == '1':

                try:
                    with open('game_data.json', 'r', encoding='utf-8') as json_file:
                        games_data = json.load(json_file)

                        for game in games_data:
                            print(game)

                # Code to read the file goes here
                except FileNotFoundError:
                    print("The 'game_data.json' file does not exist. Please create it or check the file path.")

            elif responce == '3':

                self.ph.letters = self.sak.get_letters(7)

                self.pc.letters = self.sak.get_letters(7)

                self.run()

            elif responce == 'q':
                self.end()

    def run(self):
        # turn == 0 -> player, turn == 1 -> computer
        turn = 0
        while True:
            if turn == 0:

                self.ph.print_general_details()

                print("ΛΕΞΗ: ", end='')

                choice = str(input()).upper().strip()

                if choice == 'p' or choice == 'P':
                    self.sak.return_letters(self.ph.letters)

                    self.ph.letters = self.sak.get_letters(7)

                    turn = 1

                    continue
                if choice == 'q':
                    self.end()
                if not self.ph.check_word_letters(choice):
                    print('Η ΛΈΞΗ ΠΕΡΙΕΧΕΙ ΧΑΡΑΚΤΉΡΕΣ ΠΟΥ ΔΕΝ ΒΡΙΣΚΟΝΤΑΙ ΣΤΗΝ ΚΑΤΟΧΗ ΣΟΥ!!')
                    continue
                if not self.sak.is_accepted_word(choice):
                    print('ΜΗ ΑΠΟΔΕΚΤΗ ΛΕΞΗ, ΠΡΟΣΠΑΘΗΣΕ ΞΑΝΑ')

                    # print('ΜΗ ΑΠΟΔΕΚΤΗ ΛΕΞΗ. ΧΑΝΕΙΣ ΤΗ ΣΕΙΡΑ ΣΟΥ')
                    #
                    # turn = 1

                    continue
                self.ph.print_word_choice_details(choice, self.sak.calculate_value(choice), self.sak)

                if self.algorithm_chosen == 'SMART_TEACH':
                    pc_choice = self.ph.algorithm_smart(self.sak)
                    print('Η ΛΕΞΗ ΜΕ ΤΗΝ ΒΕΛΤΙΣΤΗ ΑΠΟΔΟΣΗ ΕΙΝΑΙ:', pc_choice)

                self.ph.remove_letters(choice)

                self.ph.add_letters(self.sak.get_letters(len(choice)))

                if len(self.ph.letters) < 7:
                    self.end()

                turn = 1

                print('ENTER ΓΙΑ ΣΥΝΕΧΕΙΑ', '*' * 20, sep='\n')

                input()
            else:

                choice = None

                if self.algorithm_chosen == 'MIN':

                    choice = self.pc.algorithm_min(self.sak)

                elif self.algorithm_chosen == 'MAX':

                    choice = self.pc.algorithm_max(self.sak)

                else:  # SMART

                    choice = self.pc.algorithm_smart(self.sak)

                self.pc.print_general_details()

                self.pc.print_word_choice_details(choice, self.sak.calculate_value(choice), self.sak)

                self.pc.remove_letters(choice)

                self.pc.add_letters(self.sak.get_letters(len(choice)))
                if len(self.pc.letters) < 7:
                    self.end()

                turn = 0
            self.moves += 1

    def end(self):
        """Ολοκληρώνει το παιχνίδι και αποθηκεύει τα αποτελέσματα."""

        winner = self.ph.name if self.ph.score > self.pc.score else "Computer"

        print(f"Player Score: {self.ph.score}, Computer Score: {self.pc.score}")
        print("Moves played:", self.moves)

        self.file_handler.add_game(self.moves, winner, self.ph.score, self.pc.score)

        self.file_handler.write_games()

        exit()


class FileHandler:
    def __init__(self):
        try:
            with open("games.json", "r") as json_file:
                self.games = json.load(json_file)
        except FileNotFoundError:
            self.games = []

    def add_game(self, moves_played, winner, player_score, computer_score):
        game = {
            "id": str(uuid.uuid4()),
            "moves_played": moves_played,
            "winner": winner,
            "player_Score": player_score,
            "computer_Score": computer_score
        }
        self.games.append(game)

    def write_games(self):
        try:
            with open("games.json", "w") as json_file:
                json.dump(self.games, json_file, indent=4)
        except FileNotFoundError:
            print("File not found")
