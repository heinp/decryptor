from gensim.models import Word2Vec, KeyedVectors
import random
# import argparse


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
        # import pprint
        # pp = pprint.PrettyPrinter()
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



    return results


# downloaded from https://wikipedia2vec.github.io/wikipedia2vec/pretrained/
ger_path = "models/dewiki_20180420_300d.txt"
eng_path = "models/enwiki_20180420_300d.txt"

print("Loading VSM...")
model = KeyedVectors.load_word2vec_format(eng_path, binary=False, limit=50000)
print("Done.")

# solution: 1: "china", 2: "bear", 3: "table", 4: "car"
digits = {1: ["bamboo", "asia", "country"],
          2: ["brown", "grizzly", "animal"],
          3: ["chair", "coffee", "furniture"],
          4: ["fast", "road", "vehicle"]}

test = ["wheel", "communism", "stool"]

g = guess(digits, test)

for d in g:
    print(d["prediction"])