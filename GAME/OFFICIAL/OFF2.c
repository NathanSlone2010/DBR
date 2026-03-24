#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif

double random_double(double min, double max) {
    return min + (rand() / (double)RAND_MAX) * (max - min);
}

void sleep_seconds(double seconds) {
#ifdef _WIN32
    Sleep((DWORD)(seconds * 1000));
#else
    usleep((useconds_t)(seconds * 1000000));
#endif
}

int main() {
    int cylinder_size = 8;
    double odds = 4.0 / cylinder_size;
    int days = 1;
    int count = 0;

    srand(time(NULL));

    printf("\nDragon-Breath Roulette\n");
    sleep_seconds(1); printf("Remaster of DEAD'S ROULETTE\n");
    sleep_seconds(0.5); printf(" Date of Production: 3/17/26\n");
    sleep_seconds(0.5); printf("  GitHub: NathanSlone2010\n");
    sleep_seconds(0.5); printf("   VERSION 01.00.00 [OFFICIAL RELEASE]\n");
    sleep_seconds(0.5); printf("    Rating: M for Mature\n");
    printf("!!TYPE 'S' to start or 'E' to exit!!\n");

    char con[10];
    printf("C: ");
    scanf("%9s", con);
    con[0] = toupper(con[0]);

    if (con[0] == 'S') {
        printf("LOADING");
        int num_dots = rand() % 5 + 3; // 3-7 dots
        for (int i = 0; i < num_dots; i++) {
            sleep_seconds(random_double(0.3, 1.0));
            printf(".");
            fflush(stdout);
        }
        printf("\n");
    } else if (con[0] == 'E') {
        printf("EXITTING");
        int num_dots = rand() % 5 + 3;
        for (int i = 0; i < num_dots; i++) {
            sleep_seconds(random_double(0.3, 1.0));
            printf(".");
            fflush(stdout);
        }
        printf("\n");
        exit(0);
    } else {
        printf("NOT VALID OPTION. STARTING PROGRAM ANYWAYS.\n");
    }

    while (1) {
        printf("THE ROUND RACKS...\n\n");
        sleep_seconds(1); printf("1. Shoot yourself..\n");
        sleep_seconds(1.5); printf("2. Shoot the man across the table...\n");
        sleep_seconds(2); printf("3. REVENGE....\n");

        char choice[10];
        printf(">>>");
        scanf("%9s", choice);

        int bullet = rand() % cylinder_size + 1;
        int position = rand() % cylinder_size + 1;

        if (choice[0] == '1') {
            printf("You point the shotgun at yourself\n");
            if ((rand() / (double)RAND_MAX) < odds) {
                sleep_seconds(1.5); printf("The shotgun goes off.. You slump over the table...\n");
                sleep_seconds(0.5); printf("'Rid of the body in the fire. Now!'\n");
                break;
            } else {
                count = 1;
                sleep_seconds(1); printf("A shell ejects... 'You survive for now..'\n");
            }
        } else if (choice[0] == '2') {
            sleep_seconds(0.5); printf("You point it at the man. 'Good luck out there, bro..'\n");
            if ((rand() / (double)RAND_MAX) < odds) {
                sleep_seconds(0.5); printf("HE SURVIVES.\n");
            } else {
                sleep_seconds(0.5); printf("Fuck me... Goodbye.. BANG. The rounds go off.\n");
                sleep_seconds(1.8); printf("ANOTHER OPPONENT ENTERS...\n");
            }
        } else if (choice[0] == '3') {
            sleep_seconds(1); printf("You point it at the guard...\n");
            if ((rand() / (double)RAND_MAX) < odds) {
                printf("CLICK. The shell does not fire... 'DUMB BASTARD!\n");
                break;
            } else {
                printf("BANG. The gun goes off... 'Congratulations... You and Opponent both wins.\n");
                break;
            }
        } else {
            printf("MAKE A CHOICE!\n");
        }
    }

    return 0;
}
