# :: Throw dice a number of times and try the so-called 'Monte Carlo Method' or 'Monte Carlo sampling'.
# :: This gives a proven and widely recognized alternative for statistical calculations and may
# :: save you some brain cells :)

# to check the results, for eg. https://www.omnicalculator.com/statistics/dice

import random
# Enter: styletext('text', S.FAIL), by default color = WARNING
import style as S
from style import styletext

def read_int(string_atr, default="1"):
    try:
        print(f"{string_atr:<30s}({default} by default)")
        atr = int(input(f"{'':<31s}").strip())
    except:
        atr = default

    return int(atr)


def simulation_setup():
    print("\nRoll dice simulation to avoid statistical calculations by so-called 'Monte Carlo method'.\nFirst, choose one of the game types to throw dice:\n")


    print("\t1 -> All dice with the same side value")
    print("\t2 -> All dice values equal to 1")
    # Space to add more game options here eventually
    print('')

    game_type = read_int("Game type:",)
    dice_num = read_int("Number of dice:", "2")
    sides_num = read_int("A dice sides:", "6")
    times_num = read_int("Test repetitions:", "1_000_000")

    return game_type, dice_num, sides_num, times_num

def decimal_places_visible(number, count=0):
    multiplier = 1.0        # tady jsem měl int (floatem se to vyřešilo) a házelo mi to u 10mil pokusů 'OverflowError: int too large to convert to float', proč?
    while True:
        if number * multiplier > 1:
            return count
        multiplier *= 10
        count += 1
 
def roll(dice_num, sides_num, times_num):
    for _ in range(times_num):
        dice_rolls = []
        for _ in range(dice_num):
            dice_roll = random.randint(1, sides_num)
            dice_rolls.append(dice_roll)
        yield dice_rolls

def main():
    game_type, dice_num, sides_num, times_num = simulation_setup()
 
    print(f"\nGame type {game_type}: ", end="")
 
    success_cnt = 0
    for r in roll(dice_num, sides_num, times_num):
        
        # print(f"{r}", end="")
 
        if game_type == 1 and all([v == r[0] for v in r]):
            success_cnt += 1
            # print(" - YES", end="")
        elif game_type == 2 and all([v == 6 for v in r]):
            success_cnt += 1
            # print(" - YES", end="")
        else:
            # print(" - NO", end="")
            pass
        # print()
 
    print("Finished")
    
    result_percent = float(success_cnt) / times_num * 100
    decimals = decimal_places_visible(result_percent, 1)

    print(styletext(f"There are {success_cnt:,} ocurence(s) from {times_num:,}. "), end="")
    print(f"That corresponds to {result_percent:.{decimals}f} %.\n")

def main_(): # not in use
    game_type, dice_num, sides_num, times_num = simulation_setup()

    times_num_backup = times_num
    # get it roll
    dice_records = []
    for _ in range(times_num):
        dice_rolls = []
        for _ in range(dice_num):
            dice_roll = random.randint(1, sides_num)
            dice_rolls.append(dice_roll)
            # print(dice_rolls)
        dice_records.append(dice_rolls)
        #times_num -= 1

    # print(dice_records)
    # print(f'Game type {game_type}')
    count = 0
    print(f"\nGame type {game_type}: ", end='')

    # game_type 1:  All dice with the same side value
    if game_type == 1:
        for rolls in dice_records:
            flag = False
            for roll in rolls:
                if roll != rolls[-1]:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                count += 1

    # game_type 2: All dice values equal to 6
    if game_type == 2:
        for rolls in dice_records:
            flag = False
            for roll in rolls:
                if roll != 6:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                count += 1

    
    
    resultNum = float(count / times_num_backup)
    decimals = decimal_places_visible(resultNum)
    
    print(styletext("{:<20s}".format(f"There are {count} ocurence(s) from {times_num_backup}. ")), end='')
    print("That corresponds to {:.{dec}%}".format(resultNum, dec = decimals), end='\n\n')


if __name__ == "__main__":
    main()
