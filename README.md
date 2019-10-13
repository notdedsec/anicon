

# Anicon
Add cover art from MAL as folder icons to your anime collection.

### How do I use this?

- Download the executable from [here](https://github.com/notdedsec/anicon/releases)
- Run it in your anime folder
- Choose when you're asked to
- Repeat till all folders are processed

### That's it? Sounds like a lot of choosing :v

Yes. It is.
Though there are some additional features to help you with this:

#### AutoMode
If enabled, the script will automatically select the first item from the search results. This works fine in most cases but in case you have separate folders for different seasons for the same anime, it will end up applying the same cover art of to all of those folders. It will be decided on the basis of which season has the highest score.

#### Blank Input
If you're not using AutoMode, you can give a blank input when you're asked to choose and it'll pick the first item from search results. This way, you can save a few keystrokes, just hitting the Enter key instead of typing '1' and then Enter. The anime you're looking for is most often the first one in the results.

### Okay so I did everything, but the icons aren't showing up. (*panicks*)
Your PC may take some time to index those icons. They should show up in 2 to 5 minutes. I guess.

### I don't want to wait 
Uhh, follow these steps (they work in most of the cases, if they don't you'll just have to wait).
-  Make sure you have 'show hidden files and folders' option enabled.
 - Go inside the folder where '**desktop.ini**' and icon files are present.  Locate the '**desktop.ini**' file and delete it (no need to permanently delete). 
 - Move to the parent directory (the folder that contains this folder). 
 - Now, Undo the deletion (Ctrl + Z) and refresh the folder. What this does is make Windows realize that the folder needs an icon.
 - This method usually works, but in case it doesn't, all you can do is wait. Or probably restart the pc.

### The folder had an icon but then I compressed it (or something) and then it disappeared

If you compress the folder and then extract it, usually the folder will lose its icon even if it has the ini file and the icon file. The icon won't appear even if you follow the previous steps again.

There is another method to permanently attach the icon to the folder, but it'll make the icon hard to delete incase you want to remove it. Basically, this method will convert the **`desktop.ini`** file into a system file. It is relatively harder to get rid of system files.

- Make sure that the folder has '***desktop.ini***' file and the folder icon file (with an extension of `.ico`).
- Navigate to the parent folder that contains this folder.
- Right-click on the folder that contains the folder icon and 'desktop.ini' file.
- Go to '`Properties > Customize`'.
- Once there, simply press '`Okay`' and close the dialog. 
- By now the folder should have an icon and '`dekstop.ini` should be gone if not, you probably missed a step above.

### Alright. It works but I'm curious as to how?
It, uhhh
- Gets the Anime Name from the Folder Name
- Searches that name on MAL with Jikan API
- Asks you to choose the anime from results
- Gets the artwork and converts it into an icon
- Makes a `desktop.ini` file which sets the folder icon.

### I don't like these icons. How do I remove them?
To remove the cover icon from a folder, you just need to delete the `.ico` and `desktop.ini ` file from the folder. These files are hidden so make sure you have `Show Hidden Items` option ticked. You can just search and delete them all if you wanna batch remove all icons. But why would you wanna do that anyway?

#### How do I get rid of the permanent folder icon?
If you followed the steps above, the folder should have an icon by now and the `desktop.ini` should be gone from the folder. The `desktop.ini` has been converted into a System file.

If you want to remove the folder icon, then here are some ways:
- Enable 'show system files'. Once `desktop.ini` file is visible, simply delete it.
- Alternatively, `desktop.ini` can be directly deleted using a Shell terminal or any other terminal. Tested this in Bash terminal, Windows command prompt might now allow it.
- Or an even simpler method: Make a file named `desktop.ini` in any other folder. Now, copy and paste this file into the folder that has permanent icon. You'll be asked if you want to replace the existing file. Choose yes. This will remove the desktop icon and make `desktop.ini` visible. If you want, you can delete the `desktop.ini` file if you want to.


### Any Tips or Suggestions?
Yeah, the most efficient way to use this (imo) would be to:
- Run it in AutoMode first so all folders are processed
- Move out the incorrectly tagged folders and delete their icons
- Run it in ManualMode and choose the correct results

### I was promised memes. Gib memes.
Alright, here you go.

![meme](https://i.imgur.com/BXX93Rs.jpg)
