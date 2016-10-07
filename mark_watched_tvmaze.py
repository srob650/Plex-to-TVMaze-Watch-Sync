import sys
import pytvmaze
from fuzzywuzzy import process


# TVMaze premium account required for API key
tvm = pytvmaze.TVMaze('TVMAZE_USERNAME', 'TVMAZE_API_KEY')
plex_username = 'PLEX_USERNAME'


# PlexPy arguments
show_name = sys.argv[1]
title = sys.argv[2]
username = sys.argv[3]
tvdb_id = sys.argv[4]
imdb_id = sys.argv[5]
air_date = sys.argv[6]
season_num = sys.argv[7]
episode_num = sys.argv[8]


# Get TVMaze episode using season and episode numbers
def get_episode(maze_id, season_num, episode_num):
    if not maze_id or not season_num or not episode_num:
        return None

    try:
        episode = pytvmaze.episode_by_number(maze_id, season_num, episode_num)
    except pytvmaze.EpisodeNotFound:
        return None

    return episode


# Get TVMaze episode using airdate and title
def get_episode_by_date(maze_id, air_date, title):
    if not maze_id or not air_date or not title:
        return None

    try:
        episodes_by_date = pytvmaze.episodes_by_date(maze_id, air_date)
    except pytvmaze.NoEpisodesByAirdate:
        return None

    titles = {}
    for episode in episodes_by_date:
        titles[episode.title] = episode

    closest_match = process.extractOne(title, titles.keys())
    if not closest_match[1] >= 80:
        return None

    return titles[closest_match[0]]


def main():
    # Only mark watched if YOU watched it.  Helpful when you share your Plex library with others
    if not username == plex_username:
        sys.exit()

    # Attempt to get show data from TVMaze
    show = tvm.get_show(show_name=show_name, tvdb_id=tvdb_id, imdb_id=imdb_id)
    if not show:
        sys.exit()

    maze_id = show.maze_id
    episode = get_episode(maze_id, season_num, episode_num)
    if not episode:
        episode = get_episode_by_date(maze_id, air_date, title)

    if not episode:
        sys.exit()

    # Mark episode watched on TVMaze
    tvm.mark_episode(episode.maze_id, 'watched')

if __name__ == '__main__':
    main()
