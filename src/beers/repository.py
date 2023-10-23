from .models import Beer

class BeerRepo:
    def __init__(self) -> None:
        pass

    def counts(self):
        try:
            beers: list[Beer] = list(Beer.query.all())
            len(beers)
            return len(beers)
        except:
            return 0

BEER_REPOSITORY = BeerRepo()