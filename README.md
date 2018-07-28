# Journeymap Grid Creator
A quick script I whipped up to make a grid from a bottom-left starting waypoint  
*keyword "whipped" up ;P - alot of stuff will probably break it, most notably negative offsets to flip the grid's location relative to the source point - completely untested.*

# Usage
***All of this can be done while the game is running.***  
  
- While ingame, place a waypoint at the **top left** of where you want your grid to be located, name it something distinguishable from the other waypoints.
  >The parameters you provide for the grid will expand from the right and downward from this point. (See notes)  
  
- Put the python script file in the directory of your game's server or world's waypoints. This is usually;  
`<mc-instance>/journeymap/data/<sp-or-mp>/<server-or-world-name>/waypoints`  
  
- Running the script will give you a list of json files in that directory, each one is a waypoint. Pick the one you created earlier.
- Now easy as, enter the dimensions of the grid.  
  
***You must relog for the waypoints to take effect once they are generated!***

# Notes
- Use negative values on either one of the offsets to flip the direction the grid expands in from the source point (UNTESTED).  
- The colour of the origin waypoint is inherited by all the grid points.
- It's way easier to delete the grid from the file explorer rather than ingame due to the sheer amount of files.
  
# Parameters
  
| Prompt | Usage |
| --- | --- |
| **X Offset** | How much horizontal space there is between each point |
| **Z Offset** | How much vertical space there is between each point |
| **Grid Width** | How many horizontal points the grid has |
| **Grid Height** | How many vertical points the grid has |
