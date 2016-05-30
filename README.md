# domi-randomizer

ドミニオンのカード選択のためのCLIアプリケーションです。英語のみ対応です。  
  
ブラウザ上で動くやつ作りました!!  
http://ArabicaArabica.github.io/domi-randomizer

## 実行環境
Linuxをベースとしたpython2.7が動作するシステム（Mac OS X, Ubuntuなど）
## インストール方法
domi-randomizer.py および cards.datを同一ディレクトリ内においてください。  
さらに、domi-randomizer.pyに実行権限を与えてください。  
`chmod u+x domi-randomizer.py`  
実行環境によっては一行目のシバンを変えてください。
## 使用方法
オプションを何も指定せず実行すればすべての拡張セットからカード１０枚をランダムに選択します。  
`./domi-randomizer.py`  
### オプション
１文字オプションは以下の通りです。  
* -a --adventures 冒険の拡張セットを指定します。
* -b --base 基本セットを指定します。
* -c --cornucopia 収穫祭の拡張セットを指定します。
* -d --darkages 暗黒時代の拡張セットを指定します。
* -g --guilds ギルドの拡張セットを指定します。
* -i --intrigue 陰謀のセットを指定します。
* -l --alchemy 錬金術のセットを指定します。
* -n --hinterlands 異郷の拡張セットを指定します。
* -s --seaside 海辺の拡張セットを指定します。  

引数を指定した場合にはその拡張セットから枚数分だけ選択されます。残りは他のセットから選択されます。  
`./domi-randomizer.py -a 3`  
引数を指定しなければ単にその拡張セットに含まれるカードすべてが選択候補に入るだけです。  
`./domi-randomizer.py -b -c`  
引数を指定したオプションと指定していないオプションを同時に使用した場合には、指定した拡張セットがその枚数だけ選択され、
その後残りの枚数分だけ、枚数を指定していない拡張セットから選択されます。  
`./domi-randomizer.py -b 5 -g -i  
この場合基本セットから５枚、残りの５枚がギルドおよび陰謀の拡張から選択されます。`  
   ---
他のオプションは以下の通りです。
* --add 必ず含めるカードをカード名で指定します。
* --omit 選択する候補から外すカードをカード名で指定します。  

`./domi-randomizer.py -b --add saboteur`  
`./domi-randomizer.py -s -b 5 --omit witch`  
カード名は小文字で指定してください。  
また、 `great hall`のようにカード名にスペースが含まれる場合には-(ハイフン)でこれを置き換えて`great-hall`としてください。
## 今後の機能追加予定
* 魔女娘が選択された場合に災いカードを自動的に選択する機能
* 冒険拡張セットのイベントカードを自動的に選択する機能
