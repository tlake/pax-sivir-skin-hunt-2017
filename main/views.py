from django.http import JsonResponse
from django.views.generic import View, TemplateView
from django.core.exceptions import ObjectDoesNotExist

import json

from main.models import SkinCode
from main.game import GameHandler
from main.game_content import skin_codes


class MainView(TemplateView):
    template_name = "main.html"


class GameView(View):
    def get(self, request):
        code_objects = SkinCode.objects.all().filter(claimed=0).exclude(name="dubious_chest")
        dubious_code_object = SkinCode.objects.all().filter(claimed=0, name="dubious_chest")

        print(len(code_objects), len(dubious_code_object))
        
        remaining = len(SkinCode.objects.all().filter(claimed=0).exclude(code=skin_codes[-1]))
        exist, code = ("is", "code") if remaining == 1 else ("are", "codes")

        if not dubious_code_object:
            info_line = f"There {exist} {remaining} unclaimed {code} in this attic."
        else:
            info_line = f"There are {remaining} certain unclaimed {code} and 1 dubious unclaimed code in this attic."
        output_text = (
            "-- 2017 PAX WEST SIVIR SKIN HUNT --"
            "<br>"
            "A giveaway adventure by Tanner Lake"
            "<br><br>"
            f"{info_line}"
            "<br><br>"
            "YOU AWAKE to find yourself in a dark room. "
            "No, not Mr. John Robertson's dark room, although I encourage you to find him on YouTube. "
            "This is an attic. "
            "It's dry and dusty and admittedly not all that dark, because a single bare lightbulb is bathing the attic in an orangey low-wattage radiance. "
            "<br><br>"
            "You may wish to LOOK around, or ask for HELP."
            "<br><br>"
            "You are facing north. Command?"
        )

        data = {
            "playerState": {
                "direction": "north",
                "grue_chance": 0,
            },
            "outputText": output_text,
        }

        return JsonResponse(data)

    def post(self, request):
        data = json.loads(request.body)
        handler = GameHandler(data)
        response = handler.run()

        return_data = {
            "playerState": handler.state,
            "outputText": response,
        }

        return JsonResponse(return_data)
