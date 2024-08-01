from typing import NamedTuple, List, Tuple
from itertools import combinations
from collections import Counter
import re 

    
ranks = [str(x) for x in range(2, 11)] + list('JQKA')
suits = ['♠', '♦', '♥', '♣']

class Card(NamedTuple):
    rank: str
    suit: str

    def __lt__(self, other): 
        return ranks.index(self.rank) < ranks.index(other.rank)

class Deck:

    #cards = [Card(rank, suit) for suit in suits for rank in Deck.ranks]
        
    """
    def card_pos(self, card: Card) -> int:
        return self._cards.index(card)
    """
    def is_straight_flush(hand: List[Card], rank_counts):
        res1, cards =  Deck.is_straight(hand, rank_counts)
        res2, cards2 = Deck.is_flush(hand, rank_counts)
        return res1 and res2, []
    
    def is_four_of_a_kind(hand: List[Card], rank_counts):
        for k, v in rank_counts.items():
            if v == 4: return True, [k]
        return False, []
        
    def is_full_house(hand: List[Card], rank_counts) -> bool:
        trips = False
        pair = False
        card_returns = [0,0]
        for k, v in rank_counts.items():
            if v == 3:
                trips = True
                card_returns[0] = k
            if v == 2:
                pair = True
                card_returns[1] = k
        
        return trips and pair, card_returns
    
    def is_flush(hand: List[Card], rank_counts) -> bool:
        return len(set([c.suit for c in hand])) == 1, []
    
    def is_straight(hand: List[Card], rank_counts) -> bool:
        sorted_hand = sorted(hand)
        rank_idx = [ranks.index(c.rank) for c in hand]
        temp = [x-1 == rank_idx[i+1] for i, x in enumerate(rank_idx) if i != 4]
        return all(x for x in temp), []
    
    def is_three_of_a_kind(hand: List[Card], rank_counts) -> bool:
        for k, v in rank_counts.items():
            if v == 3:
                return True, [k]
        return False, []
    
    def is_two_pair(hand: List[Card], rank_counts) -> bool:
        one_pair = False
        card_return = []
        for k, v in rank_counts.items():
            if v == 2 and one_pair:
                card_return.append(k)
                card_return = sorted(card_return, key = rank_sort_key, reverse = True)
                print(card_return)
                return True, card_return
            elif v == 2:
                one_pair = True
                card_return.append(k)
        return False, []
    
    def is_pair(hand: List[Card], rank_counts) -> bool:
        for k, v in rank_counts.items():
            if v == 2:
                return True, [k]
        return False, []
    
def split_card(card:str) -> Tuple[str, str]:
    if(card[:2] == '10'):
        return card[:2], card[2:]    
    else:
        return card[:1], card[1:]
    
def rank_sort_key(rank):
    return ranks.index(rank)
    
hand_evals = {
    'straight-flush': Deck.is_straight_flush, 
    'four-of-a-kind': Deck.is_four_of_a_kind,
    'full house': Deck.is_full_house, 
    'flush': Deck.is_flush,
    'straight': Deck.is_straight, 
    'three-of-a-kind': Deck.is_three_of_a_kind, 
    'two pair': Deck.is_two_pair, 
    'pair': Deck.is_pair, 
}   
    
def hand(hole_cards, community_cards):
    cards = []
    for card in hole_cards + community_cards:
        rank, suit = split_card(card)
        cards.append(Card(rank, suit))
    cards = sorted(cards, reverse = True)
    possible_hands = list(combinations(cards, 5)) 
    
    for outcome, eval in hand_evals.items(): 
        #print(outcome)
        for hand in possible_hands:
            #print(hand)
            rank_counts = Counter([c.rank for c in hand])
            res, res_cards = eval(hand, rank_counts)
            
            if (res):
                print(res_cards)
                hand_order = res_cards + [card.rank for card in hand if card.rank not in res_cards]
                return outcome, [c for c in hand_order]
    
    return "nothing", [c.rank for c in possible_hands[0]] 
    return
