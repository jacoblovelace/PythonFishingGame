from Fish_Classes import *
from Pond_Class import *

sakura_pond = Pond('Sakura Pond', 3, 4, [Goldfish, Koi, Catfish],
                   "A quiet, still pond surrounded by cherry blossom trees.")
aspen_river = Pond('Aspen River', 9, 3, [Salmon, Bass, Trout],
                   "A river.")
breezy_lake = Pond('Breezy Lake', 7, 7, [Carp, Pike, Bass, Crappie, Perch],
                   "Large lake with a variety of fish.")
muddy_marsh = Pond('Muddy Marsh', 8, 5, [Bass, Herring, Shad, Catfish, Perch],
                   "Muddy waters.")


PONDS = [
        sakura_pond,
        aspen_river,
        breezy_lake,
        muddy_marsh
    ]
