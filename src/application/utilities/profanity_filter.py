from better_profanity import Profanity


profanity_list = ['puto', 'idiot', 'fuck', "Mamon", "Pinche", "verga", "huevon", "Chinga", "Pendejo", "Chingar", "Puta",
                  "huevos", "Chachalaco", "Malacopa", "Chingaquedito", "Argüendero", "chingada", "Cascado", "asshole",
                  "hooker", "Dumbass", "Motherfucker", "bitch", "perra", "Imbecil", "estupido", "maricon", "mierda",
                  "maldito", "pene", "p3n3", "pito", "p1t0", "pit0", "p1to", "bastard", "bastardo", "puto", "puta",
                  "putas", "putos", "dick", "d1ck", "fucking", "fuck1ng", "fock", "f0ck", "vtm", "ptm", "pt" "chtm",
                  "ctm", "vrg"]

profanity = Profanity()
profanity.add_censor_words(profanity_list)