app: obsidian
-
tag(): user.tabs
tag(): user.find
tag(): user.line_commands
tag(): user.splits
tag(): user.emoji

<user.teleport> daily note:
    key(ctrl-p)
    insert('today daily note')
    key(enter)

<user.teleport> dock:
    key(ctrl-o)
    edit.delete_line()

<user.teleport> dock <user.text>:
    key(ctrl-o)
    edit.delete_line()
    insert(text)
    key(enter)

<user.find> dock <user.text>:
    key(ctrl-o)
    edit.delete_line()
    insert(text)

please [<user.text>]:
    key(ctrl-p)
    edit.delete_line()
    insert(text or "")

bar (show | hide | dog) | (show | hide) bar:
    key(alt-b)

rack (show | hide | dog) | (show | hide) rack:
    key(alt-c)

task (dog | check | uncheck | complete):
    key(ctrl-l)