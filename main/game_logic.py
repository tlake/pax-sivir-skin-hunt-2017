from django.core.exceptions import ObjectDoesNotExist

from main.models import SkinCode

from random import randint


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

    def discovery(self, state):
        instance = SkinCode.objects.get(name=self.name)
        if instance.claimed:
            message = (
                "<br><br>"
                "...Unfortunately, somebody else has beaten you to it. "
                f"The code has been scratched off, and somebody has scrawled '{instance.summoner_name} wuz heer, get gud scrub' in heavy marker."
            )
            return (message, state)

        state["skin_code"] = self.name
        state["activation_step"] = "confirm_activation"
        message = (
            "<br><br>"
            "Enter YES to begin the activation process, or anything else to abort."
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


class InspectSkinCodeObject(SkinCodeObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def inspect(self, state):
        response, new_state = self.discovery(state)
        return ((self.open_text + response), new_state)


class OpenSkinCodeObject(SkinCodeObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def open(self, state):
        response, new_state = self.discovery(state)
        return ((self.open_text + response), new_state)


class UseSkinCodeObject(SkinCodeObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def use(self, state):
        response, new_state = self.discovery(state)
        return ((self.use_text + response), new_state)


class YuGiOhSkinCodeObject(SkinCodeObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def use(self, state):
        return self.inspect(state)

    def inspect(self, state):
        return self.discovery(state)

    def discovery(self, state):
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


class ChestSkinCodeObject(OpenSkinCodeObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def discovery(self, state):
        instance = SkinCode.objects.get(name=self.name)
        if instance.claimed:
            message = (
                "<br><br>"
                "...Unfortunately, somebody else has beaten you to it. "
                f"The code has been scratched off, and somebody has scrawled '{instance.summoner_name} wuz heer, get gud scrub' in heavy marker. "
                f"Although, this particular skin code may or may not have been claimed before I put it into the game, so maybe {instance.summoner_name} came away with a big fat nothing."
            )
            return (message, state)

        state["skin_code"] = self.name
        state["activation_step"] = "confirm_activation"
        message = (
            " BE WARNED, however: "
            "I don't know if this skin is valid, so you're sort of rolling the dice on this one. "
            "You're welcome to keep hunting if this one doesn't work out!"
            "<br><br>"
            "Enter YES to begin the activation process, or anything else to abort."
        )
        return (message, state)
