---
title: 情報セキュリティ対策ガイドライン
toc: true
keywords: ["security", "mail"]
summary: '情報セキュリティのリスクに対応するためのガイドラインをご提供します．'
---
セキュリティ対策は，日常的に行うことが大切です。  

### 不審なメールへの対策と対応
#### 不審なメールの見分けかた
次のような特徴に合致するメールは，標的型不審メールの可能性があるため，注意が必要です。
差出人，本文，添付ファイルをチェックしましょう。
##### STEP1 : 差出人のメールアドレス
* 企業や公的機関を名乗っているが，フリーメールアドレス(gmail, hotmailなど)から送信されている  
* 差出人のメールアドレスとメール本文の署名に記載されたメールアドレスが異なる  
##### STEP2 : メール本文
* 表示されているURLと実際のリンク先のURLが異なる  
* 署名に記載された組織名や電話番号が実在しない  
##### STEP3 : 添付ファイル
* 実行形式ファイル(exe, scr, cplなど)が添付されている  
* ショートカットファイル(lnkなど)が添付されている  
* アイコンが偽装されている  
---- (例)実行形式ファイルなのに文書ファイルやフォルダのアイコンとなっている  
* ファイル拡張子が偽装されている  
---- (例1) 二重拡張子となっている  
---- (例2) ファイル拡張子の前に大量の空白文字が挿入されている  
---- (例3) テキストの流れを右から左に強制変更する制御記号を用いて，安全な拡張子に見せかけている   
---- (ファイル形式は，プロパティで拡張子を表示することで確認できます)  

#### 不審なメールへの対応
不審なメールが届いたら...
##### 不審だと判断できれば，削除しましょう
よく分からないときは，情報基盤センターへ相談してください

##### 興味本位でアクセスしない
* 添付ファイルを開かない  
* 埋め込まれているリンクへアクセスしない  
* 返信しない  
* メールの内容についての検索結果ヘ安易にアクセスしない  
##### 開いてしまったら， アクセスしてしまったら
不審なメールの添付ファイルを開いてしまったり，リンクへアクセスしてしまったときは，  
情報基盤センターへ相談してください
##### 不審な添付ファイルを開く必要がある場合は
* ダウンロードした上で，アンチウィルスソフトなどで安全を確認した上で利用してください  
* よくわからないときは，情報基盤センターへ相談してください  

#### 被害を最小限に食い止めるために
次のような対策を実施することで，開封などした場合の被害を最小限に食い止めることができます

