from main.game_logic import ActionEnabledObject
from main.game_content import VIEWS, SKIN_CODE_OBJECTS

from random import randint


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
