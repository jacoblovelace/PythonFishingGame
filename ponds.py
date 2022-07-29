from Fish_Classes import *
from Pond_Class import *

sakura_pond = Pond('Sakura Pond', 3, 4, [4, 3], [Koi, Goldfish, Catfish],
                   "A quiet, still pond surrounded by cherry blossom trees.")
aspen_river = Pond('Aspen River', 9, 3, [6, 3], [Salmon, Bass, Trout],
                   "A river.")
breezy_lake = Pond('Breezy Lake', 7, 7, [6, 3], [Carp, Pike, Bass, Crappie, Perch],
                   "Large lake with a variety of fish.")
muddy_marsh = Pond('Muddy Marsh', 8, 5, [8, 5], [Bass, Herring, Shad, Catfish, Perch],
                   "Muddy waters.")
radioactive_lagoon = Pond('Radioactive Lagoon', 10, 9, [2, 2], [Dead_Fish, Glowfish],
                          "Most fish die here.")
furious_river = Pond('Furious River', 12, 5, [5, 4], [Electric_Eel, Piranha, Bull_Shark],
                     "Dangerous river.")

PONDS = [
    sakura_pond,
    aspen_river,
    breezy_lake,
    muddy_marsh,
    radioactive_lagoon,
    furious_river
]
