from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
import subprocess

class AIFallbackExtension(Extension):
    def __init__(self):
        super(AIFallbackExtension)
        self.subscribe(KeywordQueryEvent, QueryHandler())

class QueryHandler(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument()

        if not query:
            return

        try:
            subprocess.Popen(query, shell=True)
        except:
            cmd = extension.preferences.get("openclaw_cmd")
            result = subprocess.check_output(
                f"{cmd} \"{query}\"",
                shell=True,
                text=True
            )
            subprocess.Popen(result, shell=True)

        return None

if __name__ == '__main__':
    AIFallbackExtension().run()
