
#include <iostream>
#include <cstdlib>
#include<ctime>
#include <stdio.h>

using namespace std;

int player1Choice, player2Choice;
int won_game = 0;
int player_health = 100;
int enemy_health = 100;

string player_choice = "hit";






int r = rand() % (16 - 10) + 10;



int i;



int WinConditions(int User, int Computer) {



    if ((User == 1) && (Computer == 3) || (User == 2) && (Computer == 1) || (User == 3) && (Computer == 2)) {

        cout << "Player 1 wins!" << endl;

        return 1;

    }



    else if (User == Computer) {



        cout << "It's a draw!" << endl;



        return 3;



    }



    else {



        cout << "Player 2 wins!" << endl;



        return 2;



    }



}





int main() {

    while (player_health > 0 && enemy_health > 0) {





        // Player 1 input



        std::cout << "Player 1, enter your choice (1 for rock, 2 for paper, 3 for scissors): ";



        std::cin >> player1Choice;





        // Validate Player 1 input



        while (player1Choice < 1 || player1Choice > 3) {



            std::cout << "Invalid input! Please enter 1 for rock, 2 for paper, or 3 for scissors: ";



            std::cin >> player1Choice;



        }





        // Player 2 input



        std::cout << "Player 2, enter your choice (1 for rock, 2 for paper, 3 for scissors): ";



        std::cin >> player2Choice;





        // Validate Player 2 input



        while (player2Choice < 1 || player2Choice > 3) {



            std::cout << "Invalid input! Please enter 1 for rock, 2 for paper, or 3 for scissors: ";



            std::cin >> player2Choice;



        }





        int win = WinConditions(player1Choice, player2Choice);





        if (win == 1) {



            cout << "Would you like to hit or heal : ";



            cin >> player_choice;





            if (player_choice == "hit") {



                enemy_health = enemy_health - r;



                cout << "You hit the enemy for " << r << " health points!" << endl;



                cout << "You have " << player_health << " health points" << endl;



                cout << "The enemy has " << enemy_health << " health points" << endl;



                cout << "*" << endl;



                r = rand() % (16 - 10) + 10;



            }



            if (player_choice == "heal") {



                player_health = player_health + r;



                cout << "You healed for " << r << " health points!" << endl;



                cout << "You have " << player_health << " health points" << endl;



                cout << "The enemy has " << enemy_health << " health points" << endl;



                cout << "*" << endl;



                r = rand() % (16 - 10) + 10;



            }



        }





        if (win == 2) {



            if (enemy_health >= 50) {



                player_health = player_health - r;



                cout << "You were hit for " << r << " health points" << endl;



                cout << "You have " << player_health << " health points" << endl;



                cout << "The enemy has " << enemy_health << " health points" << endl;



                cout << "*" << endl;



                r = rand() % (16 - 10) + 10;



            }



            if (enemy_health < 50) {



                enemy_health = enemy_health + r;



                cout << "The enemy healed for " << r << " health points!" << endl;



                cout << "You have " << player_health << " health points" << endl;



                cout << "The enemy has " << enemy_health << " health points" << endl;



                cout << "*" << endl;



                r = rand() % (16 - 10) + 10;



            }

        }



        if (enemy_health <= 0) {



            cout << "YOU WON!" << endl;

            won_game = 1;

            player_health = 100;

            enemy_health = 100;



        }



        if (player_health <= 0) {



            cout << "YOU LOST!" << endl;

            won_game = 2;

            player_health = 100;

            enemy_health = 100;



        }



        if (won_game == 1 || won_game == 2) {



            cout << "Play again(enter 1 for yes or  for no): ";



            cin >> i;



            if (i > 0) {

                won_game = 0;

                continue;

            }



            if (i == 0); {

                break;

            }

        }





    }

}

