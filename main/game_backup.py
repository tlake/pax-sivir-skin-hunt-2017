from django.core.exceptions import ObjectDoesNotExist
from main.models import SkinCode
from random import randint
from types import MethodType


class AtticView(object):
    def __init__(self, look_text="", objects={}):
        self.look_text = look_text
        self.objects = objects

    def describe(self):
        return self.look_text


class ActionEnabledObject(object):
    def __init__(self):
        self.action_map = {
            "close": self.close,
            "go": self.go,
            "inspect": self.inspect,
            "inventory": self.inventory,
            "look": self.look,
            "open": self.open,
            "take": self.take,
            "use": self.use,
        }

    def close(self):
        return "CLOSE doesn't work on that."

    def go(self):
        return "GO doesn't work on that."

    def inspect(self):
        return "INSPECT doesn't work on that."

    def inventory(self):
        return "INVENTORY doesn't work on that."

    def look(self):
        return "LOOK doesn't work on that."

    def open(self):
        return "OPEN doesn't work on that."

    def take(self):
        return "TAKE doesn't work on that."

    def use(self):
        return "USE doesn't work on that."


class AtticObject(ActionEnabledObject):
    def __init__(self,
                 identifiers=[],
                 inspect_text="",
                 look_text="",
                 open_text="You can't OPEN that.",
                 use_text="That's not something you can just USE.",
                 ):
        super().__init__()
        self.identifiers = identifiers
        self.inspect_text = inspect_text if inspect_text else look_text
        self.look_text = look_text
        self.open_text = open_text
        self.use_text = use_text

    def __repr__(self):
        return f"AtticObject: {self.identifiers}"

    def inspect(self, state):
        return (self.inspect_text, state)

    def look(self, state):
        return (self.look_text, state)

    def open(self, state):
        return (self.open_text, state)

    def use(self, state):
        return (self.use_text, state)


