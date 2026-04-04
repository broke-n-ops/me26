init python:
  class Quest_where_to_get_bot_parts(Quest):
    quest_type="note"

    name="Where to get bot parts"

    def init(self):
      self.entries={}
    def add_method(self,method,description):
      if self.entries.get(method)!=description:
        self.entries[method]=description
        process_event("quest_updated",self)

    class phase_1_notes:
      def description(self):
        rv=[]
        for method,description in sorted(self.entries.items()):
          rv.append(" - "+description)
        if rv:
          rv="\n".join(rv)
        else:
          rv="{info}You don't know where to get bot parts. You need to ask around, check markets, and maybe other places.{/}"
        return rv

    class phase_1000_finished:
      description="Finished"
    class phase_2000_failed:
      description="Failed"
