# bottle serial

- HTTP経由でArduinoにシリアルでコマンドを送り、Arduinoからの応答をHTTPで返します。
- ブラウザからの呼び出しを想定し、CORSに対応しています。

## 使い方

- Arduinoを接続し、bottle_serial.pyのシリアルパラメータ```/dev/tty.usbmodem1451```を書き換え、起動します。
```
$ python bottle_serial.py
```
- ブラウザから```http://localhost:8946/arduino/1234```を開くと、Arduinoに文字列```1234````が送信されます。。

## bottleとpyserialのインストール

```
pip install bottle
pip install pyserial
```
