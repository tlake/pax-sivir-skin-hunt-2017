from main.game_logic import (
    AtticView,
    AtticObject,
    # InspectSkinCodeObject,
    OpenSkinCodeObject,
    UseSkinCodeObject,
    YuGiOhSkinCodeObject,
    ChestSkinCodeObject,
)


################################
# SKIN CODE OBJECT DECLARATIONS
################################

skin_codes = [
    "NA23687X8PDRBJHXXV724GUXZ",  # redeemed by Austin
    "NA23688YE6TLQLKXAN6Q36ZSJ",  # redeemed by Ann
    "NA2368RJALWMQVEBN6J3WHBRB",  # redeemed by YES?
    "NA2368QZ874722C6KC3CSQDDF",  # redeemed by Sawyer; from Selena

    "NA236844QT3QHM7FFXLAVQ3ZJ",  # redeemed by Rory; one of Christine's
    "NA2368BJTYMRFBDQLX5TC7PB8",  # one of Christine's; not implemented in game

    "NA2368GXZDTRL2BLS4WRMRLVZ",  # found by Hambone; confirmed already used, tho
]

yugioh_skin_code = YuGiOhSkinCodeObject(
    name="yugioh",
    code=skin_codes[0],
    identifiers=[
        "cards",
        "deck",
        "yugioh",
    ],
    look_text=(
        "The backs of these cards are brown with a black oval in the center. "
        "Do you believe in the heart of the cards?"
    ),
    inspect_text=[
        (
            "http://vignette2.wikia.nocookie.net/yugioh/images/2/21/DarkMagicianGirl-SDMY-EN-C-1E.png/revision/latest?cb=20161021195941",
            "Dark Magician Girl"
        ),
        (
            "https://vignette4.wikia.nocookie.net/yugioh/images/d/da/InjectionFairyLily-LCJW-EN-C-1E.png/revision/latest?cb=20131015031814",
            "Injection Fairy Lily"
        ),
        (
            "https://vignette.wikia.nocookie.net/yugioh/images/4/4c/GeminiElf-YSYR-EN-C-1E.png/revision/latest?cb=20170901153234",
            "Gemini Elf"
        ),
        (
            "https://vignette.wikia.nocookie.net/yugioh/images/8/86/Nekogal1-TP6-EN-C-UE.jpg/revision/latest?cb=20081030041455",
            "Nekogal #1"
        ),
        (
            "https://vignette.wikia.nocookie.net/yugioh/images/9/9b/HighPriestessofProphecy-BPW2-NA-UR-1E.png/revision/latest?cb=20140120115659",
            "High Priestess of Prophecy"
        ),
        (
            "https://vignette.wikia.nocookie.net/yugioh/images/b/bb/HarpieGirl-LCJW-EN-C-1E.png/revision/latest?cb=20131011123335",
            "Harpie Girl"
        ),
        (
            "https://vignette.wikia.nocookie.net/yugioh/images/2/24/HarpieDancer-LCJW-EN-UR-1E.png/revision/latest?cb=20131011120627",
            "Harpie Dancer"
        ),
        (
            "https://vignette.wikia.nocookie.net/yugioh/images/c/cb/HarpieChanneler-MP14-EN-UR-1E.png/revision/latest?cb=20140904212514",
            "Harpie Channeler"
        ),
    ],
)

poro_skin_code = OpenSkinCodeObject(
    name="poro",
    code=skin_codes[1],
    identifiers=[
        "poro",
    ],
    look_text=(
        "A small, white, fluffy, round creature. "
        "It has beady black eyes and small horns, and its mouth seems to be actuated so it can open and close."
    ),
    open_text=(
        "You open the mouth of the poro, and sitting on its fabric tongue is a skin code!"
    ),
)

bag_skin_code = OpenSkinCodeObject(
    name="bag",
    code=skin_codes[2],
    identifiers=[
        "bag",
        "sack",
        "pax",
        "swag",
        "swag bag",
        "pax bag",
        "pax sack",
    ],
    look_text=(
        "It's a cheap white plastic bag with assorted computer company branding plastered all over it. "
        "The top has been rolled down, but you can make out the lines of various cardstock things inside it. "
        "It's probably just advertisements, like it always is at PAX."
    ),
    open_text=(
        "You open up the bag and peek inside. "
        "You see a League of Legends lanyard featuring Thresh and Lucian and advertisements from Alienware, ASUS, Intel, Logitech, MSI, and others. "
        "There are some pins, and cards advertising for a bunch of indie games, some non-indie games, and... yes! "
        "A card with a skin code on it!"
    ),
)