* OS，ソフトウェアはアップデートを行い最新の状態にする
* ウィルス対策ソフトをインストールし，最新の状態にする
* PDF閲覧ソフトのJavaScriptをオフにする
* メールソフトのhtml表示をオフにする
* データのバックアップをとっておく
対策方法については，[こちら](#device-setting)をご確認ください

#### IPA 映像コンテンツ紹介
IPA(独立行政法人情報処理推進機構)が，YouTube内の「IPA Channel」を通じて公開している映像コンテンツです。 
IPA 映像コンテンツ を観る 
そのメール本当に信用していいんですか?  
?標的型サーバー攻撃メールの手口と対策?
[![そのメール本当に信用してもいいんですか？-標的型サイバー攻撃メールの手口と対策-](./img/IPA-UntrustMailVideo.jpg)](https://www.youtube.com/watch?v=duGNXcEEToU)
企業内の標的型攻撃メールの訓練を舞台に，ウイルスが含まれている添付ファイルを開かせる標的型標的型サイバー攻撃メールの手口を示し，その対策を説明します。

### 機器の対策
#### STEP1 : OSやソフトウェアのアップデート
パソコンやスマートフォンのOS，各種ソフトウェアは，脆弱性を改善した最新版が随時提供されており，アップデートにより適用されます。  
とくにJavaやAdobeは，ウイルス強制感染の経路となったことが多く報告されています。
最新の状態を維持するようにしましょう。  
更新を放置することは，たいへん危険です。
#####  Javaのアップデート方法
次のURLにアクセスし，Javaの最新バージョンをインストールできます。  
<https://java.com/ja/download/>  
#####  Adobe Acrobat Readerのアップデート方法
既存のAcrobat Readerから 「ヘルプ(H)→アップデートの有無をチェック 」を実行します。  
また，次のURLにアクセスし，Acrobat Readerの最新バージョンをインストールできます。  
<https://get.adobe.com/jp/reader/>  
#####  Adobe Flash Playerのアップデート方法
次のURLにアクセスし，Adobe Flash Playerの最新バージョンをインストールできます。  
<https://get.adobe.com/jp/flashplayer/>  

#### STEP2 : ウイルス対策ソフトウェア
ウィルス対策ソフトウェアのウィルスパターンファイルや検索エンジンは，自動更新にするなどして常に最新の状態にしてください。
※ウイルスは日々最新のものが作成されています。ウィルスパターンファイルも最新にする必要があります。  
インターネットに接続せず利用するパソコンにもウィルス対策ソフトウェアは必要です。  
また，インターネットに接続して，最新のウィルス定義ファイルをダウンロードしましょう。  
※USBメモリ，CD-R/DVD-R等からウイルスに感染する恐れがあります。  
#### STEP3 : PDF閲覧ソフトウェアのJavaScriptの無効化
悪意のあるJavascriptを仕込んだPDFを添付されていることがあります。  
PDF閲覧ソフトウェアの設定をあらかじめ変更しておくことで，悪意のあるPDFファイルを開いてしまった場合でも，攻撃を阻止することができます。  
Javascript のオプションは，ON(デフォルト)からOFFに変更しておいてください。  

##### －Adobe Acrobat Readerの場合－
**編集 - 環境設定 - JavaScript** で，「Acrobat JavaScriptを使用」のチェックを外します.

#### STEP4 : 電子メールをテキスト形式で表示する
電子メールに悪意のあるhtmlや画像(Webビーコン)が組み込まれている場合があります。  
* 電子メールをテキスト形式で表示することをおすすめします。  
[テキスト形式で電子メール メッセージを読む](https://support.office.com/ja-jp/article/%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E5%BD%A2%E5%BC%8F%E3%81%A7%E9%9B%BB%E5%AD%90%E3%83%A1%E3%83%BC%E3%83%AB-%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8%E3%82%92%E8%AA%AD%E3%82%80-0b94051b-9985-44e4-b254-cdc836f57945)  
電子メールを送る場合も，必要の無い限りテキスト形式で送ることをおすすめします。  
[メッセージ形式を HTML、リッチ テキスト形式、またはテキストに変更する](https://support.office.com/ja-jp/article/%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8%E5%BD%A2%E5%BC%8F%E3%82%92-html%E3%80%81%E3%83%AA%E3%83%83%E3%83%81-%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E5%BD%A2%E5%BC%8F%E3%80%81%E3%81%BE%E3%81%9F%E3%81%AF%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%81%AB%E5%A4%89%E6%9B%B4%E3%81%99%E3%82%8B-338a389d-11da-47fe-b693-cf41f792fefa)  
*メーリングリストに投稿する際は，テキスト形式にして下さい。  
#### STEP5 : データのバックアップ
* 必ずバックアップをとるようにしましょう。  
　 USBメモリや外付けハードディスク，CD-R/DVD-Rなど，外部記憶媒体にバックアップをとって下さい。  
　 iCloud DriveやGoogle Drive，Dropboxなどのクラウド・ストレージもございます。  
　 Office 365で利用できる，OneDriveの使用をお勧めします。

### 情報漏洩への対策
漏れないようにすることはもちろん，漏れても困らないようにしましょう。  
#### データの暗号化
ノートパソコンやUSBの紛失・盗難，廃棄されたパソコンからのデータ復元などによる，情報の漏洩対策として，データを暗号化する方法があります。  

##### Office製品の暗号化
ファイルの保存時に暗号化ができます。  
ファイルを保存する際に，読み取り，書き込みのパスワードを設定できます。  
[名前を付けて保存]－[全般オプション]  

ファイルに様々なアクセス制限を設定する機能も，Office2007から導入されています。  
コピー，貼り付けの禁止，閲覧期限の設定など，パスワードより柔軟な制限を設定できます。  
##### ファイルの暗号化
また，USBメモリや外付けハードデイスクの場合には，ファイルをすべて暗号化して保存する製品もあります。  
##### 暗号化ソフト
暗号化されたファイル保存領域を作成するためのオープンソースソフトウェアもあります。  
ファイルやパーテイションを暗号化されたファイルの保存領域として作成できます。  

#### パスワードの管理
ウェブサービスや暗号化ソフト，ファイルの暗号化などパスワードが必要なシーンは増加しています。  
適切な管理をお願いします。  

##### パスワードを強く!
パスワードの使い回しや，すぐに推定可能なパスワードなど，セキュリテイの要であるパスワードが脆弱では意味がありません。
* 使用できる文字種（大小英文字、数字、記号）すべてを組み合わせましょう。  
* 8文字以上のパスワードにしましょう。  
* 辞書に載っているような単語や人名は使用を避けて下さい。

##### 適切に保管
紙にメモしても構いませんが，その際，IDとパスワードは別々の紙にメモするなどして保管しましょう。  
Webブラウザなどに記憶して保管するのはおすすめしません。
パスワード管理ソフトもあります。  
[Moodle](https://lms.naruto-u.ac.jp/local/narutologin/index.php) で紹介しています。
（[Moodle ログイン方法](moodle_login.pdf)）  
Moodle へは，ユーザIDとパスワードでログインしてください。

##### 使いまわしをしない!
複数のサービスで同じIDやパスワードを使いまわしていると，不正利用の被害が拡大する危険性があります。  
また普段利用していないインターネットサービスに関しては，登録解除することをおすすめします。  
##### IPA パスワード強化啓発サイト
IPA(独立行政法人情報処理推進機構)の啓発サイトです。  
[パスワード?もっと強くキミを守りたい?](https://www.ipa.go.jp/security/keihatsu/munekyun-pw/)  
[チョコっとプラスパスワード](http://www.ipa.go.jp/chocotto/pw.html)  

### P2Pソフトを使用しない
P2P (Peer to Peer) ソフトは，動画の閲覧やファイル共有などのソフトでよく利用されています。  

##### P2Pソフトを利用しないようにしてください。

　鳴門教育大学のネットワークを経由して，  
　コンテンツの違法な交換が行われる可能性のあるP2Pソフトに関しては，  
　ウィルス感染・情報漏洩・著作権侵害などの危険性があるため，利用を禁止しています。  
##### VPNソフトを利用しないようにしてください。

　同様に，コンテンツの違法な交換が行われる可能性のあるVPN（Virtual Private Network）ソフトに関しても，利用を禁止しています。  
### 違法ダウンロード
文化庁に次のようなサイトがあります。  
[著作権に関連する情報](https://www.bunka.go.jp/seisaku/chosakuken/seidokaisetsu/index.html)  
[著作権に関連する教材・資料等](https://www.bunka.go.jp/seisaku/chosakuken/seidokaisetsu/kyozai.html)  
### IPA 映像で知る情報セキュリティ
IPA(独立行政法人情報処理推進機構)が，YouTube内の「IPA Channel」を通じて公開している映像コンテンツです。   
[![映像で知る情報セキュリティ](./img/IPA-securityVideo.png)](https://www.ipa.go.jp/security/keihatsu/videos/index.html)  

