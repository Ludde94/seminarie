class HighScore:

    def __init__(self):
        self.add_highscore
        self.highscores

    def highscores(self):
        with open('C:/Users/fekbl/Desktop/ProgrammeringAllmänt/Projektarbete/SCR/game/Highscores.txt', 'r') as Highscores_file:
            name = Highscores_file.readline().rstrip('\n')
            while name != '':
                count = int(Highscores_file.readline())
                print(f'{name} scored {count} points.')
                name = Highscores_file.readline().rstrip('\n')

    def add_highscore():
        pass
