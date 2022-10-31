"""
project_1_lchy.py: první projekt do Engeto Online Python Akademie

author: Lucie Chytilová
email: studyroomchy@gmail.com
discord: Lucie Ch.#8282
"""

import task_template as task

title_count = 0
upper_count = 0
lower_count = 0
numeric_count = 0
sum_numeric = 0

graph_value = {}

#Vyžádá si od uživatele přihlašovací jméno a heslo
username = input("username: ").lower()
password = input("password: ")

#zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
if username not in task.USER or password != task.USER[username]:

    #pokud není registrovaný, upozorni jej a ukonči program
    print("unregistered user, terminating the program...")

#pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
else:
    print(task.SEPARATOR)
    print(f"Welcome to the app, {username}") 
    print(f"We have 3 texts to be analyzed.\n{task.SEPARATOR}")
    
    #Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS
    text_nbr = input("Enter a number btw. 1 and 3 to select: ")

    #Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,    
    #pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí
    if not text_nbr.isdigit() or not(int(text_nbr)-1 in range(len(task.TEXTS))):
        print("Your choice is not correct, terminating the program...")
    
    else:
        #pročištění vybraného textu
        select_text = task.TEXTS[int(text_nbr)-1]
        translate_table = select_text.maketrans(",-", "  ", ".")
        clear_list = select_text.translate(translate_table).split()
        print(clear_list)
        
        for word in clear_list:
            #hodnoty pro sloupcový graf
            len_word = len(word)
            if len_word in graph_value:
                graph_value[len_word] += 1
            else:
                graph_value[len_word] = 1
          
            #počet slov začínajících velkým písmenem
            if word.istitle():
                title_count += 1
            
            #počet slov psaných velkými písmeny
            elif word.isupper():
                upper_count += 1
            
            #počet slov psaných malými písmeny
            elif word.islower():
                lower_count += 1
            
            #počet čísel (ne cifer)
            #sumu všech čísel (ne cifer) v textu
            elif word.isnumeric():
                numeric_count += 1
                sum_numeric += int(word)
        
        print(task.SEPARATOR)
        
        #výpis statistik - počet slov
        print(f"There are {len(clear_list)} words in the selected text.")    
        
        #výpis ostatních statistik
        print(f"There are {title_count} titlecase words.")
        print(f"There are {upper_count} uppercase words.")
        print(f"There are {lower_count} lowercase words.")
        print(f"There are {numeric_count} numeric strings.")
        print(f"The sum of all the numbers {sum_numeric}.\n{task.SEPARATOR}")  
        
        #šířky pro sloupcový graf
        if len("LEN") > len(str(sorted(graph_value.keys()).pop())):
            max_len = len("LEN")
        else:
            max_len = len(str(sorted(graph_value.keys()).pop()))        
        
        if len("OCCURENCES") > sorted(graph_value.values()).pop():
            max_nr = len("OCCURENCES") + 2
        else:
            max_nr = sorted(graph_value.values()).pop() + 2
        
        #výpis hlavičky grafu
        print(f"{'LEN':>{max_len}}|{'OCCURENCES':^{max_nr}}|NR.\n{task.SEPARATOR}")
        
        #výpis samotného sloupcového grafu
        for key, value in sorted(graph_value.items()):
            print(f"{key:>{max_len}}|{'*'*value:<{max_nr}}|{value}")
