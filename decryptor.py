from gensim.models import KeyedVectors
from itertools import combinations, permutations
import pprint
import random
import argparse

pp = pprint.PrettyPrinter()


def guess(digits, words):
    global model
    results = []
    for word in words:
        # create dict for the results where:
        # "word" -> the word as string
        # "scores" -> scores as a dict with possible digits as key and their score as value
        # "ranking" -> the ranked digits
        result = {"word": word, "scores": {}, "ranking": []}
        for dig, l in digits.items():
            if len(l) > 0:
                # calculate cosine similarities to each existing word
                similarities = [model.wv.similarity(word, w) for w in l]
                # calc avg and store digit and its score
                result["scores"][dig] = sum(similarities) / len(similarities)
                result["ranking"].append(dig)
            else:  # handle empty classes
                result["scores"][dig] = 0
                result["ranking"].append(dig)

        # sort the ranking list with the scores from the scores dict
        result["ranking"].sort(key=lambda e: result["scores"][e], reverse=True)
        result["prediction"] = result["ranking"][0]
        result["choice"] = 0  # index to show which score is used as prediction, might change during optimization
        results.append(result)
    # pp.pprint(results)

    # find optimal solution
    # not using "clever" optimization algorithm because it doesnt work and its only 24 options
    # as long as answers are not destibuted, keep on optimizing
    """ 
    c = 0
    while len(set(r["prediction"] for r in results)) != 3 and c < 3:
        c += 1
        for i1, r1 in enumerate(results):
            for i2, r2 in enumerate(results[0:i1] + results[i1:]):
                if r1["prediction"] == r2["prediction"]:
                    if r1["choice"] < 3:
                        # calculate "distance" between next best score and actual score
                        # print("r1:", )
                        delta1 = r1["scores"][r1["choice"] + 1][1] - r1["scores"][r1["choice"]][1]
                    else:
                        delta1 = 100  # if there is no next best, use huge distance
                    if r2["choice"] < 3:
                        delta2 = r2["scores"][r2["choice"] + 1][1] - r2["scores"][r2["choice"]][1]
                    else:
                        delta2 = 100

                    # search smaller distance and use next best choice there
                    if delta1 < delta2:
                        i = i1
                    elif delta2 < delta1:
                        i = i2
                    else:
                        i = random.choice([i1, i2])  # use random choice if both distances are equal

                    results[i]["choice"] += 1
                    results[i]["prediction"] = results[i]["scores"][results[i]["choice"]][0]"""

    # wood hammer optimization algorithm
    if len(set(r["prediction"] for r in results)) != 3:
        # check the average score of all permutations and find best one
        print("Not the best solution for every word possible.")
        best_avg_score = 0
        best_perm = random.sample([1,2,3,4], k=3)  # initialize best permutation randomly, if no best option is found
        for comb in combinations([1,2,3,4], 3):
            for perm in permutations(comb):
                sum_of_scores = 0
                for result, dig in zip(results, perm):
                    sum_of_scores += result["scores"][dig]
                avg_score = sum_of_scores / 3
                if avg_score > best_avg_score:
                    best_perm = perm
                    best_avg_score = avg_score
        # update results
        for ri, best_dig in zip(range(3), best_perm):
            results[ri]["prediction"] = best_dig
            results[ri]["choice"] = results[ri]["ranking"].index(best_dig)
    pp.pprint(results)
    return results


# downloaded from https://wikipedia2vec.github.io/wikipedia2vec/pretrained/
ger_path = "models/dewiki_20180420_300d.txt"
eng_path = "models/enwiki_20180420_300d.txt"

parser = argparse.ArgumentParser(description="Computer player for the game 'Decrypto'")
parser.add_argument("--german", "-g", action="store_true", help="Use German version (default: English)")
parser.add_argument("--example", "-e", action="store_true", help="Use example Data (default: play")
args = parser.parse_args()



print("Loading VSM...")
if args["german"]:
    path = ger_path
else:
    path = eng_path
model = KeyedVectors.load_word2vec_format(path, binary=False, limit=50000)
print("Done.")

if args["example"]:
    # Example data for debugging
    # solution: 1: "china", 2: "bear", 3: "table", 4: "car"
    digits = {1: ["bamboo", "asia", "country"],
              2: ["brown", "grizzly", "animal"],
              3: ["chair", "coffee", "furniture"],
              4: ["fast", "road", "vehicle"]}

    test = ["rice", "claw", "stool"]

    g = guess(digits, test)

    for d in g:
        print(d["prediction"])
    quit()



# initialize data_structures
digits = {1: [], 2: [], 3: [], 4: []}


