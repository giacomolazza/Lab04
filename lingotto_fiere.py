from operator import attrgetter
class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.espositori = []
        self.stand = []

        # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                campi = line.strip().split(",")
                if campi[0].startswith("ES"):
                     codice_espositore = campi[0]
                     nome_espositore = campi[1]
                     cognome_espositore = campi[2]

                     espositore = Espositori(campi[0], campi[1], campi[2])
                     self.espositori.append(espositore)
                else:
                    if campi[0].startswith("ST"):
                        if len(campi) == 4:
                            codice_stand = campi[0]
                            superficie = int(campi[1])
                            padiglione = int(campi[2])
                            prezzo_base = int(campi[3])

                            stand = Stand(codice_stand, superficie, padiglione, prezzo_base)
                            self.stand.append(stand)

                        if len(campi) == 5:

                            if campi[4].isdigit():
                                codice_stand = campi[0]
                                superficie = int(campi[1])
                                padiglione = int(campi[2])
                                prezzo_base = int(campi[3])
                                prese = int(campi[4])

                                stand_presa = StandPrese(codice_stand, superficie, padiglione, prezzo_base, prese)
                                self.stand.append(stand_presa)

                            else:
                                codice_stand = campi[0]
                                superficie = int(campi[1])
                                padiglione = int(campi[2])
                                prezzo_base = int(campi[3])
                                posizione = campi[4]

                                stand_posizione = StandPosizione(codice_stand, superficie, padiglione, prezzo_base, posizione)
                                self.stand.append(stand_posizione)
        # TODO

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        for stand in self.stand:
            if stand.codice_stand == codice_stand:
                if stand.disponibile:
                    for espositore in self.espositori:
                        if espositore.codice_espositore == codice_espositore:
                            if espositore.stand is None:
                                espositore.stand = codice_stand
                                stand.espositore = espositore
                                stand.disponibile = False
                                return
                            else:
                                raise ValueError("l'espositore ha gia uno stand")
                    raise ValueError("codice espositore non valido")
                else:
                    raise ValueError("stand occupato")
        raise ValueError("codice stand non valido")

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositori in self.espositori:
            print(espositori)
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        sort = sorted(self.stand, key=attrgetter("prezzo"))
        return sort

        # TODO
class Stand:
    def __init__(self, codice_stand, superficie, padiglione, prezzo_base):
        self.codice_stand = codice_stand
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo = prezzo_base
        self.disponibile = True
        self.espositore = None

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = "Occupato"

        return f"{self.codice_stand}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f}€ - {stato}"
class StandPrese(Stand):

    def __init__(self, codice_stand, superficie, padiglione, prezzo_base, prese):

        super().__init__(codice_stand, superficie, padiglione, prezzo_base)

        self.prese = prese
        self.prezzo = prezzo_base * (1 + 0.07 * prese)

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = "Occupato"

        return f"{self.codice_stand}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f}€ - n prese {self.prese} - {stato}"
class StandPosizione(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo_base, posizione):

        super().__init__(codice_stand, superficie, padiglione, prezzo_base)
        self.prezzo = prezzo_base * 1.30
        self.posizione = posizione

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = "Occupato"

        return f"{self.codice_stand}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo:.2f}€ - Posizione {self.posizione} - {stato}"
class Espositori:
    def __init__(self, codice_espositore, nome_espositore, cognome_espositore):
        self.codice_espositore = codice_espositore
        self.nome_espositore = nome_espositore
        self.cognome_espositore = cognome_espositore
        self.stand = None

    def __str__(self):
        if self.stand is None:
            stato = "Non associato"
        else:
            stato = self.stand
        return f"{self.codice_espositore}: {self.nome_espositore} - {self.cognome_espositore} - Stand: {stato}"
