class deck:
    def __init__(self):
        self.cards = [[0 for i in range(13)] for j in range(4)]

    def Card_translator(self,y1,y2):
        conversortipo =  {
            0: "Copas",
            1: "Diamantes",
            2: "Corações",
            3: "Espadas" }

        conversorcarta = {
            0: "As",
            1: "2",
            2: "3",
            3: "4",
            4: "5",
            5: "6",
            6: "7",
            7: "8",
            8: "9",
            9: "10",
            10: "Valete",
            11: "Rainha",
            12: "Rei"    }

        return ( conversorcarta.get(y2) + " de "  + conversortipo.get(y1) );

    def Card_emoji(self,y1,y2):
        conversorTIPO =  {
            0: '\u1F0D' ,
            1: '\u1F0C' ,
            2: '\u1F0B' ,
            3: '\u1F0A' }

        conversorCARTA = {
            0: '1',
            1: '2',
            2: '3',
            3: '4',
            4: '5',
            5: '6',
            6: '7',
            7: '8',
            8: '9',
            9: 'A',
            10: 'B',
            11: 'D',
            12: 'E'    }

        return ('u' + conversorTIPO.get(y1) + conversorCARTA.get(y2) );
