import sublime, sublime_plugin
import webbrowser

class OpenHelpCommand(sublime_plugin.TextCommand):

   def run(self,edit):
      helpLink = 'http://uk.php.net/manual-lookup.php?pattern={0}';
      for region in self.view.sel():
         if not region.empty():
            syntax = self.view.substr(region)
            webbrowser.open_new(helpLink.format(syntax))