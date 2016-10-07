# One-directional Plex-to-TVMaze watch status sync

This script is to be used in conjunction with [PlexPy](https://github.com/JonnyWong16/plexpy), please see their page for setup instructions.

A Premium account from [www.tvmaze.com](http://www.tvmaze.com) is also required.

Please note that PlexPy currently only supports custom notifications when actually watching a TV show, so **this script will not run when manually marking a show as watched with Plex.**

**Requires:** `pytvmaze`, `fuzzywuzzy`

- `pip install --upgrade pytvmaze`
- `pip install --upgrade fuzzywuzzy`

## Instructions
1. Download the `mark_watched_tvmaze.py` script from this repo into the folder of your choosing
- Modify the script by entering your TVMaze premium credentials and Plex username at the top
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

You can test this out by scrolling to the near-end of an episode on Plex and letting it play out.  The exact amount of time left you need to watch depends on your **Watched Percent** setting in PlexPy and the length of the show, but I find that watching the last 2 minutes with **Watched Percent** at 95 works for both 20 and 40 minute episodes.  Once you've done this go to the corresponding episode on TVMaze and see if it has become "Watched".  Enjoy!
