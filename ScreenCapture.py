import pygame
import imageio
import os
import numpy as np
import time

import DynamicMaze
import Game

fps = 70

video_writer = imageio.get_writer('VideoFiles/NewFile.mp4', fps=fps)
d = ["D", "R", "U", "L"]

def save_frame(screen):
    frame = pygame.surfarray.array3d(screen)  # Capture screen as 3D array
    frame = np.transpose(frame, (1, 0, 2))  # Transpose to (height, width, color channels)
    video_writer.append_data(frame)

def rename_or_delete_file():
    file_name = input("Enter a file name (or press Enter to delete the file): ").strip()
    source_path = 'VideoFiles/NewFile.mp4'

    if file_name:
        destination_path = f'VideoFiles/{file_name}.mp4'
        os.rename(source_path, destination_path)
        print(f"File renamed to {destination_path}")
    else:
        os.remove(source_path)
        print("File deleted.")

def first_impression_room():
    maze = DynamicMaze.get_plain_map(2, 'walls')
    openings = [('', 2), ('', 3), ('L', 2), ('U', 3), ('UL', 0), ('U', 2), ('UU', 2)]
    for tile, index in openings:
        maze.place_wall_or_opening(tile, index, 'opening')
    maze.place_wall_or_opening('UU', 1, 'wall')

    return maze


def second_impression_room():
    maze = DynamicMaze.get_plain_map(2, 'walls+')
    openings = [('U', 'L'), ('UL', 'D'), ('U', 'R'), ('L', 'U'), ('L', 'D'), ('LD', 'R'),
                ('D', 'R'), ('D', 'L'), ('DR', 'U'), ('R', 'D'), ('R', 'U'), ('RU', 'L')]
    for tile, direction in openings:
        maze.place_wall_or_opening(tile, d.index(direction), 'opening')

    walls = [('UL', 'U'), ('UL', 'L'), ('LU', 'U'), ('LU', 'L'), ('LD', 'L'), ('LD', 'D'),
             ('DL', 'L'), ('DL', 'D'), ('DR', 'D'), ('DR', 'R'), ('RD', 'D'), ('RD', 'R'),
             ('RU', 'R'), ('RU', 'U'), ('UR', 'R'), ('UR', 'U')]

    for tile, direction in walls:
        maze.place_wall_or_opening(tile, d.index(direction), 'wall')

    return maze


if __name__ == '__main__':
    dynamic_maze = DynamicMaze.DynamicMaze()
    Game.run_game(default_render='2D', maze=dynamic_maze, include_mini_map=False, mini_map_generates_tiles=False,
                  screen_capture=True)

    video_writer.close()
    time.sleep(1)
    #rename_or_delete_file()