mirror_skin_code = UseSkinCodeObject(
    name="mirror",
    code=skin_codes[3],
    identifiers=[
        "mirror",
    ],
    look_text=(
        "A full-length mirror stands here, a little out of place with the other outdoorsy objects. "
        "It's rectangular with gently rounded corners and silver curlicues swirling around the edges."
    ),
    inspect_text=(
        "Moving closer to the mirror, you stand directly in front of it to get a good look at your... hair or something. "
        "Your reflection changes, however. "
        "Instead of looking how you normally look - which... no, I shouldn't say anything - you see yourself wearing a blue and grey and yellow futuristic cyber suit. "
        "An orange visor covers your eyes, your hair is long and silvery, and you're holding an oversized X-shaped boomerang."
        "<br><br>"
        "It seems like your reflection wants to give you something."
    ),
    use_text=(
        "Your reflection motions for you to come closer. "
        "You do, half-expecting it to produce a skin code and put it in its pocket and then somehow you would have a skin code in *your* pocket. "
        "Instead, the reflection whispers to you. "
        "'This isn't the Mirror of Erised. "
        "That's somebody else's intellectual property. "
        "The skin code is taped to the back of the mirror.'"
    ),
)

chest_skin_code = OpenSkinCodeObject(
    name="chest",
    code=skin_codes[4],
    identifiers=[
        "chest",
        "treasure",
        "treasure chest",
        "obvious",
    ],
    look_text=(
        "It's certainly a very pretty chest. "
        "The wood is stained a dark brown, and it's accented with gold filigree. "
        "It's a modest size - about the size of a carry-on bag."
    ),
    open_text=(
        "The hinges of the chest creat as you pivot the lid backwards. "
        "The interior of the chest is dark and empty - except for a skin code! "
        "Congratulations! "
        "You found the obvious one!"
    ),
)

dubious_chest_skin_code = ChestSkinCodeObject(
    name="dubious_chest",
    code=skin_codes[-1],
    identifiers=[
        "chest",
        "treasure",
        "treasure chest",
    ],
    look_text=(
        "It's certainly a pretty chest - wood stained a dark brown, accented with gold filigree. "
        "It's a modest size, about the size of a carry-on bag."
    ),
    open_text=(
        "The hinges of the chest creak as you pivot the lid backwards. "
        "The interior of the chest is dark and empty - except for a skin code!"
    ),
)


################################
# STANDARD OBJECT DECLARATIONS
################################

# -- NORTH --

ten_speed = AtticObject(
    look_text=(
        "While technically a bicycle, this one is maybe a little non-traditional. "
        "The chassis of the device is less machined steel or aluminum, and more the skeleton of some devil. "
        "The bones of its arms and legs extend downward to clutch the wheels' axels with clawed digits, and the fiend is hunched forward such that its torso bridges the wheels and forms the frame of the bike. "
        "At the front of the bike, the demon's skull glares balefully forward. "
        "Flames dance in its empty eye sockets and its maw gapes open in a screaming grin, exposing needle-like teeth. "
        "From the temples extend a pair of ridged ram's horns, curving down to serve as handlebars."
        "<br><br>"
        "'So are you gonna kill her off?' it asks."
    ),
    identifiers=[
        "bike",
        "bicycle",
        "ten",
        "speed",
        "demon",
        "demonic",
    ],
    inspect_text=(
        "With a closer look, you notice that the bicycle is covered in the blood of some god and grave dirt. "
        "<br><br>"
        "'The only thing love's done is put you in this position,' it says. 'I say kill her off.'"
        "<br><br>"
        "This bike says plenty of things. And how's that work? It's a bicycle..."
    ),
)

ladder = AtticObject(
    identifiers=[
        "ladder",
    ],
    look_text=(
        "An old wooden ladder. "
        "The hinges are a little rusty and some of the rungs look worn, but otherwise it's in decent condition."
    ),
)

