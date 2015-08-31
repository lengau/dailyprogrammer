#!/usr/bin/env python3
# Daily Programmer #230, easy edition: Searching in JSON
# https://redd.it/3j3pvm

import json
import timeit

TEST_INPUT_1 = """\
{"name": "William Shakespeare", "wife": {"birthYear": 1555, "deathYear": 
"Fun fact, she's a vampire", "name": "Anne Hathaway", "dead": false}, 
"favoriteWebsites": ["dailysonneter", "dailyprogrammer", 
"vine (he's way into 6-second cat videos)"], "dead": true, "birthYear": 1564, 
"facebookProfile": null, "selectedWorks": [{"written": 1606, "name": 
"The Tragedy of Macbeth", "isItAwesome": true}, {"written": 1608, "name": 
"Coriolanus", "isItAwesome": "It's alright, but kinda fascist-y"}], "deathYear":
 1616}"""
TEST_OUTPUT_1 = 'favoriteWebsites -> 1'
TEST_INPUT_2 = """\
{"dlpgcack": false, "indwqahe": null, "caki": {"vvczskh": null, "tczqyzn": 
false, "qymizftua": "jfx", "cyd": {"qembsejm": [null, "dailyprogrammer", null], 
"qtcgujuki": 79, "ptlwe": "lrvogzcpw", "jivdwnqi": null, "nzjlfax": "xaiuf", 
"cqajfbn": true}, "kbttv": "dapsvkdnxm", "gcfv": 43.25503357696589}, "cfqnknrm": 
null, "dtqx": "psuyc", "zkhreog": [null, {"txrhgu": false, "qkhe": false, 
"oqlzgmtmx": "xndcy", "khuwjmktox": 48, "yoe": true, "xode": "hzxfgvw", 
"cgsciipn": 20.075297532268902}, "hducqtvon", false, [null, 76.8463226047357, 
"qctvnvo", null], [null, {"nlp": false, "xebvtnvwbb": null, "uhfikxc": null, 
"eekejwjbe": false, "jmrkaqky": null, "oeyystp": false}, [null, 10, "nyzfhaps", 
71, null], 40, null, 13.737832677566875], [true, 80, 20, {"weynlgnfro":
40.25989193717965, "ggsirrt": 17, "ztvbcpsba": 12, "mljfh": false, "lihndukg": 
"bzebyljg", "pllpche": null}, null, [true, false, 52.532666161803895, "mkmqrhg",
"kgdqstfn", null, "szse"], null, {"qkhfufrgac": "vpmiicarn", "hguztz": 
"ocbmzpzon", "wprnlua": null}], {"drnj": [null, false], "jkjzvjuiw": false, 
"oupsmgjd": false, "kcwjy": null}]}"""
TEST_OUTPUT_2 = 'caki -> cyd -> qembsejm -> 1'

TEST_VALUES = {
    TEST_INPUT_1: TEST_OUTPUT_1,
    TEST_INPUT_2: TEST_OUTPUT_2
}

TEST_TIMES = 100

class JsonFinder(object):
    
    def __init__(self, json_string, search_term='dailyprogrammer'):
        self.__json_object = json.loads(json_string)
        self.search_term = search_term
        
    def find(self):
        return self.__search(self.__json_object)
        
    def __search(self, node):
        if isinstance(node, dict):
            for key in node:
                if node[key] == self.search_term:
                    return key
                if isinstance(node[key], (dict, list)):
                    result = self.__search(node[key])
                    if isinstance(result, str):
                        return '%s -> %s' % (key, result)
        elif isinstance(node, list):
            if self.search_term in node:
                return str(node.index(self.search_term))
            for item in node:
                result = self.__search(item)
                if isinstance(result, str):
                    return '%s -> %s' % (node.index(item), result)
                    
for key in TEST_VALUES:
    finder = JsonFinder(key)
    output = finder.find()
    print('Expected: %s' % TEST_VALUES[key])
    print('Actual:   %s' % output)
    assert output == TEST_VALUES[key]
    
for challenge in range(1,3):
    print('Challenge %d:' % challenge)
    with open('challenge%d.txt' % challenge) as challenge_file:
        challenge_data = challenge_file.read()
    finder = JsonFinder(challenge_data)
    print('Result: %s' % finder.find())
    time = timeit.timeit(
        stmt='finder.find()',
        setup='from __main__ import JsonFinder,challenge_data; finder = JsonFinder(challenge_data)',
        number=TEST_TIMES
        )
    print('Average time in seconds: %f' % (time/TEST_TIMES))
