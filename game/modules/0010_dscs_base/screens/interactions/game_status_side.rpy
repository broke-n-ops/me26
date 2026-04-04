## 0.9.2 change suggested by 'MikasaTanikawa' to have the location name on top left a 'hide screen' button - 1 of 3
## style interaction_game_status_location:  ## original line
style ui_choice_title_game_status_loc:      ## replacement line
  layout "nobreak"
  text_align 0.5
  size 36

init python:
  def days_left_str(target_day,day_name,pay,did_today):
    days_left=(dow_names.index(target_day)-now.dow)%7
    if now(target_day):
      if did_today:
        if pay>mc.money:
          payday="{bad}"+day_name+" in 7 days.{/}"
        else:
          payday="{info}"+day_name+" in 7 days.{/}"
      else:
        if pay>mc.money and not did_today:
          payday="{bad}"+day_name+"!{/}"
        else:
          payday="{info}"+day_name+".{/}"
    elif days_left==1:
      if pay>mc.money:
        payday="{bad}"+day_name+" tomorrow.{/}"
      else:
        payday="{info}"+day_name+" tomorrow.{/}"
    else:
      if pay>mc.money:
        payday="{bad}"+day_name+" in %s days.{/}"%days_left
      else:
        payday="{info}"+day_name+" in %s days.{/}"%days_left
    return payday

screen interaction_game_status(act_data):
  use ui_frame(ysize=True,scroll=True):
    use ui_scrollbox:
## 0.9.2 change suggested by 'MikasaTanikawa' to have the location name on top left a 'hide screen' button - 2 of 3
##      null height 32  ## original line
      use vdiv
## 0.9.2 change suggested by 'MikasaTanikawa' to have the location name on top left a 'hide screen' button - 3 of 3
##      add FitTextDisplayable("{mark}"+game.location.name+"{/}","idle","interaction_game_status_location",side_text_size) xalign 0.5  ## original line
##  next line is the replacement line
      use ui_choice(HideInterface(),title="{mark}"+game.location.name+"{/}",size=(side_text_size[0],72),style_suffix="game_status_loc",keyboard_focus=False,align=0.5)
      use vdiv
      text "Day [now.day] - [now.dow_name]" style "cs_center"
      text "[now.tod_name]" style "cs_center"
      use vdiv
      use info_row("Mood:","[mc.mood.level_name]")
      use info_row("Energy(AP):",("{mark}[mc.energy]{/}" if mc.energy else "{bad}[mc.energy]{/}")+"{size=-8}{info}/[mc.max_energy]{/}{/}")
      use vdiv
      use info_row("Money:",money_str(mc.money))
      use vdiv
      $expenses=home.expenses
      use info_row("Expenses:",money_str(expenses))
      $payday=days_left_str(home.payment_day,"Payment day",expenses,home["paid_expenses_today"])
      text "{size=-4}[payday]{/}" xalign 0.5
      if quests.exiled_engineer=="debt1" or quests.exiled_engineer=="debt2":      ##  CHANGE MADE HERE
        use vdiv
        use info_row("Debt:",money_str(mc.debt))
        use info_row("Interest:",money_str(mc.debt_pending))
        $payday=days_left_str(quests.exiled_engineer.payment_day,"Payment day",mc.debt_pending,quests.exiled_engineer["paid_today"])
        text "{size=-4}[payday]{/}" xalign 0.5
## 0.11.n addition of Ruthie's rent after upgrading her apartment
      if fwb_pay_rent==1:    ## you are now paying 75% of Ruthie's rent
        use vdiv
        use info_row("[gn_store_owner_name]'s Rent:",money_str(fwb_amount))
        $payday=days_left_str(fwb_day,"Payment day",fwb_amount,fwb_paid_today)
        text "{size=-4}[payday]{/}" xalign 0.5
      use vdiv
      use info_row("Power Level:","{mark}[sr24_power_level]{/}")
      use vdiv
      $sr24_occupied_capsules="{mark}"+str(len(home.sexbots)-home.available_capsules)+"{/}"
      use info_row("Capsules","")
      use info_row("     In Use:",sr24_occupied_capsules)
      use info_row("     Available:","{mark}[home.available_capsules]{/}")
      if workshop.max_sexbots>0:                                         ## only show storage once you have some
        use vdiv
        $sr24_occupied_storage="{mark}"+str(len(workshop.sexbots)-workshop.available_space)+"{/}"
        use info_row("Storage","")
        use info_row("     In Use:",sr24_occupied_storage)
        use info_row("     Available:","{mark}[workshop.available_space]{/}")
      null height 32