lightbulb = AtticObject(
    identifiers=[
        "light",
        "bulb",
        "lightbulb",
    ],
    look_text=(
        "A simple light bulb, low in wattage, secured to the wall with a simple white ceramic plate. "
        "The small chain that toggles the power to the light hangs from the plate."
    ),
    use_text=(
        "You pull the small chain, and the light goes off. "
        "After a moment or two of allowing your eyes to adjust to the darkness, you realize that it's just really dark in here now. "
        "You pull the chain again to turn on the light and continue your search."
    ),
)

outdoorsy = AtticObject(
    identifiers=[
        "outdoorsy",
    ],
    look_text=(
        "You put on some sunglasses, a straw hat, some flannel, a vest, and some heavy boots. "
        "You now look outdoorsy."
    ),
)

pool = AtticObject(
    identifiers=[
        "pool",
        "noodle",
        "noodles",
    ],
    look_text=(
        "In addition to the life vests, there are three foam pool noodles here on the floor; red, blue, and green. "
        "The green one seems to have been gotten hold of by a dog at some point in its past, judging by the chewed-up appearance."
    ),
    inspect_text=(
        "The partially-shredded state of the green noodle warrants closer inspection in your opinion, so you take a harder look. "
        "Your detective work determines that yes, this noodle was indeed likely chewed on by a dog for a minute or two."
    ),
)

vests = AtticObject(
    identifiers=[
        "life",
        "vest",
        "vests",
        "lifevests",
        "lifevest",
    ],
    look_text=(
        "In addition to the pool noodles, there are two orange life vests here on the floor. "
        "They seem like rather standard life vests."
    ),
)

shelving = AtticObject(
    identifiers=[
        "shelf",
        "shelves",
        "shelfs",
        "shelving",
    ],
    look_text=(
        "A metal shelving unit with three shelves stands about four feet tall. "
        "It was painted a navy blue many years ago, and the paint has flaked off in parts. "
        "The top shelf holds a small toolbox, while the bottom two shelves are home to a small assortment of gardening implements."
    ),
)

toolbox = AtticObject(
    identifiers=[
        "toolbox",
        "tools",
        "tool box",
        "box",
    ],
    look_text=(
        "The toolbox is one of those old metal ones with a clasp on the front and a handle on the top - the kind that looks a little like an old lunch pail."
    ),
    open_text=(
        "The interior of the toolbox contains a small ball-peen hammer, a pair of needlenose pliers, a couple of fishing hooks, a carpet knife without blades, and a roll of electrical tape on its last legs. "
        "No skin code, though."
    ),
)

gardening = AtticObject(
    identifiers=[
        "gardening",
        "garden",
        "implements",
        "equipment",
    ],
    look_text=(
        "An assortment of things like cute trowels, old gloves, watering cans containing rather more cobwebs than water, and plastic plant markers."
    ),
    inspect_text=(
        "Handling these items, nothing seems of any interest except for the watering can. "
        "As you move to pick it up, a large grey spider climbs out of the spout and waggles a forelimb disapprovingly at you. "
        "Wisely applying the live-and-let-live principle, you leave the watering can alone, and the spider retreats back into its home. "
    ),
)


# -- EAST --

eastern_window = AtticObject(
    identifiers=[
        "window",
        "glass",
    ],
    look_text=(
        "The window bears only a passing semblance to something described as 'transparent' because of the thick layer of dust that's built up and solidified on it over the years. "
        "Dust, and... could that be steam? "
        "Is that moisture billowing up on the other side of the glass? "
        "Are there figures moving about? "
        "Are those the voices of attractive naked people playing naughty games in a bath house just beyond this wall?"
        "<br><br>"
        "Possibly. "
        "But this wall is the wall of an attic, and it's very doubtful that there would be an entire bath house just on the other side of it. "
        "More likely, you're a bit of a perv and maybe dehydrated."
    ),
)

cat = AtticObject(
    identifiers=[
        "cat",
        "kitty",
        "meow",
        "meow-wow",
        "feline",
        "royalty",
    ],
    look_text=(
        "You look at the cat. It's a sleek black thing, resting comfortably in traditional loaf form upon the window sill. "
        "I don't know whose cat it is, or how it keeps getting into my attic, but there it is."
    ),
    inspect_text=(
        "A closer examination reveals a creature that would not, in a million years, deign to give a fraction of a single shit about you."
        "<br><br>"
        "This does nothing to stop you from exclaiming, 'AAH, KITTY!' and scritching its fuzzy little noggin."
    ),
    open_text=(
        "You monster!"
    ),
)

