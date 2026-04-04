default rename_bot_to=None

init python:
  def validate_bot_name(name):
    if name.strip():
      return ""
    else:
      return "{bad}Can't be nameless{/}"

define allowed_bot_name_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -'`0123456789#/"

label interact_default_rename(bot):
  header "[bot] - Rename"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [bot.model_id] avatar@400x600}"
  $act.set_block("c")
  "[bot.hisher!c] current name is {mark}[bot]{/}."
  ""
  "If you think a different name might fit [bot.himher] better, you can always change it. It's not like [bot.heshe] can complain, and license agreements rarely include fixed trademark name clauses."
  ""
  $rename_bot_to=bot.name
  $act.add_screen("ui_input","rename_bot_to","do_rename_bot:{}".format(bot.id),'validate_bot_name("{}")',xalign=0.5,width=300,allowed_chars=allowed_bot_name_chars)
  $act.end_block()
  choice("do_rename_bot:{}".format(bot.id),sensitive_if="$not validate_bot_name(rename_bot_to)") "Rename"
  choice("<<<",key="cancel") "Cancel"
  return

label do_rename_bot(bot):
  $bot=find_character(bot)
  if bot.name==rename_bot_to:
    $bot=None
    return "<<<"
  header "[bot] - Rename"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [bot.model_id] avatar@400x600}"
  $act.set_block("c")
  "You decided to rename {mark}[bot]{/} to {mark}[rename_bot_to]{/}."
  $bot.name=rename_bot_to
  call interact_include("rename_reaction")
  $bot=None
  $act.end_block()
  choice("<<<") "Continue"
  return
