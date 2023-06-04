import random

class Roaster:

    def __init__(self, name, weight_class):

        self.name = name

        self.weight_class = weight_class

        self.roast_points = 0

    def battle(self, opponent):

        print(f"\n{self.name} vs {opponent.name} - Battle starts!")

        for round_num in range(1, 4):

            print(f"\nRound {round_num} - 60 Seconds!")

            if round_num == 3:

                print("Sudden Death round!!!")

            # each roaster gets to make a roast

            self_roast = input(f"{self.name}, make a roast: ")

            opp_roast = input(f"{opponent.name}, make a roast: ")

            # audience votes for the best roast

            self_votes = random.randint(0, 5)  # generate random number of votes

            opp_votes = random.randint(0, 5)

            print(f"\nAudience votes: {self.name} - {self_votes} / {opponent.name} - {opp_votes}")

            if self_votes > opp_votes:

                self.roast_points += 1

                print(f"{self.name} wins the round!")

            elif opp_votes > self_votes:

                opponent.roast_points += 1

                print(f"{opponent.name} wins the round!")

            else:

                print("It's a tie!")

        print(f"\n\nBattle Ended! Final Score: {self.name} - {self.roast_points} / {opponent.name} - {opponent.roast_points}")

        if self.roast_points > opponent.roast_points:

            self.beat(opponent)

        elif opponent.roast_points > self.roast_points:

            opponent.beat(self)

        else:

            print("No winner!!!")

    def beat(self, opponent):

        old_roastmaster = Roaster.roastmaster

        Roaster.roastmaster = self

        print(f"{self.name} beat {opponent.name} and became the new Roast Master!")

        if old_roastmaster:

            old_roastmaster.lost()

    def lost(self):

        print(f"{self.name} lost the Roast Master title!")

        Roaster.roastmaster = None

Roaster.roastmaster = None

weight_classes = {'heavyweight': 3, 'middleweight': 2, 'lightweight': 1}

roasters = [

    Roaster("John", 'heavyweight'),

    Roaster("Mike", 'middleweight'),

    Roaster("Anna", 'lightweight'),

    Roaster("Tom", 'heavyweight'),

    Roaster("Samantha", 'middleweight'),

    Roaster("Peter", 'lightweight')

]

while True:

    # pick two random roasters from different weight classes

    roaster1, roaster2 = random.sample(roasters, k=2)

    if weight_classes[roaster1.weight_class] != weight_classes[roaster2.weight_class]:

        break

# start the battle!

roaster1.battle(roaster2)

