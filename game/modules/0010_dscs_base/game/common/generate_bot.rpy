default global_bots_counter=0

define default_generate_bot_warranty_seals_table={
  "oral": 0,
  "vaginal": 0,
  "anal": 0,
  }

init python:
  def generate_bot(target,*tags):
    models=[]
    process_event("generate_bot",models,target,tags)
    if models:
      model=randwchoice(models)
      if model:
        bot_cls=find_character_cls(model)
        bot=bot_cls(id="{}_#{}".format(bot_cls.id,store.global_bots_counter))
        bot.name=randchoice(bot.name_variants)
        store.global_bots_counter+=1
        generate_bot_warranty_seals(bot,default_generate_bot_warranty_seals_table)
        return bot

  def default_generate_bot_mind(bot,settings):
    for skill,xp_range in settings:
      xp=randint(*xp_range)
      if xp>0:
        bot.give_xp(skill,xp)
