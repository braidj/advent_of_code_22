shapes = {}
shapes['A'] = 'rock'
shapes['B'] = 'paper'
shapes['C'] = 'scissors'
shapes['X'] = 'rock'
shapes['Y'] = 'paper'
shapes['Z'] = 'scissors'

value = {}
value['rock'] = 1
value['paper'] = 2
value['scissors'] = 3

score = {}
score['win'] = 6
score['draw'] = 3
score['lose'] = 0

def get_result(pair):
    """
    Work out the value for a single round
    """

    if pair[0] == pair[1]: # draw
        return "draw"

    if ('rock' == pair[1] and 'scissors' in pair):
        return "win"

    if ('scissors' == pair[1] and 'paper' in pair):
        return "win"

    if ('paper' == pair[1] and 'rock' in pair):
        return "win"

    return "lose"

def get_round_total(result,shape):
    """
    Add the score of the result and the shape
    """

    result_value = score[result]
    shape_value = value[shape]
    return result_value + shape_value

def main():
    """
    Entry point
    """

    grand_total = 0
    counter = 1

    with open("./data/daytwo.dat", 'r') as f:
        data_lines = f.readlines()
    
    for line in data_lines:

        left,right = line.strip().split(" ")
        pair =[shapes[left],shapes[right]]
        print(f"{counter}) {get_result(pair)} {shapes[right]}")
        sub_total = get_round_total(get_result(pair),shapes[right])
        grand_total = grand_total + sub_total
        counter +=1

    print(grand_total)

if __name__ == "__main__":

    main()