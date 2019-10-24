"""
This module controls the game and has all attributes refered to the game.

Lorem Ipsum.
"""
import pygame
import settings
import random

TILE_WIDTH = (settings.SCREEN_SIZE[0]-1)/settings.TABLE_SIZE[0]
TILE_HEIGHT = (settings.SCREEN_SIZE[1]-1)/settings.TABLE_SIZE[1]
NUMBER_OF_TILES = settings.TABLE_SIZE[0]*settings.TABLE_SIZE[1]


class Tile():
    """Represents a tile in the map."""

    def __init__(self, gt=None):
        """Docsstring."""
        size = (
            TILE_WIDTH,
            TILE_HEIGHT)
        self.surface = pygame.Surface(size)
        self.groundType = gt
        self.surface.fill(settings.GROUND_TYPE[self.groundType])
        self.gameObject = None
        self.speedMod = None

    def get_tile_size(self):
        """Docstring."""
        return size

    def update(self):
        """Docs."""
        self.surface.fill(settings.GROUND_TYPE[self.groundType])

    def change_color(self):
        """Docstring."""
        if self.groundType == 'rock':
            self.groundType = 'water'
        elif self.groundType == 'water':
            self.groundType = 'grass'
        elif self.groundType == 'grass':
            self.groundType = 'rock'


class Mapper():
    """Builds the entire map."""

    def __init__(self, size=settings.SCREEN_SIZE):
        """Docsstring."""
        self.background = pygame.Surface(size)
        self._drawBgLines()
        self.slots = []
        for slot in range(0, NUMBER_OF_TILES):
            self.slots.append(Tile(random.choice(['grass', 'rock', 'water'])))

    def _pixels_to_index(self, pos):
        """DOCS."""
        x_coordinate = int(pos[0] / TILE_WIDTH)
        y_coordinate = int(pos[1] / TILE_HEIGHT)
        index = x_coordinate + y_coordinate * settings.TABLE_SIZE[0]
        return index

    def _coordinates_to_pixels(self, x, y):
        """Docs."""
        x_pixels = x * TILE_WIDTH
        y_pixels = y * TILE_HEIGHT
        return (x_pixels, y_pixels)

    def _drawBgLines(self):
        """Draw the lines to make visual tile slots."""
        for x in range(0, settings.TABLE_SIZE[0]):
            if not x > settings.TABLE_SIZE[1]:
                pygame.draw.line(
                    self.background,
                    pygame.Color(
                        settings.COLORS['bg-gray'][0],
                        settings.COLORS['bg-gray'][1],
                        settings.COLORS['bg-gray'][2]),
                    (0, TILE_HEIGHT*x),
                    (settings.SCREEN_SIZE[0] - 1, TILE_HEIGHT*x))
            pygame.draw.line(
                self.background,
                pygame.Color(
                    settings.COLORS['bg-gray'][0],
                    settings.COLORS['bg-gray'][1],
                    settings.COLORS['bg-gray'][2]),
                (TILE_WIDTH*x, 0),
                (TILE_WIDTH*x, settings.SCREEN_SIZE[1]))
        pygame.draw.lines(
            self.background,
            pygame.Color(
                settings.COLORS['bg-gray'][0],
                settings.COLORS['bg-gray'][1],
                settings.COLORS['bg-gray'][2]),
            False,
            ((0, settings.SCREEN_SIZE[1] - 1),
                (settings.SCREEN_SIZE[0] - 1, settings.SCREEN_SIZE[1] - 1),
                (settings.SCREEN_SIZE[0] - 1, 0)))

    def _draw_tiles(self):
        """Docs."""
        for index in range(0, len(self.slots)):
            coordinatess = self._coordinates_to_pixels(
                index % settings.TABLE_SIZE[0],
                int(index / settings.TABLE_SIZE[0]))
            self.background.blit(
                self.slots[index].surface,
                (coordinatess[0], coordinatess[1]))

    def get_surface(self):
        """Get surface."""
        return self.background

    def change_tile_color(self, pos):
        """DOCS."""
        # ex pos. (425, 129)
        index = self._pixels_to_index(pos)
        self.slots[index].change_color()

    def update(self):
        """Docs."""
        self.background.fill(settings.COLORS['black'])
        for slot in self.slots:
            slot.update()
        self._draw_tiles()
        self._drawBgLines()


class GameMode():
    """Class manages game rules and flow."""

    def __init__(self):
        """Docstring."""
        self.world = Mapper()
