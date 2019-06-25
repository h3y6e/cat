# main
import subprocess
from PIL import Image
import sys
import pyocr
import pyocr.builders
from googletrans import Translator

def main():
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))
    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))
    lang = langs[0]
    print("Will use lang '%s'" % (lang))

    subprocess.run(["gnome-screenshot", "--area", "--file=./tmp.jpg"])

    origintext = tool.image_to_string(
            Image.open('tmp.jpg'),
            lang='eng',
            builder=pyocr.builders.TextBuilder()
            )

    print("eng: ", origintext)
    text = origintext.replace('-\n','').replace('\n','')
    text = (Translator().translate(text, dest ='ja').text)
    print("ja_jp: ", text)