jumanji = AtticObject(
    identifiers=[
        "game",
        "jumanji",
        "board",
        "board game",
    ],
    look_text=(
        "Of course there's a copy of Jumanji in my attic. "
        "Do I really need to describe it to you? "
        "The box has a jungley theme about it, and large jungle-themed letters proclaim 'JUMANJI' across its top. "
        "Now go and watch the movie, you person who was deprived of a childhood. "
        "(And I mean the old one, with Robin Williams. "
        "If you see the newer one, let me know if it's any good.)"
    ),
    inspect_text=(
        "Of course you look closer. "
        "Either you know the story and want to test my cred, or you're genuinely curious, in which case, stop this and go see the movie. "
        "But here, I'll throw you a bone. "
        "Leaning closer, you can read some of the smaller print:"
        "<br><br>"
        "A game for those who seek to find<br>"
        "A way to leave their world behind"
    ),
    open_text=(
        "You open the box in pursuit of the promised 'way to leave [your] world behind.' "
        "The interior of the box contains..."
        "<br><br>"
        "Rather a lot of drug paraphrenalia. "
        "Huh. "
        "Let's just close that back up."
    ),
    use_text=(
        "Oh, no you don't. "
        "I know how this story goes, and I'm not spending my time writing it again in a text-based adventure game about finding League skin codes. "
        "Just go see the movie."
    ),
)

dollhouse = AtticObject(
    identifiers=[
        "doll",
        "house",
        "dollhouse",
    ],
    look_text=(
        "Somebody put a lot of love and work into making this little house. "
        "There's a fine paint job on it, the doors and shutters are articulated, and the whole thing pivots open on a hinge along one wall."
    ),
    open_text=(
        "Sure looks like the inside of a dollhouse. "
        "Tiny furniture, tiny decorations, a working electrical system; "
        "even a tiny functioning stove like in those tiny cooking YouTube videos. "
    ),
    use_text=(
        "There are a couple of figures scattered around the small house, and you spend some time delighting in a story that you make up between them: "
        "Sally comes home from a day at the office to meet her boyfriend who is also getting home from his job in animal control. "
        "They make a nice dinner and talk about their day, then retire to the big sofa in the den. "
        "They get cozy, then they start making out, and they start tearing off each others' clothes, and... "
        "You made it weird. "
        "Stop."
        "<br><br>"
        "Stop it."
    ),
)

harp = AtticObject(
    identifiers=[
        "harp",
        "instrument",
    ],
    look_text=(
        "It's a gorgeous harp - not one of those little lap ones, but a full-sized harp that stands on the floor when you use it. "
        "If I had a Sona skin to give away, I'd almost certainly hide it here."
    ),
    inspect_text=(
        "You pluck at a couple of the strings to find that they're miraculously in-tune!"
    ),
    use_text=(
        "I have no idea if you're good at the harp or not, so let's just say that you do whatever your version of 'playing' the harp is. "
        "I love and/or hate it."
    ),
)


# -- SOUTH --

cardboard_boxes = AtticObject(
    identifiers=[
        "cardboard",
        "boxes",
        "box",
    ],
    look_text=(
        "A couple of small cardboard boxes. "
        "They are a little bent and sagging in places, suggesting that they've gone through a few moves before finding their current resting spot."
    ),
    open_text=(
        "Opening the boxes, you find a lot of assorted papers that don't hold your interest. "
        "You also see a small collection of old photographs, a PAX swag bag, and a Super Nintendo Entertainment System."
    )
)

photos = AtticObject(
    identifiers=[
        "photos",
        "photo",
        "photographs",
        "photograph",
        "pictures",
        "picture",
    ],
    look_text=(
        "Flipping through the small stack of old photographs, they seem to be heartwarming images of your great grandmother. "
        "(No, I don't know why I have pictures of your grandmother.) "
        "She's wearing a very proper uniform in the first couple of pictures, and then a very nice polka-dotted frock. "
        "The next couple of pictures show her at a picnic, and then in a slinky dress. "
        "Next are some photos of her at a beach in a swimsuit, and then... "
        "Oh. "
        "Looks like your grandma was a pinup girl."
    ),
)

