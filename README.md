# bottle serial

- HTTP経由でArduinoにシリアルでコマンドを送り、Arduinoからの応答をHTTPで返します。
- ブラウザからの呼び出しを想定し、CORSに対応しています。

## 使い方

- Arduinoを接続し、bottle_serial.pyを起動します。
（Macの場合、ポートを自動取得します。
Windowsの場合は手動で指定してください。）

```
$ python bottle_serial.py
```
- ブラウザから```http://localhost:8946/arduino/1234```を開くと、Arduinoに文字列```1234````が送信されます。。

## bottleとpyserialのインストール

```
pip install bottle
pip install pyserial
```