class SkinCodeObject(AtticObject):
    def __init__(self, name="", code="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        try:
            instance = SkinCode.objects.get(name=name)
        except ObjectDoesNotExist:
            instance = SkinCode(name=name, code=code)
            instance.save()

    def __repr__(self):
        return f"SkinCodeObject: {self.name}"

    def inspect(self, state):
        instance = SkinCode.objects.get(name=self.name)
        if instance.claimed:
            message = (
                "Congratulations! You've found a skin code!"
                "<br><br>"
                "...Unfortunately, somebody else has beaten you to it. "
                f"The code has been scratched off, and somebody has scrawled '{instance.summoner_name} wuz heer, get gud scrub' in heavy marker."
            )
            return (message, state)

        state["skin_code"] = self.name
        state["activation_step"] = "confirm_activation"
        message = (
            "Found a skin code! Would you like to claim it?"
            "<br><br>"
            "(enter YES to begin activation; anything else to abort)"
        )
        return (message, state)

    def activation(self, player_input, state):
        instance = SkinCode.objects.get(name=self.name)
        if instance.claimed:
            message = (
                "<br>Ooh, tough break! "
                f"As you were preparing to claim this skin code, {instance.summoner_name} shoved you out of the way and took it for themselves! "
                "Bummer."
                "<br><br>"
                "...But you know their summoner name, now, so maybe you could settle it in-game."
                "<br><br>"
                f"You are facing {state['direction']}. Command?"
            )
            del(state["activation_step"])
            del(state["skin_code"])
            return (message, state)

        if state["activation_step"] == "confirm_activation":
            if player_input.lower() == "yes":
                state["activation_step"] = "enter_human_name"
                message = "<br>Enter your human name:"
                return (message, state)

            message = (
                "<br>"
                "Aborting activation."
                "<br><br>"
                f"You are facing {state['direction']}. Command?"
            )
            del(state["activation_step"])
            del(state["skin_code"])
            return (message, state)

        if state["activation_step"] == "enter_human_name":
            instance.human_name = player_input
            instance.save()
            state["activation_step"] = "enter_summoner_name"
            message = "<br>Enter your summoner name:"
            return (message, state)

        if state["activation_step"] == "enter_summoner_name":
            instance.summoner_name = player_input
            instance.save()
            state["activation_step"] = "confirm_final_claim"
            message = (
                "<br>"
                f"Human name: {instance.human_name} <br>"
                f"Summoner name: {instance.summoner_name} <br>"
                "<br>"
                "Enter YES to finalize claim, or anything else to abort."
                "<br><br>"
                "WARNING - after finalization, you will only be able to see the code ONCE. "
                "Be careful not to leave or refresh or close the page until you've copied down the code."
            )
            return (message, state)

        if state["activation_step"] == "confirm_final_claim":
            if player_input.lower() == "yes":
                message = (
                    "Congratulations! Here is your code to get the PAX West 2017 Sivir skin!"
                    "<br><br>"
                    f"{instance.code}"
                    "<br><br>"
                    "Thanks for playing! "
                    "You can continue to explore, although I do ask that you not claim other skin codes if you find them."
                    "<br><br>"
                    f"You are facing {state['direction']}.  Command?"
                )
                instance.claimed = True
                instance.save()

            else:
                message = (
                    "<br>"
                    "Understood; aborting."
                    "<br><br>"
                    f"You are facing {state['direction']}. Command?"
                )

            del(state["activation_step"])
            del(state["skin_code"])
            return (message, state)


class YuGiOhSkinCodeObject(SkinCodeObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def use(self, state):
        return self.inspect(state)

    def inspect(self, state):
        if not state.get("cards_drawn"):
            state["cards_drawn"] = 0

        message = "Believing in the heart of the cards, you draw a card from the deck.<br><br>"

        i = randint(0, 4)

        if i > 0:
            message_parts = self.inspect_text[i]
            message += f"You draw: <a target='blank' href='{message_parts[0]}'>{message_parts[1]}</a>."

            state["cards_drawn"] += 1

            if state["cards_drawn"] > 6:
                state["cards_drawn"] = 0
                message += "<br><br>You're either pretty sure that I've hidden a skin code somewhere in this deck of cards, or you're really into the pictures on these cards. Not judgin', just sayin'."
            if state["cards_drawn"] == 6:
                message += "<br><br>This is starting to get creepy. What kind of person would keep a deck full of Yu-Gi-Oh! girls in his attic?"
            if state["cards_drawn"] == 4:
                message += "<br><br>Still haven't found any other sorts of cards in here, huh?"
            if state["cards_drawn"] == 2:
                message += "<br><br>There seem to be an awful lot of cards with pictures of anime girls on them in this deck."

            return (message, state)

        else:
            del(state["cards_drawn"])
            instance = SkinCode.objects.get(name=self.name)
            if instance.claimed:
                message += (
                    "You pull out a... wait, this isn't a Yu-Gi-Oh! card! "
                    "It's a skin code!"
                    "<br><br>"
                    "...Unfortunately, somebody else has beaten you to it. "
                    f"The code has been scratched off, and somebody has scrawled '{instance.summoner_name} wuz heer, git gud scrub' in heavy marker."
                )
                return (message, state)

            state["skin_code"] = self.name
            state["activation_step"] = "confirm_activation"
            message += (
                "You pull out a... wait, this isn't a Yu-Gi-Oh! card! "
                "It's a skin code! "
                "Would you like to claim it?"
                "<br><br>"
                "Enter YES to begin the activation process, or anything else to abort."
            )
            return (message, state)


class GameHandler(ActionEnabledObject):
    def __init__(self, data):
        super().__init__()
        self.state = data["playerState"]
        self.command = data["playerCommand"]
        self.action_map["help"] = self.help

    def __repr__(self):
        return "GameHandler"

    # Helper functions
    def command_is_valid(self):
        return self.command[0] in self.action_map.keys()

    def format_message(self, message):
        return "<br>" + message + f"<br><br>You are facing {self.state['direction']}. Command?"

    def get_player_view(self):
        player_direction = self.state["direction"]
        view = VIEWS[player_direction]
        return view

    def get_player_view_objects(self):
        view = self.get_player_view()
        return view.objects

    def apply_action_to_objects(self, action="", targets=[]):
        view_objects = self.get_player_view_objects()

        for target in targets:
            # It's possible for a player to specify the dict key entry.
            if target in view_objects.keys():
                view_object = view_objects[target]
                action_func = view_object.action_map[action]
                response, new_state = action_func(self.state)
                self.state = new_state
                return response

            # Otherwise, we look through all the objects in the current view.
            for obj in view_objects.values():
                if target in obj.identifiers:
                    action_func = obj.action_map[action]
                    response, new_state = action_func(self.state)
                    self.state = new_state
                    return response

        return f"Could not find {' '.join(targets).upper()} here."

    def grue_check(self):
        chance = self.state["grue_chance"]
        upper = 500
        roll = randint(0, upper)
        return roll < chance

    def handle_skin(self):
        active_skin_code = SKIN_CODE_OBJECTS[self.state.get("skin_code")]
        response, new_state = active_skin_code.activation(self.command, self.state)
        self.state = new_state
        return response

    # Game functions
    def run(self):
        if len(self.command) == 0:
            return "<br>Command?"

        if self.state.get("dead"):
            return "<br>You are dead. Refresh the page to start over!"

        if self.state.get("skin_code"):
            return self.handle_skin()

        eaten = self.grue_check()
        if eaten:
            self.state["dead"] = True
            message = (
                "<br>Oh no! "
                "Quite suddenly and without any warning, you have been eaten by a grue! "
                "This is not a result of what you were just doing, but you should probably expect a grue somewhere in every text-based adventure game."
                "<br><br>"
                "Refresh the page to restart."
            )

            return message

        self.state["grue_chance"] += 1
        self.command = self.command.lower().split()

        if not self.command_is_valid():
            return self.format_message(
                f"{self.command[0].upper()} is not a valid command. "
                "Try HELP for a list of obvious actions you can take."
            )

        response = self.action_map[self.command[0]]()
        return self.format_message(response)

    def close(self):
        return (
            "You're probably looking for [ctrl+w] or [command+w]. "
            "You could also click the 'X' on this tab or window."
        )

    def go(self):
        return (
            "You're in a single-room attic, and that single room is pretty small. "
            "Where do you expect to GO? "
            "The only exit here is the folding ladder that extends down into the house, which I haven't coded up. "
            "The skin codes are all up here anyway. "
            "Why would you want to... "
            "<br><br>"
            "Oh. "
            "Fine. "
            "I get it. "
            "If you wanted to leave, you could have just closed the page. "
            "You didn't have to intentionally hurt my feelings."
        )

    def help(self):
        response = (
            "Here are some commands that people often use in these sorts of games:"
            "<br>"
            f"{' '.join([x.upper() for x in self.action_map.keys()])}"
            "<br><br>"
            "LOOK is your primary means of gathering information:"
            "<br>> LOOK to see what's in front of you."
            "<br>> LOOK [DIRECTION] to look at a different part of the room."
            "<br>> LOOK [THING] to look at something in your field of view."
            "<br><br>"
            "Use INSPECT to take a closer look at something."
        )

        return response

    def inspect(self):
        if len(self.command) == 1:
            return "What are you tring to INSPECT?"

        action = self.command[0]
        targets = self.command[1:]
        return self.apply_action_to_objects(action, targets)

    def inventory(self):
        return (
            "Why not just root through your pockets yourself? "
            "I promise, it's way easier than me tracing your IP, discovering your location, going all the way to where you are, and shaking you down myself."
        )

        if len(self.command) == 1:
            return "I don't know if I'm even going to use an INVENTORY in this game."

        action = self.command[0]
        targets = self.command[1:]
        return self.apply_action_to_objects(action, targets)

    def look(self):
        """
        The LOOK command is the player's primary vector for gathering information
        about their environment. They can LOOK at look_texts of the direction
        in which they are currently facing, a named direction, or an object in
        the direction in which they are currently facing.
        """
        # Case where the player is looking for the look_text of the current
        # direction in which they're facing.
        if len(self.command) == 1:
            player_direction = self.state["direction"]
            response = VIEWS[player_direction].describe()
            return response

        # Case where the player is looking for the look_text of a specific
        # direction of the attic.
        #
        # A successful execution here updates the player's current view direction.
        targets = self.command[1:]
        if targets[0] in VIEWS.keys():
            target_view = targets[0]
            self.state["direction"] = target_view
            response = VIEWS[target_view].describe()
            return response

        # Otherwise, see if the player has specified an object in view.
        action = self.command[0]
        return self.apply_action_to_objects(action, targets)

    def open(self):
        if len(self.command) == 1:
            return "What do you intend to OPEN?"

        action = self.command[0]
        targets = self.command[1:]
        return self.apply_action_to_objects(action, targets)

    def take(self):
        return "Listen pal, I invited you here to LOOK through my attic and find skin codes. Don't just go around stealing my things. It's rude."

    def use(self):
        if len(self.command) == 1:
            return "What are you trying to USE?"

        action = self.command[0]
        targets = self.command[1:]
        return self.apply_action_to_objects(action, targets)


################################
# SKIN CODE OBJECT DECLARATIONS
################################

skin_codes = [
    "NA23687X8PDRBJHXXV724GUXZ",
    "NA23688YE6TLQLKXAN6Q36ZSJ",
    "NA2368RJALWMQVEBN6J3WHBRB",
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

poro_skin_code = SkinCodeObject(
    name="poro",
    code=skin_codes[1],
    identifiers=[
    ],
    look_text=(
        ""
    ),
    inspect_text=(
    ),
)


################################
# STANDARD OBJECT DECLARATIONS
################################

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
        "vests",
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
    ],
    look_text=(
    ),
    inspect_text=(
    ),
)

wall = AtticObject(
    identifiers=[
    ],
    look_text=(
    ),
    inspect_text=(
    ),
)


################################
# GAME CONTENT COMPILATION
################################

SKIN_CODE_OBJECTS = {
    yugioh_skin_code.name: yugioh_skin_code,
    poro_skin_code.name: poro_skin_code,
}


VIEWS = {
    "north": AtticView(
        look_text="The northern part of the room houses the bare lightbulb responsible for illuminating the attic. The storage in this area seems mostly devoted to outdoorsy things; old pool noodles and life vests lie in a pile on the floor. A ladder stands in the corner. A small shelving unit houses a toolbox and various gardening equipment. What seems like a bicycle is leaning upon the wall.",
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
            "wall": wall,
        },
    ),
    "east": AtticView(
        look_text="The eastern view.",
        objects={
        },
    ),
    "south": AtticView(
        look_text="The southern view.",
        objects={
        },
    ),
    "west": AtticView(
        look_text="The western view. A small stuffed poro rests upon an old rocking chair.",
        objects={
            poro_skin_code.name: poro_skin_code,
        },
    ),
    "up": AtticView(
        look_text="The uppern view. In the dimness of the rafters, a deck of cards can be seen just peeking out over the edge of one of the wooden beams.",
        objects={
            yugioh_skin_code.name: yugioh_skin_code,
        },
    ),
    "down": AtticView(
        look_text="The downern view.",
        objects={
        },
    ),
}
