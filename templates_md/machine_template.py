from templates_md import get_template_char_user_rating, get_template_chart_radar
import datetime

def get_machine_template(VAULT_PATH,machine_data,user_average,author,user_rating,machine_tags,ownWriteup):
    time_today = datetime.datetime.now()
    string_tags = ""
    for tag in machine_tags:
        tag_with_no_spaces = tag["name"].replace(" ", "_")
        string_tags = string_tags + "#" + tag_with_no_spaces + " "

    botonUpdateMachineInfo = '''
```dataviewjs
const {createButton} = app.plugins.plugins["buttons"]
createButton({app,
            el: this.container,
            args: {
                name: "Update this Machine info",
                type: "link",
                action: "obsidian://shell-commands/?vault=HTB&execute=g7sm2q030y&_writeup="+this.current().writeup,
                },
            })
```'''
    botonCreateWriteup = '''
```dataviewjs
const {createButton} = app.plugins.plugins["buttons"]
createButton({app,
            el: this.container,
            args: {
                name: "Create Writeup",
                type: "link",
                action: "obsidian://shell-commands/?vault=HTB&execute=518r5yzp4k",
                color: "yellow",
                },
            })
```'''

    botonWriteup = '''
```dataviewjs
const {update} = this.app.plugins.plugins["metaedit"].api
const {createButton} = app.plugins.plugins["buttons"]
createButton({app, el: this.container, args: {name: this.current().writeup ? "Writeup: ✅" : "Writeup: ❌"}, clickOverride: {click: update, params: ['writeup', !this.current().writeup, this.current().file.path]}})
```'''

    return f'''
---
fileClass: Machine
---

<p align="center"> <img src= "https://www.hackthebox.com/{machine_data.avatar}"> </p>

#machine

## Operation system - {machine_data.os}
<img style = "max-width:70px" src = "app://local/{VAULT_PATH}.res/{machine_data.os}.png">

## Metadata

|              |                                            |
| ---------    | ------------------------------------------ |
| ID           | `=this.id`                                 |
| Name         | `=this.name`                               |
| Active       | `$=this.current().active == true ? "✅" : "❌"`    |
| User Flag    | `$=this.current().user_flag == true ? "✅" : "❌"` |
| Root Flag    | `$=this.current().root_flag == true ? "✅" : "❌"` |
| Writeup      | `$=this.current().writeup == true ? "✅" : "❌"` |
| Difficulty   | `=this.difficulty_text`                    |
| Stars        | ⭐️ `=this.stars`                          |
| Created Note | `=this.created`                            |
| Published    | `=this.published`                          |
| tags         | `=this.tags`                               |

<p style = "display:none">
id:: {machine_data.id}
active:: {machine_data.active}
name:: {machine_data.name}
os::{machine_data.os}
user_flag:: {machine_data.user_owned}
root_flag:: {machine_data.root_owned}
difficulty_text:: {machine_data.difficulty}
writeup:: {ownWriteup}
stars:: {machine_data.stars}
created:: {time_today.strftime("%d/%m/%Y")}
published:: {machine_data.release_date.strftime("%d/%m/%y")}
avatar:: {machine_data.avatar}
tags:: {string_tags}
</p>

## Statistics

{get_template_chart_radar(user_average, author)}


### User rating

{get_template_char_user_rating(user_rating)}


{botonUpdateMachineInfo}

{botonCreateWriteup}

{botonWriteup}

'''
