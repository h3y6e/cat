# main
import sys
import pyocr
import pyocr.builders
import subprocess
from PIL import Image
from googletrans import Translator

def main():
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("Error: No OCR tool found")
        sys.exit(1)
    tool = tools[0]
    print("%s を使用します" % (tool.get_name()))
    langs = tool.get_available_languages()
    print("使用可能言語は %s です\n" % (langs))

    args = sys.argv
    if len(args) < 2:
        lang = "eng"
    else:
        lang = args[1]

    print("翻訳したい範囲を選択してください...\n")
    subprocess.run(["gnome-screenshot", "--area", "--file=./tmp.jpg"])

    origintext = tool.image_to_string(
            Image.open('tmp.jpg'),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
            ).replace('-\n','').replace('\n',' ')

    print("%s:\n%s\n" % (lang, origintext))
    newtext = Translator().translate(origintext, dest ='ja').text
    print("ja:\n%s" % (newtext))


