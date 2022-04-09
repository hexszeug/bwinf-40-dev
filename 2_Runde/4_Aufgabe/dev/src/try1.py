from collections.abc import Callable

def search_xored_cards(card_pool: list, card_group_size: int) -> list:

    def combine_elements(combination_pool: list, group_size: int, recall: Callable[[list], None]):
        def combi_level(pool: list, depth: int, pre_combi: list):
            if depth == 0:
                recall(pre_combi)
                return
            for i, x in enumerate(pool):
                new_pre_combi = pre_combi[:]; new_pre_combi.append(x)
                combi_level(pool[i+1:], depth-1, new_pre_combi)
        combi_level(combination_pool, group_size, [])

    def xor_list(list: list):
        xor = 0
        for elm in list:
            xor = xor ^ elm
        return xor

    xored_cards = []
    def save_xored_cards(card_combination: list):
        xor = xor_list(card_combination[:-1])
        if xor == card_combination[-1]:
            xored_cards.append(card_combination)
    
    combine_elements(card_pool, card_group_size + 1, save_xored_cards)

    return xored_cards


with open("stapel2.txt") as f:
    cards = [int(x, 2) for x in f.readlines()[1:]]

print([[bin(y) for y in x] for x in search_xored_cards(cards, 10)])