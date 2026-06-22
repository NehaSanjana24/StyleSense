from utils.data_loader import load_outfits

OUTFITS = load_outfits()


def recommend(gender, style, occasion, budget):

    matches = []

    for outfit in OUTFITS:

        score = 0

        if outfit["gender"] == gender:
            score += 30

        if outfit["style"] == style:
            score += 30

        if outfit["occasion"] == occasion:
            score += 25

        if outfit["budget"] == budget:
            score += 15

        matches.append((score, outfit))

    matches.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return matches[:3]