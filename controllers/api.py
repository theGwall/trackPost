import random

# Mocks implementation.
def get_tracks():
    start_idx = int(request.vars.start_idx) if request.vars.start_idx is not None else 0
    end_idx = int(request.vars.end_idx) if request.vars.end_idx is not None else 0
    # We just generate a lot of of data.
    tracks = []
    for i in range(start_idx, end_idx):
        t = dict(
            artist = random.choice(['IU', 'Ailee', 'T-ara', 'Mamamoo']),
            album = random.choice(['Modern times', 'Melting', 'Absolute']),
            title = random.choice(['Falling U', 'TTL', 'Piano Man']),
            duration = random.uniform(3 * 60, 4 * 60),
            rating = random.randint(1, 5),
            num_plays = random.randing(0, 100),
        )
    has_more = True
    logged_in = False
    return response.json(dict(
        tracks=tracks,
        logged_in=logged_in,
        has_more=has_more,
    ))
