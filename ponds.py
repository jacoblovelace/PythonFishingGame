from Fish_Classes import *
from Pond_Class import *

sakura_pond = Pond('Sakura Pond', 3, 4, [4, 3], False, [Koi, Goldfish, Catfish],
                   "A small, tranquil pond in a cherry blossom forest that many koi fish call home.")
aspen_river = Pond('Aspen River', 9, 3, [6, 3], False, [Salmon, Bass, Trout],
                   "A narrow and winding river with a steady current.")
breezy_lake = Pond('Breezy Lake', 7, 7, [6, 3], False, [Carp, Pike, Bass, Crappie, Perch],
                   "Large lake with a variety of fish.")
muddy_marsh = Pond('Muddy Marsh', 8, 5, [8, 5], False, [Bass, Herring, Shad, Catfish, Perch],
                   "Muddy waters.")
radioactive_reservoir = Pond('Radioactive Resevoir', 10, 9, [3, 3], False, [Dead_Fish, Mutant_Minnow, Glowfish],
                             "Most fish die here.")
furious_river = Pond('Furious River', 12, 5, [5, 4], False, [Electric_Eel, Piranha, Payara, Bull_Shark],
                     "Dangerous!.")
open_ocean = Pond('Open Ocean', 24, 24, [8, 6], True, [Herring, Jellyfish, Anchovy, Sardine, Great_White_Shark, Tuna],
                  "The big, open, middle of the sea.")
sapphire_pier = Pond('Sapphire Pier', 6, 16, [5, 4], False,
                     [Flounder, Mullet, Hammerhead_Shark, Redfish, Mackerel, Croaker],
                     "")
desert_basin = Pond('Desert Basin', 7, 8, [6, 5], False,
                    [Desert_Sucker, Loach_Minnow, Pupfish, Bonytail_Chub, Squawfish],
                    "")
rainbow_reef = Pond('Rainbow Reef', 12, 12, [3, 2], False,
                    [Clownfish, Snapper, Angelfish, Triggerfish, Tang, Pufferfish,
                     Sea_Turtle],
                    "A beautiful coral reef situated in warm, tropical waters and inhabitated by a diverse population "
                    "of ocean dwellers.")
kelp_forest = Pond('Kelp Forest', 10, 12, [6, 4], False,
                   [Piece_of_Kelp, Sea_Turtle, Giant_Kelpfish, Rockfish, Bonito, Blue_Shark],
                   "")
killer_tooth_bay = Pond('Killer Tooth Bay', 8, 13, [5, 3], True,
                        [Blue_Shark, Mako_Shark, Tiger_Shark, Hammerhead_Shark, Great_White_Shark, Whale_Shark],
                        "You'll need a strong rod if you fish here.")

terror_trench = "Terror Trench [Anglerfish, Goblin_Shark, Pelican_Eel, Dragonfish, Deepsea_Octopus]" \
                " (trackers do not work here because it is too dark)"

# [Marlin, Swordfish, Barracuda]

pirate_ship_graveyard = "Pirate Ship Graveyard [Kraken, Ghost_Fish, Giant_Squid, Dead_Fish, Debris]"

PONDS = [
    sakura_pond,
    aspen_river,
    breezy_lake,
    muddy_marsh,
    radioactive_reservoir,
    furious_river,
    open_ocean,
    sapphire_pier,
    desert_basin,
    rainbow_reef,
    kelp_forest,
    killer_tooth_bay
]
