import json

test = '{"button":"search_init_button"}'
test2 = json.loads(test)
print(test2['button'])