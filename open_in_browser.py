import sublime_plugin
import webbrowser


class OpenInBrowser(sublime_plugin.TextCommand):
    def run(self, edit):

        webbrowser.open()
