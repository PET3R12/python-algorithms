from itertools import combinations

def _txt_to_tab(txt_path: str):
    tab = []
    with open(txt_path, "r") as f:
        for element in f.readlines():
            row = []
            for char in element.split():
                row.append(int(char))
            tab.append(row)
    return tab

def covering(path: str):
    tab = _txt_to_tab(path)
    
    ilosc_wierszy = len(tab)
    ilosc_cech = len(tab[0]) - 1
    
    wszystkie_obiekty = []
    for i in range(ilosc_wierszy):
        wiersz = tab[i]
        decyzja = wiersz[-1]
        
        cechy_wiersza = []
        for j in range(ilosc_cech):
            cechy_wiersza.append((j + 1, wiersz[j]))
            
        wszystkie_obiekty.append([i + 1, cechy_wiersza, decyzja])
    do_pokrycia = []
    for i in range(1, ilosc_wierszy + 1):
        do_pokrycia.append(i)
    wyniki_do_printu = []
    rzad = 1
    while len(do_pokrycia) > 0 and rzad <= ilosc_cech:
        obiekty_w_tym_rzedzie = list(do_pokrycia)
        
        for obj_id in obiekty_w_tym_rzedzie:
            if obj_id not in do_pokrycia:
                continue

            cechy_aktualnego = []
            decyzja_aktualnego = None
            for ob in wszystkie_obiekty:
                if ob[0] == obj_id:
                    cechy_aktualnego = ob[1]
                    decyzja_aktualnego = ob[2]
                    break
            kombinacje_tymczasowe = list(combinations(cechy_aktualnego, rzad))
            unikalne_kombinacje = list(set(kombinacje_tymczasowe))
            znaleziona_regula = False
            
            for kombinacja in unikalne_kombinacje:
                sprzeczna = False
                pokryte = []                
                for ob_test in wszystkie_obiekty:
                    id_test = ob_test[0]
                    cechy_test = ob_test[1]
                    decyzja_test = ob_test[2]
                    
                    zawiera_sie = True
                    for k in kombinacja:
                        if k not in cechy_test:
                            zawiera_sie = False
                            break
                            
                    if zawiera_sie:
                        if decyzja_test != decyzja_aktualnego:
                            sprzeczna = True
                            break
                        else:
                            pokryte.append(id_test)
                            
                if sprzeczna == False:
                    znaleziona_regula = True
                    for p in pokryte:
                        if p in do_pokrycia:
                            do_pokrycia.remove(p)       
                    warunki = " ∧ ".join([f"(a{k[0]} = {k[1]})" for k in kombinacja])
                    ilosc = len(pokryte)
                    support = f"[{ilosc}]" if ilosc > 1 else ""
                    tekst = f"z o{obj_id} {warunki} -> (d = {decyzja_aktualnego}){support},"
                    wyniki_do_printu.append([rzad, tekst])
                    break
            
            if znaleziona_regula == False:
                wyniki_do_printu.append([rzad, f"z o{obj_id} brak"])

        rzad += 1
        
    return wyniki_do_printu


if __name__ == "__main__":

    #trzeba tutaj tylko zmienić ścieżkę do pliku tekstowego, bo w projekcie miałem według tej struktury
    # wyniki = covering("algorithms/tab.txt")
    aktualny_rzad = 0
    for wpis in wyniki:
        rzad_wpisu = wpis[0]
        tekst_na_ekran = wpis[1]
        
        if rzad_wpisu != aktualny_rzad:
            if aktualny_rzad > 0:
                print(f"Rząd {rzad_wpisu}:")
            aktualny_rzad = rzad_wpisu
        print(tekst_na_ekran)