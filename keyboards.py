import json

input_search_data = json.dumps({
    "inline": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": {"button": "search_init_button"},
                    "label": "Ввести данные поиска"
                }
            },
            {
                "action": {
                    "type": "text",
                    "payload": {"button": "bay_button"},
                    "label": "Пока"
                }
            }
        ]
    ]
})

start_search = json.dumps({"inline": True,
                           "buttons": [
                               [
                                   {
                                       "action": {
                                           "type": "text",
                                           "label": "Найти пару"
                                       }
                                   },
                               ]
                           ]
                           })

next_keyboard = json.dumps({
    "inline": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": {"button": "add_to_favor"},
                    "label": "Добавить в избранное"
                }
            },
            {
                "action": {
                    "type": "text",
                    "payload": {"button": "next_button"},
                    "label": "Дальше"
                }
            },
            {
                "action": {
                    "type": "text",
                    "payload": {"button": "show_favor"},
                    "label": "Показать избранных"
                }
            },

        ]
    ]
})

favor_keyboard = json.dumps({
    "inline": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": {"button": "next_button"},
                    "label": "Дальше"
                }
            },
            {
                "action": {
                    "type": "text",
                    "payload": {"button": "show_favor"},
                    "label": "Показать избранных"
                }
            },

        ]
    ]
})

last_favor = json.dumps({
    "inline": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "payload": {"button": "show_favor"},
                    "label": "Показать избранных"
                }
            },
        ]
    ]
})
