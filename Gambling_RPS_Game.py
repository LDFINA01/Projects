import random
from getpass import getpass
if __name__ == '__main__':
    # this creates the function that will decide on which player wins the point
    # Choice 1 = player 1 and vise versa with Choice 2
    def determine_winner(RPS1, RPS2):
    # this is if the players choose the same thing
    #this is the statment where its a draw so neither of them win the point
        if RPS1 == RPS2:
            return "draw"
    # this is part of the if statement that actually checks who wins for this
    # instance if one of these is true player 1 wins
        elif (RPS1 == "rock" and RPS2 == "scissors") or (RPS1 == "paper" and RPS2 == "rock") or (RPS1 == "scissors" and RPS2 == "paper"):
            return "player1"
        # if above is not true then play 2 wins
        else:
            return "player2"
    # startup message that just tells the users how to play the game
    print("Welcome to Rock Paper Scissors Gamble ")
    print("How to play:")
    print("1: Each player will choose countries to gamble in each round.")
    print("2: Players will then play Rock Paper Scissors to determine the winner of the round.")
    print("*Rock beats Scissors, Paper beats Rock, Scissors beats Paper*")
    print("3: The winner will receive the gambled countries.")
    print("4: The game consists of 5 rounds.")
    print()
    # This dictionary contains player 2's countries as keys. The corresponding values are the surface area (in km squared)
    # of each country
    player2countries = dict({"Russia": 16378410, "China": 9326410, "India": 2973190, "Argentina": 2736690,
                             "Kazakhstan": 2699700, "Algeria": 2381741, "Saudi Arabia": 2149690, "Mexico": 1943945,
                             "Libya": 1759540,
                             "Mongolia": 1553556, "Peru": 1279996, "Niger": 1266700, "Mali": 1220190,
                             "Colombia": 1038700, "Bolivia": 1083301,
                             "Mauritania": 1025520, "Nigeria": 910768, "Pakistan": 856690, "Turkey": 769632,
                             "Zambia": 743398,
                             "Afghanistan": 652867, "France": 640427, "Central African Republic": 622984,
                             "Ukraine": 579300, "Botswana": 566730,
                             "Thailand": 510890, "Turkmenistan": 469930, "Papua New Guinea": 452860,
                             "Uzbekistan": 425400, "Iraq": 438317,
                             "Zimbabwe": 386847, "Japan": 364546, "Republic of the Congo": 341500, "Malaysia": 329613,
                             "Ivory Coast": 318003,
                             "Oman": 309500, "Ecuador": 256369, "Burkina Faso": 273602, "Guinea": 245717,
                             "United Kingdom": 241930,
                             "Uganda": 197100, "Laos": 230800, "Belarus": 202900, "Senegal": 192530, "Syria": 183630,
                             "Uruguay": 175015,
                             "Tunisia": 155360, "Bangladesh": 148460, "Eritrea": 125000, "North Korea": 120538,
                             "Honduras": 111890})
    # This is the same as the above, but for player 1
    player1countries = dict({"USA": 9147593, "Australia": 7633565, "Canada": 9093507, "Brazil": 8460415,
                             "Democratic Republic of the Congo": 2267048, "Denmark (with Greenland)": 2220072,
                             "Indonesia": 1811569,
                             "Sudan": 1731671, "Iran": 1648195, "Chad": 1259200, "Angola": 1246700,
                             "South Africa": 1221037, "Ethiopia": 1096630,
                             "Egypt": 995450, "Tanzania": 885800, "Venezuela": 882050, "Namibia": 823290,
                             "Mozambique": 786380,
                             "Chile": 743812, "Myanmar": 653508, "South Sudan": 644329, "Somalia": 627337,
                             "Madagascar": 581540,
                             "Kenya": 569140, "Yemen": 527968, "Spain": 498980, "Cameroon": 472710, "Sweden": 407284,
                             "Morocco": 446300,
                             "Paraguay": 397302, "Norway": 365957, "Germany": 348672, "Finland": 303816,
                             "Vietnam": 310070, "Poland": 311888,
                             "Italy": 294140, "Philippines": 298170, "New Zealand": 262443, "Gabon": 257667,
                             "Romania": 231291, "Ghana": 227533,
                             "Guyana": 196849, "Kyrgyzstan": 191801, "Cambodia": 176515, "Suriname": 156000,
                             "Tajikistan": 141510,
                             "Nepal": 143686, "Greece": 130647, "Nicaragua": 119990, "Benin": 114305})
    # Tis is a variable for the players' scores. The goal is for it to increase or stay the same
    # per round depending on the outcome. At the end, the players will find out who won the most
    player1_score = 0
    player2_score = 0
    # These values will be used later in the code. They must be in the outermost portion of the code
    # because they will need to be used within various portions of the code (with different indentations)
    frst = 0
    scnd = 0
    # Loop for the rounds that will execute 5 times, plus there's a little statement that tells
    # the user what round is (a few lines down)
    for rnd_num in range(1, 6):
        # It is important later in the game that Player 1 and Player 2 each go first at different times
        # This keeps things fair, because players can gamble a different amount of countries if they go
        # second. This random number makes sure that each player gets a chance to go first, randomly
        whogoesfirst = random.randint(0,1)
        # These three numbers will make it so that whoever goes second will have the chance to gamble an extra country
        second_numb = 0
        extra_numbs = 0
        base_number = 0
        # These two dictionaries will hold the countries that each player gambles. Think of it like pushing
        # your chips across the table, making them into a separate pile. This is kind of like that
        player1hold = dict()
        player2hold = dict()
        # This prints what round it is
        print("Round", rnd_num)
        # For the keys (countries) to be printed cleanly, they have to be converted to a list
        list_convert = []
        # For them to be printed randomly, which makes sure that the user doesn't notice a size pattern
        # that list has to be made into a set
        set_convert = {}
        # This takes the keys and turns them into a list (for printing)
        for k, v in player1countries.items():
            list_convert.append(k)
        # this makes the list into a set
        set_convert = set(list_convert)
    # if the random number is zero, then Player 1 goes first
        if(whogoesfirst == 0):
    # This prints out what countries Player 1 has (in random order)
            print("Player 1 countries:", set_convert)
    # This loop will execute until the player is done gambling countries
            while True:
    # checks when P1 enters done to end
                x = input("Player 1, enter a country that you want to gamble (enter 'done' when finished): ")
                if x == "done":
                    break
                i = 0
                extrascore = 0
                # Bellow is the code for if the player chooses to gamble "Benin". Since Benin is one of Player 1's smallest
                # countries, this is less of a gamble. As such, the player has to work to be able to make this bet. They have to
                # answer some questions about the country
                if x == "Benin":
                    print("Player 1, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer. Get two out of the three right, and you can gamble the country.")
                    Ben1 = input("Which continent is Benin located in? a: Asia, b: Europe, c: Africa  ")
                    # If the answer is correct, then the player only needs to get one more right
                    # If ay any point in this if/else chain the country is not successfully gambled, then all that happens is that the loop
                    # is not "continued" through. If it is not continued, then the code proceeds to add the country to the "hold" list
                    if Ben1 == 'c':
                        Ben2 = input("Nice! Now, what are the colors of Benin's flag? a: Red, white, and blue, b: Green and red, c: Green, yellow and red  ")
                        # If they get the second one right, then they have succeeded.
                        if(Ben2 == 'c'):
                            print("Great job! Benin has been successfully gambled.")
                        # Otherwise, they have to get the third question right.
                        else:
                            Ben3 = input("Well, You still have a chance. What is Benin's official language? a: French, b: Yoruba, c: English  ")
                            if(Ben3 == 'a'):
                                print("Great job! Benin has been successfully gambled.")
                            # If they were wrong, then they only got one question right, and so they failed to gamble Benin
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Ben2 = input("Incorrect. Hopefully you get this one right. What are the colors of Benin's flag? a: Red, white, and blue, b: Green and red, c: Green, yellow and red  ")
                        if(Ben2 == 'c'):
                            Ben3 = input("Nice! Now, think hard. What is Benin's official language? a: French, b: Yoruba, c: English  ")
                            if(Ben3 == 'a'):
                                print("Great job! Benin has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                # The same principles hold true for this code (and all of the similar if/else chains below) as they do for the "Benin" code above
                if x == "Nicaragua":
                    print("Player 1, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Nic1 = input("What countries border Nicaragua? a: Mexico and Guatemala, b: Costa Rica and Honduras, c: Costa Rica and Panama  ")
                    if Nic1 == 'b':
                        Nic2 = input("Nice! Now, what are the main colors of Benin's flag? a: Blue and white, b: Green and white, c: Green, yellow and red  ")
                        if(Nic2 == 'a'):
                            print("Great job! Nicaragua has been successfully gambled.")
                        else:
                            Nic3 = input("Well, You still have a chance. What body of water lies to the east of Nicaragua? a: The Caspian Sea, b: The Caribbean Sea, c: The Gulf of Mexico  ")
                            if(Nic3 == 'b'):
                                print("Great job! Nicaragua has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Nic2 = input("Incorrect. Hopefully you get this one right. What are the main colors of Benin's flag? a: Blue and white, b: Green and white, c: Green, yellow and red  ")
                        if(Nic2 == 'a'):
                            Ben3 = input("Nice! Now, think hard. What body of water lies to the east of Nicaragua? a: The Caspian Sea, b: The Caribbean Sea, c: The Gulf of Mexico  ")
                            if(Ben3 == 'b'):
                                print("Great job! Nicaragua has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                # This code works the same as the above blocks
                if x == "Greece":
                    print("Player 1, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Gree1 = input("What empire has Greece NOT been a part of? a: Ottoman, b: Byzantine, c: Carolingian:  ")
                    if Gree1 == 'c':
                        Gree2 = input("Nice! Now, which Greek philosopher was the founder of Stoicism? a: Diogenes of Sinope, b: Socrates, c: Zeno of Citium  ")
                        if(Gree2 == 'c'):
                            print("Great job! Greece has been successfully gambled.")
                        else:
                            Gree3 = input("Well, You still have a chance. What seas lay to the west and east of Greece, respectively? a: Ionian Sea and Aegean Sea, b: Ionean Sea and Adriatic Sea, c: Aegean Sea and Ionian sea  ")
                            if(Gree3 == 'a'):
                                print("Great job! Greece has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Gree2 = input("Incorrect. Hopefully you get this one right. Which Greek philosopher was the founder of Stoicism? a: Diogenes of Sinope, b: Socrates, c: Zeno of Citium  ")
                        if(Gree2 == 'c'):
                            Gree3 = input("Nice! Now, think hard. What seas lay to the west and east of Greece, respectively? a: Ionian Sea and Aegean Sea, b: Ionean Sea and Adriatic Sea, c: Aegean Sea and Ionian sea  ")
                            if(Gree3 == 'a'):
                                print("Great job! Greece has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                # This code works the same as the above blocks
                if x == "Nepal":
                    print("Player 1, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Nep1 = input("What religion was founded by a person from Nepal? a: Buddhism, b: Hinduism, c: Zoroastrianism  ")
                    if Nep1 == 'a':
                        Nep2 = input("Nice! Now, what is the primary religion of modern day Nepal? a: Buddhism, b: Hinduism, c: Christianity  ")
                        if(Nep2 == 'b'):
                            print("Great job! Nepal has been successfully gambled.")
                        else:
                            Nep3 = input("Well, you still have a chance. Which of these three countries does Nepal border? a. China, b. Bhutan, c. Pakistan  ")
                            if(Nep3 == 'a'):
                                print("Great job! Nepal has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Nep2 = input("Incorrect. Hopefully you get this one right. what is the primary religion of modern day Nepal? a: Buddhism, b: Hinduism, c: Christianity  ")
                        if(Nep2 == 'b'):
                            Nep3 = input("Nice! Now, think hard. Which of these three countries does Nepal border? a. China, b. Bhutan, c. Pakistan  ")
                            if(Nep3 == 'a'):
                                print("Great job! Nepal has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                # This code works the same as the above blocks
                if x == "Tajikistan":
                    print("Player 1, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Taj1 = input("Which of these other '-istan' countries is actually a real country? a. Turkistan, b. Kyrgyzstan, c. Dardistan  ")
                    if Taj1 == 'b':
                        Taj2 = input("Nice! Now, what language family does Tajik, one of Tajikistan's official languages, belong to? a. Turkish, b. Indo-European, c. Sino-Tibetan  ")
                        if(Taj2 == 'b'):
                            print("Great job! Tajikistan has been successfully gambled.")
                        else:
                            Taj3 = input("Well, you still have a chance. Besides Tajik, what is the official language of Tajikistan? a. Russian, b. English, c. Arabic  ")
                            if(Taj3 == 'a'):
                                print("Great job! Tajikistan has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Taj2 = input("Incorrect. Hopefully you get this one right. What language family does Tajik, one of Tajikistan's official languages, belong to? a. Turkish, b. Indo-European, c. Sino-Tibetan  ")
                        if(Taj2 == 'b'):
                            Taj3 = input("Nice! Now, think hard. Besides Tajik, what is the official language of Tajikistan? a. Russian, b. English, c. Arabic  ")
                            if(Taj3 == 'a'):
                                print("Great job! Tajikistan has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                # This loop searches for a key that matches the player's country input. If it is found, then
                # the country and its value are added to a "hold" list. They need to be put into a separate list
                # so that they can be handed over to the other player if this player loses the rock, paper, scissors
                # Ruscancel means that Russia cannot be put into the "hold" list. If it is true, then that means that
                # the player failed the quiz below. That quiz is inside the loop because, unlike the other countries,
                # we want to make it so that every player, whether they originally had the country or gained it in a
                # gamble, will have to answer questions in order to gamble it. That is simply because of Russia's size.
                Ruscancel = False
                for k, v in player1countries.items():
                    if k == x:
                        if x == "Russia":
                            print(
                                "Whoah, that's a big country! The type of country you don't just give away too easily. If you want to gamble it, you'll first have to answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                            Rus1 = input(
                                "What is the name of the alphabet used to write Russian? a. Russian Alphabet, b. Cyrillic Alphabet, c. Greek Alphabet  ")
                            if Rus1 == 'b':
                                Rus2 = input(
                                    "Nice! Now, during the Cold War, which of the three 'worlds' was Russia proclaimed to belong to? a. First World, b. Second World, c. Third World  ")
                                if (Rus2 == 'b'):
                                    print("Great job! Russia has been successfully gambled.")
                                else:
                                    Rus3 = input(
                                        "Well, you still have a chance. Which of these three Russian authors wrote Anna Karenina? a. Alexander Pushkin, b. Fyodor Dostoevsky, c. Leo Tolstoy  ")
                                    if (Rus3 == 'c'):
                                        print("Great job! Russia has been successfully gambled.")
                                    else:
                                        print("Incorrect. Please choose a different country to gamble.")
                                        Ruscancel = True
                                        continue
                            else:
                                Rus2 = input(
                                    "Incorrect. Hopefully you get this one right. What are the colors of Tunisia's flag? a. Red and Green, b. Red and Yellow, c. Red and white  ")
                                if (Rus2 == 'b'):
                                    Rus3 = input(
                                        "Nice! Now, think hard. Which of these three Russian authors wrote Anna Karenina? a. Alexander Pushkin, b. Fyodor Dostoevsky, c. Leo Tolstoy  ")
                                    if (Rus3 == 'c'):
                                        print("Great job! Russia has been successfully gambled.")
                                    else:
                                        print("Incorrect. Please choose a different country to gamble.")
                                        Ruscancel = True
                                        continue
                                else:
                                    print("Incorrect. Please choose a different country to gamble.")
                                    Ruscancel = True
                                    continue
                        player1hold.update({k: v})
                        i = i + 1
                        base_number = base_number + 1
                # This loop does the opposite. It takes the key and corresponding value out of the main list, since we
                # don't want duplicates of the same country
                if Ruscancel == False:
                    for k, v in player1countries.items():
                        if x == k:
                            player1countries.pop(k)
                            # If the country is found, then the loop breaks, since the loop no longer needs to execute
                            break
    # For the keys (countries) to be printed cleanly, they have to be converted to a list
            list_convert = []
    # For them to be printed randomly, which makes sure that the user doesn't notice a size pattern
    # that list has to be made into a set
            set_convert = {}
            for k, v in player2countries.items():
                list_convert.append(k)
            set_convert = set(list_convert)

    # This prints the keys from Player 2's dictionary
            print("Player 2 countries:", set_convert)
            counter = 0
# All of this code below is mostly the same as that in the above while loop, the only
# difference being that it is for Player 2. Where differences exist, they are noted
            # For example, this loop's conditions are slightly different. The loop breaks when the player
            # has entered one more country than the first player has. This puts the player at a possible advantage
            # (as we will see later), and a fairly obvious potential disadvantage
            while counter < base_number + 1:
                # This is a failsafe, making extra sure that the code breaks when it ought to
                if extra_numbs == 1:
                    break
                print("Player 2, enter", base_number, "countries (enter 'done' when the number is met)")
                z = input("Or, if you want to take a bigger risk, gamble one extra country: ")
                # This makes sure that the player enters at least as many countries as the first player did
                # If they don't want to add an extra one, then they can end the loop
                if z == "done" and counter == base_number:
                    break
                i = 0
                if z == "Honduras":
                    print("Player 2, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Hon1 = input("Which form of Christianity is dominant in Honduras? a. Catholicism, b. Protestantism, c. Neither, they are both equally influential  ")
                    if Hon1 == 'c':
                        Hon2 = input("Nice! Now, which empire extended into part of Honduras? a. Aztec, b. Incan, c. Mayan  ")
                        if(Hon2 == 'c'):
                            print("Great job! Honduras has been successfully gambled.")
                        else:
                            Hon3 = input("Well, you still have a chance. How many times has Honduras qualified for the Men's World Cup? a. one, b. two, c. three  ")
                            if(Hon3 == 'c'):
                                print("Great job! Honduras has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Hon2 = input("Incorrect. Hopefully you get this one right. Which empire extended into part of Honduras? a. Aztec, b. Incan, c. Mayan  ")
                        if(Hon2 == 'c'):
                            Hon3 = input("Nice! Now, think hard. How many times has Honduras qualified for the Men's World Cup? a. one, b. two, c. three  ")
                            if(Hon3 == 'c'):
                                print("Great job! Honduras has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                if z == "North Korea":
                    print("Player 2, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Nor1 = input("What is the alphabet used by North Koreans known as in North Korea? a. Hangul, b. Chosongul, c. Neither, they use a character system instead of an alphabet  ")
                    if Nor1 == 'b':
                        Nor2 = input("Nice! Now, who was the previous leader of North Korea? a. Kim Jong Un, b. Kim Il Sung, c. Kim Jong Il  ")
                        if(Nor2 == 'c'):
                            print("Great job! North Korea has been successfully gambled.")
                        else:
                            Nor3 = input("Well, you still have a chance. In what decade did North Korea and South Korea become separate states? a. 1930s, b. 1940's, c. 1950's  ")
                            if(Nor3 == 'b'):
                                print("Great job! North Korea has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Nor2 = input("Incorrect. Hopefully you get this one right. Who was the previous leader of North Korea? a. Kim Jong Un, b. Kim Il Sung, c. Kim Jong Il  ")
                        if(Nor2 == 'c'):
                            Nor3 = input("Nice! Now, think hard. In what decade did North Korea and South Korea become separate countries? a. 1930s, b. 1940's, c. 1950's  ")
                            if(Nor3 == 'b'):
                                print("Great job! North Korea has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                if z == "Eritrea":
                    print("Player 2, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Eri1 = input("What are the three main colors on the flag of Eritrea? a. Green, Blue, and Red, b. Green, Black, and Red, c. Red, White and Blue  ")
                    if Eri1 == 'a':
                        Eri2 = input("Nice! Now, which of these three countries does Eritrea border? a. Egypt, b. Nigeria, c. Djibouti  ")
                        if(Eri2 == 'c'):
                            print("Great job! Eritrea has been successfully gambled.")
                        else:
                            Eri3 = input("Well, you still have a chance. What sea does Eritrea border? a. The Mediterranean Sea, b. The Red Sea, c. The Caspian Sea  ")
                            if(Eri3 == 'b'):
                                print("Great job! Eritrea has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Eri2 = input("Incorrect. Hopefully you get this one right. Which of these three countries does Eritrea border? a. Egypt, b. Nigeria, c. Djibouti  ")
                        if(Eri2 == 'c'):
                            Eri3 = input("Nice! Now, think hard. What sea does Eritrea border? a. The Mediterranean Sea, b. The Red Sea, c. The Caspian Sea  ")
                            if(Eri3 == 'b'):
                                print("Great job! Eritrea has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                if z == "Bangladesh":
                    print("Player 2, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Ban1 = input("What is the primary religion of Bangladesh? a. Islam, b. Hinduism, c. Buddhism  ")
                    if Ban1 == 'a':
                        Ban2 = input("Nice! Now, what are the colors of Bangladesh's flag? a. Red and Green, b. Red and Yellow, c. Red, Green, and Yellow  ")
                        if(Ban2 == 'a'):
                            print("Great job! Bangladesh has been successfully gambled.")
                        else:
                            Ban3 = input("Well, you still have a chance. Which of these countries does Bangladesh border? a. Myanmar, b. Nepal, c. Bhutan  ")
                            if(Ban3 == 'a'):
                                print("Great job! Bangladesh has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Ban2 = input("Incorrect. Hopefully you get this one right. What are the colors of Bangladesh's flag? a. Red and Green, b. Red and Yellow, c. Red, Green, and Yellow  ")
                        if(Ban2 == 'a'):
                            Ban3 = input("Nice! Now, think hard. Which of these countries does Bangladesh border? a. Myanmar, b. Nepal, c. Bhutan  ")
                            if(Ban3 == 'a'):
                                print("Great job! Bangladesh has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                if z == "Tunisia":
                    print("Player 2, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Tun1 = input("What two countries does Tunisia border? a. Libya and Algeria, b. Morocco and Algeria, c. Egypt and Algeria  ")
                    if Tun1 == 'a':
                        Tun2 = input("Nice! Now, what are the colors of Tunisia's flag? a. Red and Green, b. Red and Yellow, c. Red and white  ")
                        if(Tun2 == 'c'):
                            print("Great job! Tunisia has been successfully gambled.")
                        else:
                            Tun3 = input("Well, you still have a chance. Which Islamic caliphate conquered Tunisia? a. Umayyad, b. Rashidun, c. Abbasid  ")
                            if(Tun3 == 'b'):
                                print("Great job! Tunisia has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Tun2 = input("Incorrect. Hopefully you get this one right. What are the colors of Tunisia's flag? a. Red and Green, b. Red and Yellow, c. Red and white  ")
                        if(Tun2 == 'c'):
                            Tun3 = input("Nice! Now, think hard. Which Islamic caliphate conquered Tunisia? a. Umayyad, b. Rashidun, c. Abbasid  ")
                            if(Tun3 == 'b'):
                                print("Great job! Tunisia has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue

                Ruscancel = False
                for k, v in player2countries.items():
                    if k == z:
                        # Here is a difference in player 2's code. While the rest of the countries are harder to gamble because
                        # they are too small, this one is hard to gamble because it is too big. This is the only big country with this
                        # extra measure, and that's simply because russia is so incredibly huge that it is a special case
                        if z == "Russia":
                            print(
                                "Whoah, that's a big country! The type of country you don't just give away too easily. If you want to gamble it, you'll first have to answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                            Rus1 = input(
                                "What is the name of the alphabet used to write Russian? a. Russian Alphabet, b. Cyrillic Alphabet, c. Greek Alphabet  ")
                            if Rus1 == 'b':
                                Rus2 = input(
                                    "Nice! Now, during the Cold War, which of the three 'worlds' was Russia proclaimed to belong to? a. First World, b. Second World, c. Third World  ")
                                if (Rus2 == 'b'):
                                    print("Great job! Russia has been successfully gambled.")
                                else:
                                    Rus3 = input(
                                        "Well, you still have a chance. Which of these three Russian authors wrote Anna Karenina? a. Alexander Pushkin, b. Fyodor Dostoevsky, c. Leo Tolstoy  ")
                                    if (Rus3 == 'c'):
                                        print("Great job! Russia has been successfully gambled.")
                                    else:
                                        print("Incorrect. Please choose a different country to gamble.")
                                        Ruscancel = True
                                        continue
                            else:
                                Rus2 = input(
                                    "Incorrect. Hopefully you get this one right. What are the colors of Tunisia's flag? a. Red and Green, b. Red and Yellow, c. Red and white  ")
                                if (Rus2 == 'b'):
                                    Rus3 = input(
                                        "Nice! Now, think hard. Which of these three Russian authors wrote Anna Karenina? a. Alexander Pushkin, b. Fyodor Dostoevsky, c. Leo Tolstoy  ")
                                    if (Rus3 == 'c'):
                                        print("Great job! Russia has been successfully gambled.")
                                    else:
                                        print("Incorrect. Please choose a different country to gamble.")
                                        Ruscancel = True
                                        continue
                                else:
                                    print("Incorrect. Please choose a different country to gamble.")
                                    Ruscancel = True
                                    continue
                        player2hold.update({k: v})
                        i = i + 1
                        second_numb = second_numb + 1
                        if second_numb == base_number + 1:
                            extra_numbs = extra_numbs + 1
                if Ruscancel == False:
                    for k, v in player2countries.items():
                        if z == k:
                            counter = counter + 1
                            player2countries.pop(k)
                            break





#This portion of the code is the same as that big chunk above, only flipped. The part above executes in the random number is "0"
# but this part executes if the number is "1". Above, player 1 went first, but now player 2 goes first. As we have seen, it is important
# that both are able to go first at different times, because whoever goes second is able to gamble an extra country
        else:
            # For the keys (countries) to be printed cleanly, they have to be converted to a list
            list_convert = []
            # For them to be printed randomly, which makes sure that the user doesn't notice a size pattern
            # that list has to be made into a set
            set_convert = {}
            for k, v in player2countries.items():
                list_convert.append(k)
            set_convert = set(list_convert)
            print("Player 2 countries:", set_convert)
            while True:
                z = input("Player 2, enter a country that you want to gamble (enter 'done' when finished): ")
                if z == "done":
                    break
                i = 0
                extrascore = 0
                if z == "Honduras":
                    print("Player 2, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Hon1 = input("Which form of Christianity is dominant in Honduras? a. Catholicism, b. Protestantism, c. Neither, they are both equally influential  ")
                    if Hon1 == 'c':
                        Hon2 = input("Nice! Now, which empire extended into part of Honduras? a. Aztec, b. Incan, c. Mayan  ")
                        if(Hon2 == 'c'):
                            print("Great job! Honduras has been successfully gambled.")
                        else:
                            Hon3 = input("Well, you still have a chance. How many times has Honduras qualified for the Men's World Cup? a. one, b. two, c. three  ")
                            if(Hon3 == 'c'):
                                print("Great job! Honduras has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Hon2 = input("Incorrect. Hopefully you get this one right. Which empire extended into part of Honduras? a. Aztec, b. Incan, c. Mayan  ")
                        if(Hon2 == 'c'):
                            Hon3 = input("Nice! Now, think hard. How many times has Honduras qualified for the Men's World Cup? a. one, b. two, c. three  ")
                            if(Hon3 == 'c'):
                                print("Great job! Honduras has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                if z == "North Korea":
                    print("Player 2, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Nor1 = input("What is the alphabet used by North Koreans known as in North Korea? a. Hangul, b. Chosongul, c. Neither, they use a character system instead of an alphabet  ")
                    if Nor1 == 'b':
                        Nor2 = input("Nice! Now, who was the previous leader of North Korea? a. Kim Jong Un, b. Kim Il Sung, c. Kim Jong Il  ")
                        if(Nor2 == 'c'):
                            print("Great job! North Korea has been successfully gambled.")
                        else:
                            Nor3 = input("Well, you still have a chance. In what decade did North Korea and South Korea become separate states? a. 1930s, b. 1940's, c. 1950's  ")
                            if(Nor3 == 'b'):
                                print("Great job! North Korea has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Nor2 = input("Incorrect. Hopefully you get this one right. Who was the previous leader of North Korea? a. Kim Jong Un, b. Kim Il Sung, c. Kim Jong Il  ")
                        if(Nor2 == 'c'):
                            Nor3 = input("Nice! Now, think hard. In what decade did North Korea and South Korea become separate countries? a. 1930s, b. 1940's, c. 1950's  ")
                            if(Nor3 == 'b'):
                                print("Great job! North Korea has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                if z == "Eritrea":
                    print("Player 2, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Eri1 = input("What are the three main colors on the flag of Eritrea? a. Green, Blue, and Red, b. Green, Black, and Red, c. Red, White and Blue  ")
                    if Eri1 == 'a':
                        Eri2 = input("Nice! Now, which of these three countries does Eritrea border? a. Egypt, b. Nigeria, c. Djibouti  ")
                        if(Eri2 == 'c'):
                            print("Great job! Eritrea has been successfully gambled.")
                        else:
                            Eri3 = input("Well, you still have a chance. What sea does Eritrea border? a. The Mediterranean Sea, b. The Red Sea, c. The Caspian Sea  ")
                            if(Eri3 == 'b'):
                                print("Great job! Eritrea has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Eri2 = input("Incorrect. Hopefully you get this one right. Which of these three countries does Eritrea border? a. Egypt, b. Nigeria, c. Djibouti  ")
                        if(Eri2 == 'c'):
                            Eri3 = input("Nice! Now, think hard. What sea does Eritrea border? a. The Mediterranean Sea, b. The Red Sea, c. The Caspian Sea  ")
                            if(Eri3 == 'b'):
                                print("Great job! Eritrea has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                if z == "Bangladesh":
                    print("Player 2, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Ban1 = input("What is the primary religion of Bangladesh? a. Islam, b. Hinduism, c. Buddhism  ")
                    if Ban1 == 'a':
                        Ban2 = input("Nice! Now, what are the colors of Bangladesh's flag? a. Red and Green, b. Red and Yellow, c. Red, Green, and Yellow  ")
                        if(Ban2 == 'a'):
                            print("Great job! Bangladesh has been successfully gambled.")
                        else:
                            Ban3 = input("Well, you still have a chance. Which of these countries does Bangladesh border? a. Myanmar, b. Nepal, c. Bhutan  ")
                            if(Ban3 == 'a'):
                                print("Great job! Bangladesh has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Ban2 = input("Incorrect. Hopefully you get this one right. What are the colors of Bangladesh's flag? a. Red and Green, b. Red and Yellow, c. Red, Green, and Yellow  ")
                        if(Ban2 == 'a'):
                            Ban3 = input("Nice! Now, think hard. Which of these countries does Bangladesh border? a. Myanmar, b. Nepal, c. Bhutan  ")
                            if(Ban3 == 'a'):
                                print("Great job! Bangladesh has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                if z == "Tunisia":
                    print("Player 2, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Tun1 = input("What two countries does Tunisia border? a. Libya and Algeria, b. Morocco and Algeria, c. Egypt and Algeria  ")
                    if Tun1 == 'a':
                        Tun2 = input("Nice! Now, what are the colors of Tunisia's flag? a. Red and Green, b. Red and Yellow, c. Red and white  ")
                        if(Tun2 == 'c'):
                            print("Great job! Tunisia has been successfully gambled.")
                        else:
                            Tun3 = input("Well, you still have a chance. Which Islamic caliphate conquered Tunisia? a. Umayyad, b. Rashidun, c. Abbasid  ")
                            if(Tun3 == 'b'):
                                print("Great job! Tunisia has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Tun2 = input("Incorrect. Hopefully you get this one right. What are the colors of Tunisia's flag? a. Red and Green, b. Red and Yellow, c. Red and white  ")
                        if(Tun2 == 'c'):
                            Tun3 = input("Nice! Now, think hard. Which Islamic caliphate conquered Tunisia? a. Umayyad, b. Rashidun, c. Abbasid  ")
                            if(Tun3 == 'b'):
                                print("Great job! Tunisia has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue

                Ruscancel = False
                for k, v in player2countries.items():
                    if k == z:
                        if z == "Russia":
                            print(
                                "Whoah, that's a big country! The type of country you don't just give away too easily. If you want to gamble it, you'll first have to answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                            Rus1 = input(
                                "What is the name of the alphabet used to write Russian? a. Russian Alphabet, b. Cyrillic Alphabet, c. Greek Alphabet  ")
                            if Rus1 == 'b':
                                Rus2 = input(
                                    "Nice! Now, during the Cold War, which of the three 'worlds' was Russia proclaimed to belong to? a. First World, b. Second World, c. Third World  ")
                                if (Rus2 == 'b'):
                                    print("Great job! Russia has been successfully gambled.")
                                else:
                                    Rus3 = input(
                                        "Well, you still have a chance. Which of these three Russian authors wrote Anna Karenina? a. Alexander Pushkin, b. Fyodor Dostoevsky, c. Leo Tolstoy  ")
                                    if (Rus3 == 'c'):
                                        print("Great job! Russia has been successfully gambled.")
                                    else:
                                        print("Incorrect. Please choose a different country to gamble.")
                                        Ruscancel = True
                                        continue
                            else:
                                Rus2 = input(
                                    "Incorrect. Hopefully you get this one right. What are the colors of Tunisia's flag? a. Red and Green, b. Red and Yellow, c. Red and white  ")
                                if (Rus2 == 'b'):
                                    Rus3 = input(
                                        "Nice! Now, think hard. Which of these three Russian authors wrote Anna Karenina? a. Alexander Pushkin, b. Fyodor Dostoevsky, c. Leo Tolstoy  ")
                                    if (Rus3 == 'c'):
                                        print("Great job! Russia has been successfully gambled.")
                                    else:
                                        print("Incorrect. Please choose a different country to gamble.")
                                        Ruscancel = True
                                        continue
                                else:
                                    print("Incorrect. Please choose a different country to gamble.")
                                    Ruscancel = True
                                    continue
                        player2hold.update({k: v})
                        i = i + 1
                        base_number = base_number + 1
                if Ruscancel == False:
                    for k, v in player2countries.items():
                        if z == k:
                            player2countries.pop(k)
                            break
            # For the keys (countries) to be printed cleanly, they have to be converted to a list
            list_convert = []
            # For them to be printed randomly, which makes sure that the user doesn't notice a size pattern
            # that list has to be made into a set
            set_convert = {}
            for k, v in player1countries.items():
                list_convert.append(k)
            set_convert = set(list_convert)
            print("Player 1 countries:", set_convert)
            counter = 0
            while counter < base_number + 1:
                if extra_numbs == 1:
                    break
                print("Player 1, enter", base_number, "countries  to gamble (enter 'done' when the number is met)")
                x = input("Or, if you want to take a bigger risk, gamble one extra country: ")
                if x == "done" and counter == base_number:
                    break
                i = 0
                if x == "Benin":
                    print(
                        "Player 1, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer. Get two out of the three right, and you can gamble the country.")
                    Ben1 = input("Which continent is Benin located in? a: Asia, b: Europe, c: Africa  ")
                    if Ben1 == 'c':
                        Ben2 = input(
                            "Nice! Now, what are the colors of Benin's flag? a: Red, white, and blue, b: Green and red, c: Green, yellow and red  ")
                        if (Ben2 == 'c'):
                            print("Great job! Benin has been successfully gambled.")
                        else:
                            Ben3 = input(
                                "Well, You still have a chance. What is Benin's official language? a: French, b: Yoruba, c: English  ")
                            if (Ben3 == 'a'):
                                print("Great job! Benin has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Ben2 = input(
                            "Incorrect. Hopefully you get this one right. What are the colors of Benin's flag? a: Red, white, and blue, b: Green and red, c: Green, yellow and red  ")
                        if (Ben2 == 'c'):
                            Ben3 = input(
                                "Nice! Now, think hard. What is Benin's official language? a: French, b: Yoruba, c: English  ")
                            if (Ben3 == 'a'):
                                print("Great job! Benin has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                if x == "Nicaragua":
                    print(
                        "Player 1, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Nic1 = input(
                        "What countries border Nicaragua? a: Mexico and Guatemala, b: Costa Rica and Honduras, c: Costa Rica and Panama  ")
                    if Nic1 == 'b':
                        Nic2 = input(
                            "Nice! Now, what are the main colors of Benin's flag? a: Blue and white, b: Green and white, c: Green, yellow and red  ")
                        if (Nic2 == 'a'):
                            print("Great job! Nicaragua has been successfully gambled.")
                        else:
                            Nic3 = input(
                                "Well, You still have a chance. What body of water lies to the east of Nicaragua? a: The Caspian Sea, b: The Caribbean Sea, c: The Gulf of Mexico  ")
                            if (Nic3 == 'b'):
                                print("Great job! Nicaragua has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Nic2 = input(
                            "Incorrect. Hopefully you get this one right. What are the main colors of Benin's flag? a: Blue and white, b: Green and white, c: Green, yellow and red  ")
                        if (Nic2 == 'a'):
                            Ben3 = input(
                                "Nice! Now, think hard. What body of water lies to the east of Nicaragua? a: The Caspian Sea, b: The Caribbean Sea, c: The Gulf of Mexico  ")
                            if (Ben3 == 'b'):
                                print("Great job! Nicaragua has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                if x == "Greece":
                    print(
                        "Player 1, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Gree1 = input(
                        "What empire has Greece NOT been a part of? a: Ottoman, b: Byzantine, c: Carolingian:  ")
                    if Gree1 == 'c':
                        Gree2 = input(
                            "Nice! Now, which Greek philosopher was the founder of Stoicism? a: Diogenes of Sinope, b: Socrates, c: Zeno of Citium  ")
                        if (Gree2 == 'c'):
                            print("Great job! Greece has been successfully gambled.")
                        else:
                            Gree3 = input(
                                "Well, You still have a chance. What seas lay to the west and east of Greece, respectively? a: Ionian Sea and Aegean Sea, b: Ionean Sea and Adriatic Sea, c: Aegean Sea and Ionian sea  ")
                            if (Gree3 == 'a'):
                                print("Great job! Greece has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Gree2 = input(
                            "Incorrect. Hopefully you get this one right. Which Greek philosopher was the founder of Stoicism? a: Diogenes of Sinope, b: Socrates, c: Zeno of Citium  ")
                        if (Gree2 == 'c'):
                            Gree3 = input(
                                "Nice! Now, think hard. What seas lay to the west and east of Greece, respectively? a: Ionian Sea and Aegean Sea, b: Ionean Sea and Adriatic Sea, c: Aegean Sea and Ionian sea  ")
                            if (Gree3 == 'a'):
                                print("Great job! Greece has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                if x == "Nepal":
                    print(
                        "Player 1, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Nep1 = input(
                        "What religion was founded by a person from Nepal? a: Buddhism, b: Hinduism, c: Zoroastrianism  ")
                    if Nep1 == 'a':
                        Nep2 = input(
                            "Nice! Now, what is the primary religion of modern day Nepal? a: Buddhism, b: Hinduism, c: Christianity  ")
                        if (Nep2 == 'b'):
                            print("Great job! Nepal has been successfully gambled.")
                        else:
                            Nep3 = input(
                                "Well, you still have a chance. Which of these three countries does Nepal border? a. China, b. Bhutan, c. Pakistan  ")
                            if (Nep3 == 'a'):
                                print("Great job! Nepal has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Nep2 = input(
                            "Incorrect. Hopefully you get this one right. what is the primary religion of modern day Nepal? a: Buddhism, b: Hinduism, c: Christianity  ")
                        if (Nep2 == 'b'):
                            Nep3 = input(
                                "Nice! Now, think hard. Which of these three countries does Nepal border? a. China, b. Bhutan, c. Pakistan  ")
                            if (Nep3 == 'a'):
                                print("Great job! Nepal has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                if x == "Tajikistan":
                    print(
                        "Player 1, to gamble this country you must answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                    Taj1 = input(
                        "Which of these other '-istan' countries is actually a real country? a. Turkistan, b. Kyrgyzstan, c. Dardistan  ")
                    if Taj1 == 'b':
                        Taj2 = input(
                            "Nice! Now, what language family does Tajik, one of Tajikistan's official languages, belong to? a. Turkish, b. Indo-European, c. Sino-Tibetan  ")
                        if (Taj2 == 'b'):
                            print("Great job! Tajikistan has been successfully gambled.")
                        else:
                            Taj3 = input(
                                "Well, you still have a chance. Besides Tajik, what is the official language of Tajikistan? a. Russian, b. English, c. Arabic  ")
                            if (Taj3 == 'a'):
                                print("Great job! Tajikistan has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                    else:
                        Taj2 = input(
                            "Incorrect. Hopefully you get this one right. What language family does Tajik, one of Tajikistan's official languages, belong to? a. Turkish, b. Indo-European, c. Sino-Tibetan  ")
                        if (Taj2 == 'b'):
                            Taj3 = input(
                                "Nice! Now, think hard. Besides Tajik, what is the official language of Tajikistan? a. Russian, b. English, c. Arabic  ")
                            if (Taj3 == 'a'):
                                print("Great job! Tajikistan has been successfully gambled.")
                            else:
                                print("Incorrect. Please choose a different country to gamble.")
                                continue
                        else:
                            print("Incorrect. Please choose a different country to gamble.")
                            continue
                Ruscancel = False
                for k, v in player1countries.items():
                    if k == x:
                        if x == "Russia":
                            print(
                                "Whoah, that's a big country! The type of country you don't just give away too easily. If you want to gamble it, you'll first have to answer a few questions about it. Enter 'a', 'b', or 'c' to answer.")
                            Rus1 = input(
                                "What is the name of the alphabet used to write Russian? a. Russian Alphabet, b. Cyrillic Alphabet, c. Greek Alphabet  ")
                            if Rus1 == 'b':
                                Rus2 = input(
                                    "Nice! Now, during the Cold War, which of the three 'worlds' was Russia proclaimed to belong to? a. First World, b. Second World, c. Third World  ")
                                if (Rus2 == 'b'):
                                    print("Great job! Russia has been successfully gambled.")
                                else:
                                    Rus3 = input(
                                        "Well, you still have a chance. Which of these three Russian authors wrote Anna Karenina? a. Alexander Pushkin, b. Fyodor Dostoevsky, c. Leo Tolstoy  ")
                                    if (Rus3 == 'c'):
                                        print("Great job! Russia has been successfully gambled.")
                                    else:
                                        print("Incorrect. Please choose a different country to gamble.")
                                        Ruscancel = True
                                        continue
                            else:
                                Rus2 = input(
                                    "Incorrect. Hopefully you get this one right. What are the colors of Tunisia's flag? a. Red and Green, b. Red and Yellow, c. Red and white  ")
                                if (Rus2 == 'b'):
                                    Rus3 = input(
                                        "Nice! Now, think hard. Which of these three Russian authors wrote Anna Karenina? a. Alexander Pushkin, b. Fyodor Dostoevsky, c. Leo Tolstoy  ")
                                    if (Rus3 == 'c'):
                                        print("Great job! Russia has been successfully gambled.")
                                    else:
                                        print("Incorrect. Please choose a different country to gamble.")
                                        Ruscancel = True
                                        continue
                                else:
                                    print("Incorrect. Please choose a different country to gamble.")
                                    Ruscancel = True
                                    continue
                        player1hold.update({k: v})
                        i = i + 1
                        second_numb = second_numb + 1
                        if second_numb == base_number + 1:
                            extra_numbs = extra_numbs + 1
                if Ruscancel == False:
                    for k, v in player1countries.items():
                        if x == k:
                            player1countries.pop(k)
                            counter = counter + 1
                            break


# This below section is a way to give the game some variation. In certain rounds, the player who has lost the most rounds
# (which does not necessarily mean the person with the least amount of surface area), will be able to win more easily
        if rnd_num in [3, 5] and player1_score < player2_score:
            print("Hey Player 1, here's your chance to gain a point.")
            print(" You have two options you can decide to play while Player 2 only has one.")
            print(" As long as you choose atleast one that defeats the other players choice you get the point.")
            print(" Best of luck Player 1")
            # The player with the lowest score (in this if statement that is player 1) will input two countries
            player1_RPS = [input("Player 1, to choose type your first option 'rock', 'paper', or 'scissors': "),
                           input("Player 1, to choose type your second option 'rock', 'paper', or 'scissors': ")]
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            # Now player 2 inputs only one country
            player2_RPS = input("Player 2, to choose type 'rock', 'paper', or 'scissors': ")
            # this checks both options to decide if even one of the options beats the other player
            winner = "player2" if all(determine_winner(choice, player2_RPS) == "player2" for choice in player1_RPS) else "player1"
        # this "elif" is the same as the above "if" statement, only the role of the players are reversed
        elif rnd_num in [3, 5] and player2_score < player1_score:
            print("Hey Player 2, here's your chance to gain a point.")
            print(" You have two options you can decide to play while Player 1 only has one.")
            print(" As long as you choose at least one that defeats the other players choice you get the point.")
            print(" Best of luck Player 2")
            player1_RPS = input("Player 1, to choose type 'rock', 'paper', or 'scissors': ")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            player2_RPS = [input("Player 2, to choose type your first option 'rock', 'paper', or 'scissors': "),
                            input("Player 2, to choose type your second option 'rock', 'paper', or 'scissors': ")]
            winner = "player1" if all(determine_winner(player1_RPS, choice) == "player1" for choice in player2_RPS) else "player2"
# this is if the score is even, so it just continues like normal
        else:
            player1_RPS = ""
            # This while loop is just an error-handling method. That way, if somebody mis-types, they will have
            # a chance to re-enter, because the loop won't end until they type a correct option
            while True:
                player1_RPS = input("Player 1, to choose type 'rock', 'paper', or 'scissors': ")
                if player1_RPS == "rock" or player1_RPS == "paper" or player1_RPS == "scissors":
                    break
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            print("********************************************************************************")
            player2_RPS = ""
            # The same holds true here as above. If the player mistypes something, then they will have to reenter
            # until they type correctly
            while True:
                player2_RPS = input("Player 2, to choose type 'rock', 'paper', or 'scissors': ")
                if player2_RPS == "rock" or player2_RPS == "paper" or player2_RPS == "scissors":
                    break
            winner = determine_winner(player1_RPS, player2_RPS)

        # This adds to the total round score. This score calculates how many rounds a person has won
        if winner == "player1":
            player1_score += 1
        elif winner == "player2":
            player2_score += 1

# this is if P1 wins
        if winner == "player1" and whogoesfirst == 1:
# if P1 won the variable that was made previously will have one point added to it per round win
# These values will later store both the key and value that are Player 2's last bid
            final_countrynumb = None
            final_country = None
            matching_number = 0
            if second_numb > base_number:
                for k, v in player1hold.items():
                    final_countrynumb = v
                    final_country = k
                print("Looks like Player 1's bid payed off. Now player 2 must match their bid by handing over a country")
                print("(or countries) that is at least 10000 fewer square km than", final_country)
# Normally we wouldn't want to give away a country's surface area, but in this case it would be mean not to
                print(final_country, final_countrynumb)
                lowest_poss_numb = final_countrynumb - 100000
                while matching_number < lowest_poss_numb:
                    if matching_number >= lowest_poss_numb:
                        break
                    matching_country = input("Player 2, please enter a country: ")
                    for k, v in player2countries.items():
                        if k == matching_country:
                            # This will eventually mean that the country that the player entered will be put into the other player's dictionary
                            player2hold.update({k: v})
                            # With every value, the number will go up, so that every time the player
                            # enters a country they are closer to meeting the requirement
                            matching_number = matching_number + v
# this section adds the countries to player ones list of countries they can gamble
            player1countries.update(player1hold)
            player1countries.update(player2hold)
#this is if P2 wins and player 1 went first
        elif winner == "player2" and whogoesfirst == 0:
# These values will later store both the key and value that are Player 2's last bid
            final_countrynumb = None
            final_country = None
            matching_number = 0
# This checks if Player 1 gambled an extra country
            if second_numb > base_number:
# This loop retrieves the last country that Player 1 entered (and its surface area), setting them equal to two values
                for k, v in player2hold.items():
                    final_countrynumb = v
                    final_country = k
                print("Looks like Player 2's bid payed off. Now player 1 must match their bid by handing over a country")
                print("(or countries) that is at least 10000 fewer square km than", final_country)
# Normally we don't want to give away a country's surface area, but in this case it would be mean not to
                print(final_country, final_countrynumb)
# This sets the value that the player must meet. They have to enter a key (or keys) whose value is equal to or greater than this number
                lowest_poss_numb = final_countrynumb - 100000
                while matching_number < lowest_poss_numb:
# If the player has entered the right amount of keys with the right amount of surface area, the loop ceases
                    if matching_number >= lowest_poss_numb:
                        break
                    matching_country = input("Player 1, please enter a country: ")
                    for k, v in player1countries.items():
                        if k == matching_country:
                            player1hold.update({k: v})
                            matching_number = matching_number + v
            player2countries.update(player2hold)
            player2countries.update(player1hold)
# This is for if neither player won the round
        elif winner == "draw":
            player2countries.update(player2hold)
            player1countries.update(player1hold)
# this is if P2 wins and went first
        elif winner == "player2" and whogoesfirst == 1:
            player2countries.update(player2hold)
            player2countries.update(player1hold)
# This is if player 1 wins and went first
        elif winner == "player1" and whogoesfirst == 0:
            player1countries.update(player2hold)
            player1countries.update(player1hold)
## this prints out the round and the current scores of both of the players after the round is over
        frst = sum(player1countries.values())
        scnd = sum(player2countries.values())
        print(" Round", rnd_num, "Result")
        print(" Player 1 controls this many square kilometers:", frst)
        print(" Player 2 controls this many square kilometers:", scnd)
        print(" Player 1 has won", player1_score, "rounds")
        print(" Player 2 has won", player2_score, "rounds")
        print()
# this is just where the game end statement shows up after 5 rounds
# it prints the final scores and then it also calls for the lists of each player to be displayed that way the players can see who had the most countries at the end of the 5 rounds.
    print("Game Over ")
    print(" Final scores:")
    print(" Player 1 score:", player1_score)
    print(" Player 2 score:", player2_score)
    print(" Player 1 countries:", player1countries)
    print(" Player 2 countries:", player2countries)
    print(" Player 1 controls", frst, "km of the globe's land area")
    print(" Player 2 controls", scnd, "km of the globe's land area")
    if frst > scnd:
        print(" Winner: Player 1")
    else:
        print(" Winner: Player 2")