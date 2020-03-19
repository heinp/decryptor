from gensim.models import Word2Vec, KeyedVectors
import random
# import argparse


def guess(digits, words):
    global model
    results = []
    for word in words:
        result = {"word":word, "scores": []}
        for d, l in digits.items():
            if len(l) > 0:
                similarities = [model.wv.similarity(word, w) for w in l]
                result["scores"].append((d, sum(similarities)/len(similarities)))
            else:
                result["scores"].append((d, 0))
        result["scores"].sort(key=lambda s: s[1], reverse=True)
        result["prediction"] = result["scores"][0][0]
        result["choice"] = 0
        results.append(result)

    # find optimal solution
    # as long as answers are not destibuted, keep on optimizing
    c = 0
    while len(set(r["prediction"] for r in results)) != 3 and c < 3:
        c += 1
        for i1, r1 in enumerate(results):
            for i2, r2 in enumerate(results[0:i1] + results[i1:]):
                if r1["prediction"] == r2["prediction"]:
                    if r1["choice"] < 3:
                        # calculate "distance" between next best score and actual score
                        delta1 = r1["scores"][r1["choice"] + 1][1] - r1["scores"][r1["choice"]]
                    else:
                        delta1 = 100  # if there is no next best, use huge distance
                    if r2["choice"] < 3:
                        delta2 = r2["scores"][r2["choice"] + 1][1] - r2["scores"][r2["choice"]]
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
                    results[i]["prediction"] = results[i]["scores"][results[i]["choice"]][0]

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

test = ["wheel", "communism", "communism"]

g = guess(digits, test)

for d in g:
    print(d["prediction"])