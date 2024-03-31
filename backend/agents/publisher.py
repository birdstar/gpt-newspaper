import os
import shutil


class PublisherAgent:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def save_newspaper_html(self, newspaper_html):
        path = os.path.join(self.output_dir, "newspaper.html")
        with open(path, 'w') as file:
            file.write(newspaper_html)

        source_file = "../templates/newspaper/layouts/aigc.png"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        source_file_path = os.path.join(dir_path, source_file)

        shutil.copy(source_file_path, self.output_dir)

        return path

    def run(self, newspaper_html: str):
        newspaper_path = self.save_newspaper_html(newspaper_html)
        return newspaper_path
