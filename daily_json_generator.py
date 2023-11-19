import json
from random import randint


if __name__ == "__main__":
    count = 1000
    seeds = []
    for i in range(count):
        seed = 0
        for j in range(10):
            seed += pow(10, j) * randint(1,9)
        seeds.append(seed)

    data = {
        "version": "0.2.1",
        "start_date": {
            "month": 11,
            "day": 18,
            "year": 2023,
        },
        "seeds": seeds,
    }

    with open('dailies.json', 'w') as fp:
        json.dump(data, fp)
