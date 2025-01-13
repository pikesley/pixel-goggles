from patterns.dancer import dancer
from patterns.pendulum import pendulum
from patterns.pulse import pulse
from patterns.race import race
from patterns.rainbow import rainbow
from patterns.rainbow_tilt import rainbow_tilt
from patterns.random_dots import random_dots
from patterns.smooth import smooth
from patterns.snake import snake
from patterns.sparkle import sparkle
from patterns.spots import spots
from patterns.sunburst import sunburst
from patterns.tilter import tilter
from patterns.wave import wave
from patterns.wings import wings
from patterns.wiper import wiper

patterns = [
    wiper,
    wings,
    wave,
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

spare_patterns = [
    pendulum,
    rainbow_tilt,
    spots,
    sunburst,
]


def pattern_by_name(name):
    """Get the index for an entry by its name."""
    names = [item.__name__ for item in patterns]
    try:
        return names.index(name)
    except ValueError:
        return 0
