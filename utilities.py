def get_lines(file_type='sample', day=-1):
    '''
    Read in the lines of today's sample/input file line by line. 
    Assumes the file is in folder called 'inputs/'
    
    Parameters
    ----------
    file_type : str
        Either sample or input
    
    Returns
    -------
    list of inputs stripped of whitespace
    '''
    if day==-1:
        import datetime
        day = str(datetime.datetime.today().day).zfill(2)
    else:
        day = str(day).zfill(2)
    filename = f'inputs/{day}-{file_type}.txt'
    try:
        with open(filename,'r') as file:
            lines = [line.strip() for line in file.readlines()]
        return lines
    except:
        print(filename+' does not exist')
        return None
        
def create_empty_notebook(file):
    '''
    Helper function to batch create empty ipynb notebooks
    
    Parameters
    ----------
    file : <class '_io.TextIOWrapper'>
        This is a file object that you can write to.
        Write json to initialize a notebook.
    '''
    empty_lines = '{"cells": [],"metadata": {},"nbformat": 4,"nbformat_minor": 5}'
    try:
        file.write(empty_lines)
    except:
        print(f'{file} does not exist')
        
def batch_create_files(start=1):
    '''
    Create empty files at the beginning of the month for easy copy-pasting the day of.
    Assumes all input files will go into folder labelled 'inputs/'
    
    Parameters
    ----------
    start : int
        Which day you want to start autopopulating (in case you forgot about this function on Day 1)

    '''
    for i in range(start,26):
        day = str(i).zfill(2)
        with open(f'inputs/{day}-sample.txt','w') as file:
            pass
        with open(f'inputs/{day}-input.txt','w') as file:
            pass
        with open(f'notebooks/Day {day}-1.ipynb','w') as file:
            create_empty_notebook(file)
        with open(f'notebooks/Day {day}-2.ipynb','w') as file:
            create_empty_notebook(file)

class Tile:
    '''
    Note that AoC 2023 Day 16 is similar in terms of checking values in a matrix, but I didn't create a class.
    
    Created for AoC Day 10 (parts 1 and 2): consider location within a matrix, check values in NE, SE, SW, and NW corners
        before stepping N,E,S, or W.

    The check values are very specific to that day's challenge but the general idea could be re-used.
    '''
    def __init__(self, row, col, pipe):
        self.row = row
        self.col = col
        self.pipe = pipe
        self.N = False
        self.E = False
        self.S = False
        self.W = False
        self.is_start = False
        self.step = 0
        self.from_dir = None
        self.is_path = False
    
    Loc = namedtuple('Loc','row col pipe')
    
    def __repr__(self):
        return f'({self.row}, {self.col}, {self.pipe})'
    
    
    def check_NS(self): #  |
        if self.pipe=='|':
            if is_valid_loc(self.row-1,self.col):
                self.N = True
                return True
            if is_valid_loc(self.row+1,self.col):
                self.S = True
                return True
        return False
    
    def check_EW(self): #  -
        if self.pipe=='-':
            if is_valid_loc(self.row,self.col+1):
                self.E = True
                return True
            if is_valid_loc(self.row,self.col-1):
                self.W = True
                return True
        return False
    
    def check_NE(self): #  L
        if self.pipe=='L':
            if is_valid_loc(self.row-1,self.col):
                self.N = True
                return True
            if is_valid_loc(self.row,self.col+1):
                self.E = True
                return True
        return False
    
    def check_NW(self): #  J
        if self.pipe=='J':
            if is_valid_loc(self.row-1,self.col):
                self.N = True
                return True
            if is_valid_loc(self.row,self.col-1):
                self.W = True
                return True
        return False
    
    def check_SW(self): #  7
        if self.pipe=='7':
            if is_valid_loc(self.row+1,self.col):
                self.S = True
                return True
            if is_valid_loc(self.row,self.col-1):
                self.W = True
                return True
        return False
    
    def check_SE(self): #  F
        if self.pipe=='F':
            if is_valid_loc(self.row+1,self.col):
                self.S = True
                return True
            if is_valid_loc(self.row,self.col+1):
                self.E = True
                return True
        return False
    
    def set_start(self): #  S
        if self.pipe=='S':
            self.is_start = True
            return 1
        return 0
    
    def step_N(self):
        return (self.row-1,self.col)
    
    def step_E(self):
        return (self.row,self.col+1)
    
    def step_S(self):
        return (self.row+1,self.col)
    
    def step_W(self):
        return (self.row,self.col-1)

