---
title: ネットワーク
toc: true
weight: 40
---
 学内ネットワークシステムにより，情報コンセントや無線LANを利用して，教室や研究室，図書館などからネットワークに接続できます。
 学内ネットワークシステムは，次の方法で利用できます。  
 ・情報基盤センターが管理する端末室や図書館のPCから  
 ・ご自分の機器を各部屋の情報コンセントへ接続して  
 ・ご自分の機器を無線LAN接続して
 
端末室や図書館のPCの利用については [こちら]({{< ref "pc-room" >}}) をご覧ください。

### 利用時の設定
#### IPアドレスについて
 IPアドレスは自動取得するように設定してください。  
 学内のDHCPサーバにより，接続のたびにIPアドレスが割り振られます。  
> 固定IPアドレスの割り当てを希望される方は，申請してください。
 
#### プロキシサーバの設定
 プロキシサーバは「自動検出」にします．
 スマートフォンやタブレットを使用する場合も，プロキシサーバの設定が必要です．  
 設定方法は，情報基盤センター Knowledge  [#265 学内プロキシサーバの設定](https://www.naruto-u.ac.jp/center/it/knowledge/open.knowledge/view/265?offset=0&keyword=プロキシ)  をご覧ください．
 
 プロキシサーバは，インターネット上のファイルやウェブページ等をユーザの代理（プロキシ）で取得してくれる機能を持つサーバです。  
 適切なプロキシ（代理）サーバを設定することで，インターネットの接続が最適化され，ウィルスチェックも行われます。  
 適切に設定が行われていないと；  
 ・授業実践映像データベースの画像やYouTube, Netflixが見えない.  
 ・無線LAN利用時に学外もしくは学内のサイトへアクセスできない．  
 などの場合がありますので，注意してください。
 
 
### 情報コンセントへの接続（有線）
 学内の各部屋や端末室に，情報コンセントを設置しています。
 
 情報コンセントへ接続する室内の配線や機器は，利用者において管理くださいますよう，お願いします。
 
 また，新たに有線ネットワークへの接続を開始する場合や，利用目的を変更したい場合は，情報基盤センターへご相談ください。  
 室内のLAN配線を変更するだけでは正常に動作しない場合があります。  
 例：事務用ネットワークから学術研究用ネットワークに変更する場合
 
 
### 学内における無線LANアクセスポイントの設置について
 無線LANは，本学においても数多く利用されていますが，電波資源は有限であり，電波を発信すれば一定の空間内に影響を与えます。  
 例えば，情報基盤センターで整備した無線LANも，他者が設置した基地局（AP）の電波の影響を受け，チャンネルが隣接した場合は干渉などの影響を受けます。  
 研究室や院生室に無線LANアクセスポイントを設置する場合，次のようなガイドラインに従っていただくことが望ましいです。
 
無線AP設置ガイドライン を読む
##### 研究室にAPを設定する場合
 ・電波は簡単に盗聴可能です。通信路の暗号化を適用してください。WPA2を推奨します（WPAは暗号の脆弱性のため非推奨です）。  
 ・利用者を特定できるようにし，不特定多数に開放しないようにしてください。  
   －－暗号化キーを利用者のみに公開する，SSIDを非公開（ステルス）にする，指定するMACアドレスのみ接続可能にする（MACアドレスフィルタリング），などの対策があります。  
  
 ・5GHz（802.11a，802.11ac/ax）を利用してください。  
   －－最新のノートパソコンやスマートフォンの多くは5GHz帯に対応しております。  
 ・2.4GHz（802.11b，802.11g）はできるだけ利用しないでください。  
   －－2.4GHz帯は利用できるチャンネルが限られますので，混信や速度低下の原因となる場合があります。  
  
 ・無線LAN AP間の干渉を避けるように利用チャンネル，出力を調整してください。  
   －－出力は最低限度の設定にしても室内での利用は可能と思われます。  
 ・部屋の外にまで電波が漏れるようなら，設置情報を報告してください。  
   －－電波の強さや使用チャンネルなどの情報は，Wi-Fi Analyzer（Android）などを利用して取得できます。  
  
 ・無線LAN APの設定をご確認ください。  
   －－ルーターの設定は アクセスポイント(AP)モード または ブリッジ(Bridge)モード に設定してください。  
   　　自動設定(Auto) や ルーター(Router)モード に設定すると，プロキシサーバーへ接続できない場合があります。  
   －－LANケーブルは [WANポート] (Internetポート) につないでください。  
  　　[LANポート] につなぐと動作しないだけではなく，学内ネットワーク全体の障害の原因になる場合があります。  
  
 ・プリンタなどの共有には無線LANではなくbluetoothを利用してください。（Bluetoothは Class 2，3を推奨いたします）  
  
 ・You MUST use a wireless device that is licensed under Japanese Radio Regulations.  
無線AP設置ガイドライン を閉じる
 会議室や研究室，院生室等で学内無線LAN(INDIGO)アクセスポイントの設置を希望される場合は，情報基盤センターまでお問い合わせ下さい。
 
 
### 無線LANへの接続 (Connect to Wireless LAN)
 高島キャンパス内では「INDIGO」（IEEE802.11a/ac/ax 規格）無線LANを提供しています。  
 Wireless LAN are available on Takashima campus: "INDIGO" (IEEE802.11a/ac/ax standard) .  
#### INDIGO
SSID (ESSID)：INDIGO
認証方式(Authetification Method)：IEEE 802.1X
DO NOT tell Your Student number and password to others.  
#### INDIGO 認証パネル (802.1X Authentication)
 ユーザー名： ユーザID（学籍番号／教職員番号）　（@naruto-u.ac.jp不要）  
 (Sutudent / Faculty number -- Numeric only -- Domain name '@naruto-u.ac.jp' is Unnecessary)  
 パスワード： パスワード　(Your own Passoword)  
 [OK]を押して下さい。
 一度設定すると，端末が認証情報を記憶しますので，次回からは入力する必要はありません。  
 When you set Authenticate and connect successfully, Afterwards, You may not enter your User ID and Password again.
 
#### INDIGO 接続手順 (How to connect INDIGO Access Point)
設定手順は，情報基盤センター Knowledge  [#324 無線LANを利用したい](https://www.naruto-u.ac.jp/center/it/knowledge/open.knowledge/view/324) をご覧下さい。  
 ⇒ スマートフォン（iPhone/iPad, Android）の設定方法も上記knowledgeをご覧ください。  
 You can connect your Smartphone or tablet (iPhone/iPad, Android) to "INDIGO" Wi-Fi. Please refer knowledge #324.
 
【接続できな場合の対応方法】  
 ・[#351 INDIGOからすぐに切断されてしまう](./knowledge/open.knowledge/view/351)  
 ・[#352 ネットワーク一覧に INDIGO が表示されない](./knowledge/open.knowledge/view/352)  
 ・[#343 無線LANの接続が不安定です](./knowledge/open.knowledge/view/343)
#### プロキシサーバの設定 (Proxy Server setting)
 プロキシサーバは「自動検出」に設定します．
 スマートフォンやタブレットを使用する場合も，プロキシサーバの設定が必要です．  
 Set the Proxy Server to "Automatically detect". You also need to set up a proxy server on your Smartphone or Tablet.  
 上記［利用時の設定］～［プロキシサーバの設定］を参照して下さい。  
 情報基盤センター Knowledge  [#265 学内プロキシサーバの設定](https://www.naruto-u.ac.jp/center/it/knowledge/open.knowledge/view/265)  
#### 附属学校園
 附属学校園におきましては，認証方法が「IEEE802.11X認証」に変更になりました。（平成29年9月より）  
 認証パネルにユーザーID（学籍番号／教職員番号）とパスワードを入力してください。  
 ご利用につきましては，各附属学校の管理者にご確認ください。
 
 
