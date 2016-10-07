# One-directional Plex-to-TVMaze watch status sync

This script is to be used in conjunction with [PlexPy](https://github.com/JonnyWong16/plexpy), please see their page for setup instructions.

Please note that PlexPy currently only supports custom notifications when actually watching a TV show, so **this script will not run when manually marking a show as watched with Plex.**

**Requires:** `pytvmaze`, `fuzzywuzzy`

- `pip install --upgrade pytvmaze`
- `pip install --upgrade fuzzywuzzy`

## Instructions
1. Download the `mark_watched_tvmaze.py` script from this repo into the folder of your choosing
- Ensure PlexPy is running
- Launch the PlexPy web interface by typing `http://localhost:8181/` into your browser
- Go to **Settings > Notifications**
- Check **Enable TV Show Notifications**
- Change the **Watched Percent** value if desired, I find 95 to be suitable for TV shows
- Scroll all the way down to **Script**.  Expand **Script** and paste the following into the **Script Arguments** field: `{show_name} {title} {username} {thetvdb_id} {imdb_id} {air_date} {season_num} {episode_num}`
- Click **Save** and then **Restart**
- Once restarted, go to **Settings > Notifaction Agents**
- Click the bell next to **Scripts** so that it becomes highlighted
- Click the gear next to **Scripts** to edit its Settings
- Enter the path location where you put the `mark_watched_tvmaze.py` script in the **Script Folder** field
- Scroll down to **Watched**, click the dropdown menu and select `mark_watched_tvmaze.py`
- Click **Save**
