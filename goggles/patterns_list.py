from patterns.flying_wave import flying_wave
from patterns.pendulum import pendulum
from patterns.pulse import pulse
from patterns.race import race
from patterns.rainbow import rainbow
from patterns.random_dance import random_dance
from patterns.responder import responder
from patterns.riser import riser
from patterns.snake import snake
from patterns.sparkle import sparkle
from patterns.spots import spots
from patterns.tilter import tilter
from patterns.tilting_rainbow import tilting_rainbow
from patterns.wave import wave

patterns = [
    riser,
    wave,
    random_dance,
    spots,
    sparkle,
    snake,
    rainbow,
    race,
    pulse,
    flying_wave,
]

spare_patterns = [
    responder,
    pendulum,
    tilter,
    tilting_rainbow,
]


def pattern_by_name(name):
    """Get the index for an entry by its name."""
    names = [item.__name__ for item in patterns]
    try:
        return names.index(name)
    except ValueError:
        return 0
