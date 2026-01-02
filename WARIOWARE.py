# --- 1. PREPARAZIONE MEMORIA ---
memoria_golosa = [0] * 7000
print("Sexy Wario PC turning on...")

# --- 2. CARICAMENTO ROM (FIXED) ---
try:
    file_rom = open("gioco.txt", "r")
    indice = 0
    for riga in file_rom:
        # .strip() toglie spazi invisibili che fanno sbagliare il computer
        contenuto_pulito = riga.strip()
        
        # Carichiamo solo se la riga non è vuota
        if contenuto_pulito:
            numero_letto = int(contenuto_pulito)
            memoria_golosa[indice] = numero_letto
            indice = indice + 1
    file_rom.close()
    print("ROM Caricata! Ho letto", indice, "numeri.")
except Exception as e:
    print("Errore nel caricamento della ROM:", e)

# --- 3. CICLO DI VITA ---
acceso = True
while acceso == True:
    print("\n--- MENU WARIO ---")
    comando = input("Cosa facciamo? (esci / leggi / esegui): ").lower().strip()

    if comando == "esci":
        acceso = False
        print("Sexy Wario PC shutting down... Bye bye!")

    elif comando == "leggi":
        pos = int(input("Quale cassetto vuoi spiare? "))
        if pos < 7000:
            print(f"Nel cassetto {pos} c'e' il numero: {memoria_golosa[pos]}")
        else:
            print("Wario dice: Quel cassetto non esiste!")

    elif comando == "esegui":
        # LA CPU PRENDE I DATI
        dato1 = memoria_golosa[0]
        dato2 = memoria_golosa[1]
        istruzione = memoria_golosa[2]

        print(f"DEBUG: Sto usando {dato1} e {dato2} con il comando {istruzione}")

        # LA CPU DECIDE COSA FARE (Il tuo linguaggio)
        if istruzione == 10:
            risultato = dato1 + dato2
            print("RISULTATO SOMMA:", risultato)
        
        elif istruzione == 20:
            risultato = dato1 * dato2
            print("RISULTATO MOLTIPLICAZIONE:", risultato)
            
        else:
            print("CPU ERROR: Il comando", istruzione, "non esiste nel mio cervello!")

    else:
        print("Wario non capisce il comando:", comando)