snes = AtticObject(
    identifiers=[
        "snes",
        "super",
        "nintendo",
        "entertainment",
        "system",
    ],
    look_text=(
        "A dusty SNES that's lost some of its color to the ravages of time. "
        "'Mega Man X' is in the cartridge slot."
    ),
    inspect_text=(
        "It doesn't seem like any of the cables are in this box with the SNES, and some of the buttons on the one controller you find tend to stick a bit when you press them. "
        "You probably won't be able to play this console inside of this this text-based game."
    ),
    use_text=(
        "Look, I know the graphics in my game here suck. "
        "It's a text-based adventure game. "
        "You knew that coming into this. "
        "If you wanted to <a target='blank' href='http://lmgtfy.com/?q=snes+emulator'>play something else</a>, you should have just done so from the start."
    ),
)

katamari = AtticObject(
    identifiers=[
        "katamari",
    ],
    look_text=(
        "Instead of taking the time to organize a bunch of various things, I've instead decided to just roll stuff up with this katamari and leave the whole shebang in my attic. "
        "The katamari currently holds various items like shoes and legos and townsfolk and roses and star matter and a shield."
    ),
    use_text=(
        "Easy there, friend. "
        "You're not a Prince of the Cosmos. "
        "Better leave katamari manipulation to the professionals."
    ),
)

shoes = AtticObject(
    identifiers=[
        "shoes",
    ],
    look_text=(
        "There are a bunch of assorted shoes held to the katamari; many of them are singletons, missing the other half of their pair."
    ),
)

legos = AtticObject(
    identifiers=[
        "legos",
        "lego",
    ],
    look_text=(
        "A whole bunch of legos are stuck onto the katamari. "
        "It makes them impossible to play with, but it saves you from finding their caltropy corners with your feet."
    ),
)

townsfolk = AtticObject(
    identifiers=[
        "townsfolk",
        "townspeople",
        "folk",
        "folks",
        "people",
        "town",
    ],
    look_text=(
        "Plastered to the katamari are almost a dozen people, with arms and legs stretched out straight. "
        "Their mouths are opened in silent screams, their eyes plead for aid, and their limbs wiggle in terror. "
        "A lot of the guys have weird haircuts."
        "<br><br>"
        "If you'd like to avoid their fate, you'll keep quiet."
    ),
)

roses = AtticObject(
    identifiers=[
        "roses",
        "flowers",
        "rose",
        "flower",
    ],
    look_text=(
        "There are a lot of roses stuck to this katamari. "
        "It's almost like someone spent countless hours trying to roll up a million of them."
    ),
)

star_matter = AtticObject(
    identifiers=[
        "star",
        "matter",
    ],
    look_text=(
        "There are several points of bright light around the katamari. "
        "Since we don't have eclipse glasses here, I recommend that you don't look at them very closely."
    ),
    inspect_text=(
        "Egad, DON'T look directly at the starstuff!"
    ),
)

shield = AtticObject(
    identifiers=[
        "shield",
    ],
    look_text=(
        "It's a round shield, decorated in red, white, and blue. "
        "A large five-pointed star occupies the center."
        "<br><br>"
        "Yeah, it's Cap's shield. No big."
    ),
    inspect_text=(
        "Looking closer, you read on the backside, 'Made in China.'"
        "<br><br>"
        "Okay, fine, you got me. "
        "It's a replica."
    ),
)


# -- WEST --

western_window = AtticObject(
    identifiers=[
        "window",
    ],
    look_text=(
        "The western window is dark, as if there were no light on the other side. "
        "It seems clean, though, so it's not like the window itself is so filthy that light cannot penetrate it. "
        "It's just dark on the other side."
    ),
    inspect_text=(
        "You bring your face closer to the window in an effort to learn why it's so dark. "
        "As you squint, with your nose almost touching the glass, your breath begins to come out in mist and your face grows chilly. "
        "A pale hand slams against the glass from the other side! "
        "You jump back, startled, and the hand fades away."
        "<br><br>"
        "I maybe should have told you that the western window is just a little bit haunted."
    ),
)

stuffed_animals = AtticObject(
    identifiers=[
        "stuffed",
        "animals",
    ],
    look_text=(
        "The assortment of stuffed animals includes a green cactus, an oblong manatee, a white poro, a spherical T-Rex, and a squirrel."
    ),
)

