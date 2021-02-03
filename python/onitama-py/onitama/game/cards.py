blank =    [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
tiger =    [[0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0]]
dragon =   [[0,0,0,0,0],
            [1,0,0,0,1],
            [0,0,0,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0]]
frog =     [[0,0,0,0,0],
            [0,1,0,0,0],
            [1,0,0,0,0],
            [0,0,0,1,0],
            [0,0,0,0,0]]
rabbit =   [[0,0,0,0,0],
            [0,0,0,1,0],
            [0,0,0,0,1],
            [0,1,0,0,0],
            [0,0,0,0,0]]
crab =     [[0,0,0,0,0],
            [0,0,1,0,0],
            [1,0,0,0,1],
            [0,0,0,0,0],
            [0,0,0,0,0]]
elephant = [[0,0,0,0,0],
            [0,1,0,1,0],
            [0,1,0,1,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
goose =    [[0,0,0,0,0],
            [0,1,0,0,0], jujyut
            [0,1,0,1,0],
            [0,0,0,1,0],
            [0,0,0,0,0]]
rooster =  [[0,0,0,0,0],
            [0,0,0,1,0],
            [0,1,0,1,0],
            [0,1,0,0,0],
            [0,0,0,0,0]]
monkey =   [[0,0,0,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0]]
mantis =   [[0,0,0,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0]]
horse =    [[0,0,0,0,0],
            [0,0,1,0,0],
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0]]
ox =       [[0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,0],
            [0,0,1,0,0],
            [0,0,0,0,0]]
crane =    [[0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0]]
boar =     [[0,0,0,0,0],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
eel =      [[0,0,0,0,0],
            [0,1,0,0,0],
            [0,0,0,1,0],
            [0,1,0,0,0],
            [0,0,0,0,0]]
cobra =    [[0,0,0,0,0],
            [0,0,0,1,0],
            [0,1,0,0,0],
            [0,0,0,1,0],
            [0,0,0,0,0]]

all_cards = [tiger, dragon, frog, rabbit,
            crab, elephant, goose, rooster,
            monkey, mantis, horse, ox,
            crane, boar, eel, cobra]


def get_init_cards():
    return ([all_cards[0], all_cards[1]],
            [all_cards[2], all_cards[3]],
            [all_cards[4]])