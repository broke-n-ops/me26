screen status_mc_page_property(act_data):
  $char=find_character(act_data.get("char","mc"))
  text "{=label_text}Status - Property{/}\n" xalign 0.5
  text "{size=+8}Chop Shop{/}"
  if home.rent is None:
    text "Status: {mark}Owned{/}."
  else:
    text "Status: {mark}Rented{/}."
  text "Bot capsules: {mark}[home.max_sexbots]{/}, available: {mark}[home.available_capsules]{/}, maximum: {mark}[sr24_max_capsules]{/}."
  use vdiv
  text "{size=+8}Expenses{/}"
  $expenses={}
  $process_event("expenses",expenses)
  $expenses_sum=0
  if expenses:
    for id,(value,desc) in sorted(expenses.items()):
      $expenses_sum+=value
      use info_row(" - "+desc,money_str(value))
    use vdiv
  use info_row("Grand total:",money_str(expenses_sum))
  use info_row("Paid weekly, payment day:","{mark}[home.payment_day]{/}")
  use vdiv
  use interaction_content(act_data)