cactuar = AtticObject(
    identifiers=[
        "cactus",
        "green",
        "cactuar",
    ],
    look_text=(
        "The cactus has two arm and two legs, extended and bent at right angles. "
        "It has two black buttons for eyes and an oval of black fabric for a mouth, which gives it a constantly surprised appearance."
    ),
    inspect_text=(
        "Picking up the cactus, you drop it almost immediately as it fires ten thousand tiny needles at you. "
        "If you had hit points, you would have lost 9,999 of them."
    ),
)

urf_manatee = AtticObject(
    identifiers=[
        "urf",
        "manatee",
        "urf manatee",
        "urf_manatee",
    ],
    look_text=(
        "A stuffed manatee covered in a light blue, short-fiber velvet. "
        "It wears a white bib trimmed in red around its neck, and a stuffed replica of a chaingun on its back. "
        "In one of its flipper-hands, it holds a spatula."
    ),
)

t_rex = AtticObject(
    identifiers=[
        "t rex",
        "t-rex",
        "t_rex",
        "trex",
    ],
    look_text=(
        "It's a super-soft, super-squishy, T-Rex-from-Dinosaur-Comics plushy! "
        "It's been made delightfully Squishable(TM) by turning its entire body into a sphere and reducing its appendages to stubby proportions."
    ),
    inspect_text=(
        "You peer closer at the T-Rex, and conclude that hugging it tightly would be good for your soul."
    ),
    use_text=(
        "This T-Rex is really good to squeeze. "
        "You have discovered this fact by squeezing the T-Rex. "
        "It's truly delightful."
    ),
)

rocking_chair = AtticObject(
    identifiers=[
        "rocking",
        "chair",
    ],
    look_text=(
        "It's a pretty standard rocking chair. "
        "It's got, like, a seat, and a back, and a couple of arms, and a couple of rocking slats."
    ),
    use_text=(
        "You push aside a couple of the stuffed animals and nestle down into the chair. "
        "You feel at peace, and also like an old person."
    ),
)

squirrel = AtticObject(
    identifiers=[
        "squirrel",
    ],
    look_text=(
        "A life-sized squirrel. "
        "Its fur looks a little matted."
    ),
    inspect_text=(
        "Closer examination reveals that... this isn't a stuffed animal! "
        "Well, I mean, it is. "
        "It's an animal that has been stuffed. "
        "Why is there a taxidermied squirrel in my attic? "
        "Is this yours?"
    ),
)


# -- UP --

rafters = AtticObject(
    identifiers=[
        "rafters",
        "rafter",
        "wood",
        "beams",
        "beam",
    ],
    look_text=(
        "The ceiling of the attic is exposed, and between the wooden rafters you can see insulation strapped to the underside of the roof. "
        "Cobwebs cling among the beams, and a deck of cards can just barely be seen resting on the top of one of the rafters."
    ),
)

uppern_cobwebs = AtticObject(
    identifiers=[
        "webs",
        "cobwebs",
        "spider webs",
        "spider",
    ],
    look_text=(
        "For the most part, the spider webs contain nothing but attic dust. "
    ),
    inspect_text=(
        "One of the webs contains a large spider with a human face on the back. "
        "If you talk to it, it will go on and on about its human days, and the fabulously rich family that it used to be a part of. "
        "It'll promise you a bigger wallet in exchange for your hand in the genocide of a rare spider species. "
        "Don't listen to it. "
        "It's its own fault that it's a spider now. "
        "Maybe it shouldn't have been so greedy."
    ),
)


# -- DOWN --

heart = AtticObject(
    identifiers=[
        "sound",
        "beat",
        "pulse",
        "noise",
        "floor",
        "board",
        "boards",
        "floorboard",
        "floorboards",
    ],
    look_text=(
        "The floor is made of once-smooth wooden boards, but time has warped and roughed them up a little bit. "
        "The sound is definitely coming from underneath the floor."
    ),
    inspect_text=(
        "You zero in on the source of the sound - it's coming from underneath one of the floorboards, and it's loose."
    ),
    open_text=(
        "You pry up the edge of the loose floorboard and look underneath. "
        "It's, uh... "
        "It's a beating heart."
        "<br><br>"
        "Maybe just close that back up. "
        "I've read Edgar Allen Poe."
    ),
)

