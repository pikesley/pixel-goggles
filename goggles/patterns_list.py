from patterns.dancer import dancer
from patterns.pendulum import pendulum
from patterns.pulse import pulse
from patterns.race import race
from patterns.rainbow import rainbow
from patterns.random_dots import random_dots
from patterns.smooth import smooth
from patterns.snake import snake
from patterns.sparkle import sparkle
from patterns.spots import spots
from patterns.sunburst import sunburst
from patterns.tilter import tilter
from patterns.tilting_rainbow import tilting_rainbow
from patterns.wave import wave
from patterns.wings import wings
from patterns.wiper import wiper

patterns = [
    dancer,
    pulse,
    race,
    rainbow,
    random_dots,
    smooth,
    snake,
    sparkle,
    spots,
    wave,
    wings,
    wiper,
]

spare_patterns = [
    tilter,
    pendulum,
    sunburst,
    tilting_rainbow,
]


def pattern_by_name(name):
    """Get the index for an entry by its name."""
    names = [item.__name__ for item in patterns]
    try:
        return names.index(name)
    except ValueError:
        return 0
