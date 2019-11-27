# cat - Capture Area Translator
選択範囲をOCRして翻訳してくれる猫
(GNOME環境のみ)

## 必要なもの
 - Python 3.x
 - pip
 - gnome-screenshot
 - Tesseract

[Tesseractのインストール方法](https://github.com/tesseract-ocr/tesseract/wiki)  
Ubuntuの場合は以下
```shell
$ sudo apt install tesseract-ocr
$ sudo apt install libtesseract-dev
```

## 準備
```shell
$ pip install -r requirements.txt
```

## 使い方
```shell
$ python cat.py
```
マウスカーソルで選択した範囲の英文と，その日本語訳が出力される

## License
WTFPL
