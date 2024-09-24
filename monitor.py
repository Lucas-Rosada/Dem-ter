import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Diretório para monitorar
monitored_dir = 'videos/'

class ImageEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'Evento detectado: {event}')
        if not event.is_directory and event.src_path.endswith('.webm'):
            print(f"Novo audio detectado: {event.src_path}")

if __name__ == "__main__":
    event_handler = ImageEventHandler()
    observer = Observer()
    observer.schedule(event_handler, monitored_dir, recursive=False)
    observer.start()
    print(f"Monitorando o diretório: {monitored_dir}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()