class Hand:
    '''
    Card playing functionality created for AoC 2023 Day 7, part 1. Some of this could be useful in future events.

    Attributes
    ----------
    hand: string of five cards (such as TQ67J, KT252, etc)
    bid: integer value 
    card_values: dictionary of cards (characters) ranked by value, with Ace high

    Methods
    -------
    get_hand_type: returns integer value, 1 (high card) through 7 (five of a kind) based on cards in the hand
    rank_hands: specific to the challenge for the day
    __eq__,__lt__,__gt__: for card-by-card comparison of hands when the values (based on type of hand) are tied
    '''
    card_values = dict(zip('23456789TJQKA',range(13)))
    
    def __init__(self, hand, bid):
        self.hand = hand
        self.num_cards = len(hand)
        self.bid = bid
        
    def __repr__(self):
        return f'{self.hand}'
    
    @classmethod
    def _resolve_conflict(cls, h1, h2):
        for i in range(h1.num_cards):
            if Hand.card_values[h1.hand[i]]>Hand.card_values[h2.hand[i]]:
                return 1
            if Hand.card_values[h1.hand[i]]<Hand.card_values[h2.hand[i]]:
                return -1
        return 0
    
    def __eq__(self, other):
        if self._resolve_conflict(self, other)==0:
            return True
        return False
    
    def __lt__(self, other):
        if self._resolve_conflict(self, other)==-1:
            return True
        return False
    
    def __gt__(self, other):
        if self._resolve_conflict(self, other)==1:
            return True
        return False
    
    @classmethod
    def _get_max_count(cls, h):
        counter = Counter(h.hand)
        return max(counter.items(),
                   key=lambda item: item[1]
                  )[1]
    
    def _is_5_kind(self):
        if len(set(self.hand))==1:
            return True
        return False
    
    def _is_4_kind(self):
        if (len(set(self.hand))==2)&(Hand._get_max_count(self)==4):
            return True
        return False
    
    def _is_full_house(self):
        if (len(set(self.hand))==2)&(Hand._get_max_count(self)==3):
            return True
        return False
    
    def _is_3_kind(self):
        if (len(set(self.hand))==3)&(Hand._get_max_count(self)==3):
            return True
        return False
    
    def _is_2_pair(self):
        if (len(set(self.hand))==3)&(Hand._get_max_count(self)==2):
            return True
        return False
    
    def _is_1_pair(self):
        if len(set(self.hand))==4:
            return True
        return False
    
    def _is_high_card(self):
        if len(set(self.hand))==5:
            return True
        return False
    
    def get_hand_type(self):
        if self._is_5_kind():
            return '5 of a kind'
        if self._is_4_kind():
            return '4 of a kind'
        if self._is_full_house():
            return 'full house'
        if self._is_3_kind():
            return '3 of a kind'
        if self._is_2_pair():
            return '2 pair'
        if self._is_1_pair():
            return '1 pair'
        if self._is_high_card():
            return 'high card'
        return 'no type'
    
    hand_rank = ['high card', '1 pair', '2 pair', '3 of a kind',
                 'full house', '4 of a kind', '5 of a kind'
                ]
    hand_values = dict(zip(hand_rank, range(7)))
    
    def get_hand_value(self):
        return Hand.hand_values[self.get_hand_type()]
    
    def __hash__(self):
        return hash(self.get_hand_value())
    
    @classmethod
    def rank_hands(cls, hand_list):
        sorted_hands = sorted(hand_list, 
                       key=lambda h: Hand.get_hand_value(h)
                      )
        hold_hands = list()
        final_hands = list()
        while len(sorted_hands)>0:
            current_hand = sorted_hands.pop()
            hold_hands.append(current_hand)
            # print(f'current hand {current_hand}')
            print(f'working on rank {current_hand.get_hand_value()}')
            if len(sorted_hands)>0:
                next_hand = sorted_hands[-1]
                # print(f'\tnext hand {next_hand}')
                while next_hand is not None and current_hand.get_hand_value()==next_hand.get_hand_value():
                    next_hand = sorted_hands.pop()
                    hold_hands.append(next_hand)
                    current__hand = next_hand
                    if len(sorted_hands)>0:
                        next_hand = sorted_hands[-1]
                    else:
                        next_hand = None
                        
                       # hold_hands.append(next_hand)
                       # if len(sorted_hands)>0:
                       #     current_hand = next_hand
                       #     print(f'\tcurrent hand {current_hand}')
                       #     if len(sorted_hands)>0:
                       #         next_hand = sorted_hands[-1]
                       #         print(f'\t\tnext hand {next_hand}')
                       #         print(f'len sorted hands: {len(sorted_hands)}')
            hold_hands = sorted(hold_hands)[::-1]
            # print(f'hold hands sorted: {hold_hands}')
            final_hands.extend(hold_hands)
            print(f'len final hands extended: {len(final_hands)}')
            
            hold_hands = list()
        return final_hands[::-1]
                

        