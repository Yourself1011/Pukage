---
description: >-
  The custom level editor in Pukage is cool. You can make your own, custom
  levels. Any inappropriate levels will be removed.
---

# Custom level editor

## Lines

Custom levels are made up of many lines. Type the line content, then press enter. There are two types of lines. Basic, and special.

### Basic

Basic lines require nothing special. Just type the text. This is then given to the user as normal text.

{% hint style="info" %}
Use the `text:` line to have text lines that start with a command.
{% endhint %}

### Special

Special lines are made up of two things. The type, and the arguments. To type a special line, you type the type of line, followed by a colon, then the arguments. You can also use an alias as a substitute for the type of line. For arguments, &lt;&gt; means required, \[\] means optional, \| mean one or the other, and '' means literal.

| Type | Alias | Arguments | Description |
| :--- | :--- | :--- | :--- |
| text | t | &lt;text&gt; | Like a basic line, but you can start the text with a line type. |
| split | s | &lt;name&gt; | This is like a fork in the road. The name is required for the options. This presents the user with a choice. |
| option | o | &lt;name&gt;, &lt;split\(s\)&gt; | These are the options for a split, or many. In `<split(s)>`, put the split name\(s\) that you want to have this option. In `<name>`, put the name you want displayed to the player |
| fight | f | &lt;name&gt;, &lt;health&gt;, &lt;damage&gt;, &lt;critChance&gt;, &lt;critMulti&gt;, &lt;defense&gt;, &lt;escapeChance&gt;, &lt;character&gt;  | This starts the fighting engine. The user can attack, or defend, and the AI also chooses attack or defend. The arguments are all for the opponent. If the argument has to do with a chance \(`<critChance>`, `<defense>`, `<escapeChance>`\), then the number is the denominator in a fraction \(if the number was 10, the chance would be 1/10\). For `<character>`, replace line breaks with \n |
| command | cmd, c | &lt;commandName&gt;, &lt;commandArgs&gt; | More info in the next section. |

#### Commands

Commands are special. They don't get added to the lines of the level, but change certain things.

| Command | Aliases | Arguments | Description |
| :--- | :--- | :--- | :--- |
| exit |  |  | Exits the editor. Does not save. Make sure to save your level first, or your work will not be saved. |
| save | s |  | Saves your work. Do this before exiting, or you will lose your progress. |
| edit | e | &lt;line&gt;, &lt;new content&gt; | Edits a line. This changes the line to `<new content>`. In `<line>`, type the line number. |
| delete | d | &lt;line&gt; | Deletes a line. |
| title | t | &lt;new title&gt; | Sets the title of your level. |

