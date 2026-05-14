from itertools import combinations

def _txt_to_tab(txt_path: str) -> list[list]:
    """funkcja pomocnicza do wczytywania tablicy z pliku tekstowego

    Args:
        txt_path (str): ścieżka do pliku

    Returns:
        list[list]: tablica elementów
    """
    tab = []
    with open(txt_path, "r") as f:
        for element in f.readlines():
            row = []
            for char in element.split():
                row.append(int(char))
            tab.append(row)
    return tab



def covering(path: str) -> list[list]:
    reg = []
    comb = []
    max_el = 0
    decisions = []
    tab = _txt_to_tab(path)
    for objects in tab:
        decisions.append(objects[-1])
        max_el=len(objects[:-1])
        for i in range(1, len(objects)):
            comb.append(list(combinations(objects[0: -1], i)))

    return comb

    

if __name__ == "__main__":
    tab = covering("algorithms/tab.txt")
    [print(f"{element}\n") for element in tab]
    # print(tab)
