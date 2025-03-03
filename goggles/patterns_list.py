from patterns.dancer import dancer
from patterns.larson import larson
from patterns.pulse import pulse
from patterns.race import race
from patterns.rainbow import rainbow
from patterns.random_dots import random_dots
from patterns.smooth import smooth
from patterns.snake import snake
from patterns.sparkle import sparkle
from patterns.tilter import tilter
from patterns.wings import wings
from patterns.wiper import wiper

patterns = [
    wiper,
    wings,
    larson,
    tilter,
    sparkle,
    snake,
    smooth,
    random_dots,
    rainbow,
    race,
    pulse,
    dancer,
]


def pattern_by_name(name):
    """Get the index for an entry by its name."""
    names = [item.__name__ for item in patterns]
    try:
        return names.index(name)
    except ValueError:
        return 0