feet = AtticObject(
    identifiers=[
        "feet",
        "foot",
        "shoes",
        "shoe",
        "self",
    ],
    look_text=(
        "You can look at your feet on your own time."
    ),
    use_text=(
        "You're already using your feet. "
        "You're standing in my attic on them."
    ),
)

exit = AtticObject(
    identifiers=[
        "out",
        "exit",
        "door",
        "ladder",
    ],
    look_text=(
        "Yes, in the real world, attics have exits into other parts of the house. "
        "In this world, that's not the case. "
        "Here, the exit leads down into a room that is exactly the same as this one, like some kind of funky dream. "
    ),
    use_text=(
        "You go down through the door and are greeted with a situation exactly the same as the one you were in before you decided to use the door."
    ),
)


################################
# GAME CONTENT COMPILATION
################################

SKIN_CODE_OBJECTS = {
    yugioh_skin_code.name: yugioh_skin_code,
    poro_skin_code.name: poro_skin_code,
    bag_skin_code.name: bag_skin_code,
    mirror_skin_code.name: mirror_skin_code,
    chest_skin_code.name: chest_skin_code,
}


VIEWS = {
    "north": AtticView(
        look_text=(
            "The northern part of the room houses the bare lightbulb responsible for illuminating the attic. "
            "The storage in this area seems mostly devoted to outdoorsy things. "
            "Old pool noodles and life vests lie in a pile on the floor, and a ladder leans upright against the wall. "
            "A small shelving unit houses a toolbox and various gardening equipment. "
            "What seems like a bicycle is leaning upon the wall, and a silvery mirror stands in the corner."
        ),
        objects={
            "ten_speed": ten_speed,
            "ladder": ladder,
            "lightbulb": lightbulb,
            "outdoorsy": outdoorsy,
            "pool": pool,
            "vests": vests,
            "shelving": shelving,
            "toolbox": toolbox,
            "gardening": gardening,
            mirror_skin_code.name: mirror_skin_code,
        },
    ),
    "east": AtticView(
        look_text=(
            "The eastern part of the attic has a small window set into the wall, upon the sill of which rests a drowsy cat. "
            "Below the window is a dollhouse, with an obvious treasure chest and a board game laying nearby. "
            "A harp stands off in the corner."
        ),
        objects={
            "window": eastern_window,
            "cat": cat,
            "jumanji": jumanji,
            "dollhouse": dollhouse,
            chest_skin_code.name: chest_skin_code,
            "harp": harp,
        },
    ),
    "south": AtticView(
        look_text=(
            "The south side of the attic contains mostly the kinds of things you would put in a container labelled 'misc' in order to forget about. "
            "A few cardboard boxes are stacked up off to one side; on the other side rests a katamari, acting as a catch-all for items without a proper storage location."
        ),
        objects={
            "cardboard_boxes": cardboard_boxes,
            "photos": photos,
            bag_skin_code.name: bag_skin_code,
            "snes": snes,
            "katamari": katamari,
            "shoes": shoes,
            "roses": roses,
            "townsfolk": townsfolk,
            "star_matter": star_matter,
            "legos": legos,
            "shield": shield,
        },
    ),
    "west": AtticView(
        look_text=(
            "The western portion of the attic primarily features a window and an assortment of stuffed animals. "
            "Some of them have been nestled upon an old rocking chair."
        ),
        objects={
            poro_skin_code.name: poro_skin_code,
            "window": western_window,
            "stuffed_animals": stuffed_animals,
            "cactuar": cactuar,
            "urf_manatee": urf_manatee,
            "t_rex": t_rex,
            "rocking_chair": rocking_chair,
            "squirrel": squirrel,
        },
    ),
    "up": AtticView(
        look_text=(
            "Looking up into the low rafters of the attic, you immediately spot a plethora of dusty cobwebs swaying ever so slightly with the sluggish air circulation up here. "
            "In the dimness, something almost catches your eye in the rafters."
        ),
        objects={
            yugioh_skin_code.name: yugioh_skin_code,
            "rafters": rafters,
            "uppern_cobwebs": uppern_cobwebs,
        },
    ),
    "down": AtticView(
        look_text=(
            "Looking down gets you a view of your own feet (maybe), the floor, and the exit down into the house. "
            "With little of interest, you can discern a soft pulsing sound coming from underneath the floorboards."
        ),
        objects={
            "heart": heart,
            "feet": feet,
            "exit": exit,
        },
    ),
}
