# anicon
Add cover art from MAL as folder icons to your anime collection.

### How do I use this?

- Download the executable from [here](https://github.com/notdedsec/anicon/releases/download/v1.0/anicon.exe)
- Run it in your anime folder
- Choose when you're asked to
- Repeat till all folders are processed

### That's it? Sounds like a lot of choosing :v

Yes. It is.
Though there are some additional features to help you with this:

#### AutoMode
If enabled, the script will automatically select the first item from the search results. This works fine in most cases but in case you have seperate folders for different seasons for the same anime, it will end up applying the same cover art of to all of those folders. It will be decided on the basis of which season has the highest score.

#### Blank Input
If you're not using AutoMode, you can give a blank input when you're asked to choose and it'll pick the first item from search results. This way, you can save a few keystrokes, just hitting the Enter Key instead of typing '1' and then Enter. The anime you're looking for is most often the first one in the results.

### Okay so i did everything, but the icons aren't showing up. (*panicks*)
Your PC may take some time to index those icons. They should show up in 2 to 5 minutes. I guess.

### Alright. It works but I'm curious as to how?
It, uhhh
- Gets the Anime Name from the Folder Name
- Searches that name on MAL with Jikan API
- Asks you to choose the anime from results
- Gets the artwork and converts it into an icon
- Makes a `desktop.ini` file which sets the folder icon.

### I don't like these icons. How do i remove them?
To remove the cover icon from a folder, you just need to delete the `.ico` and `desktop.ini ` file from the folder. These files are hidden so make sure you have `Show Hidden Items` option ticked. You can just search and delete them all if you wanna batch remove all icons. But why would you wanna do that anyway?

### Any Tips or Suggestions?
Yeah, the most efficient way to use this (imo) would be to:
- Run it in AutoMode first so all folders are processed
- Move out the incorrectly tagged folders and delete their icons
- Run it in ManualMode and choose the correct results

### I was promised memes. Gib memes.
Alright here you go.

![meme](https://i.imgur.com/BXX93Rs.jpg)