---
title: 電子メールシステム
toc: true
weight: 30
---
### アカウント（ユーザ名）／パスワードとメールアドレス
#### アカウント（ユーザ名）
ユーザID@naruto-u.ac.jp（Microsoft 365のアカウント）です。
入学時に発行する「ユーザID通知書」に記載されています。
![](./img/icon-exclamation.png)ご注意 [Microsoft 365]のアカウントは［Microsoftアカウント］とは異なります。
#### パスワード
 初期値は，入学時に発行する「ユーザID通知書」に記載されています。
 必ず変更して下さい。→ [こちら]({{< ref "account#パスワード" >}})　
#### メールアドレス
 初期値は，入学時に発行する「ユーザID通知書」に記載されています。
 学生は別名（エイリアス）を設定できます。→ [こちら]({{< ref "mail#メールエイリアス別名の登録" >}})　
#### 利用期間
在学中，利用できます。
卒業，修了，退職後は，メールシステムにもアクセスできなくなります。
必要なデータは移行してください。
### 多要素認証（MFA）の設定
#### Microsoft 365 多要素認証（MFA）の設定
Microsoft365のセキュリティを強化するため，不正ログイン対策として，学外からログインする場合に多要素認証を適用します。
次のマニュアルを参照し，いずれかの方法で初期設定をお願いします。
##### ■Microsoft365 多要素認証の導入について（初期設定マニュアル）
Microsoft365のセキュリティを強化するため，不正ログイン対策として，学外からログインする場合に多要素認証を適用します。
次のマニュアルを参照し，いずれかの方法で初期設定をお願いします。
学外からログインする場合，初期設定を行った認証方法（スマートフォン・電話・パソコン）での承認が必要となりますので，ご注意ください。（例：学外から大学のOutlookやTeamsを使用する場合）
* [①パソコンとスマートフォンを用い，アプリで行う認証方法](./mfa/MFA1-PC_and_Smartphone.pdf)（推奨）
* [②スマートフォンだけ行う認証方法](./mfa/MFA2-Smartphone_only.pdf)
* [③パソコンと電話で行う認証方法](./mfa/MFA3-PC_and_Telephone.pdf)（固定電話／携帯電話）
* [④パソコンだけで行う認証方法](./mfa/MFA4-PC_only.pdf)
* ![](./img/icon-exclamation.png)注意事項
* Windows PCをお使いの場合，Edge以外のブラウザでは正常に設定作業が行えない場合があります。
* ①QRコードをスキャンする場合，スマートフォン付属のQRコードリーダーは使用いたしません。
* ①②スマートフォンは学内無線LAN（INDIGO）ではなく，携帯電話回線に接続して設定を行って下さい。
* ③大学の電話番号を登録しないようにしてください。携帯電話を推奨いたします。
* ④大学のパソコンで登録した場合，ノートパソコンなど他のパソコンを使用する場合は追加登録が必要となります。  
Mac OS Xの場合，ChromeブラウザとChrome用拡張機能  [Authenticator](https://authenticator.cc/) を使用します。
##### ■設定の確認および認証方法の追加手順
[portal.office.com](https://portal.office.com)よりMicrosoft365にログインします。
ホーム画面の右上の人型アイコンより　「アカウントを表示」を選びます。
「セキュリティ情報」＞更新情報　で現在のサインイン方法が表示され、変更・削除が可能です（例：電話番号の変更）
＋サインイン方法の追加　よりサインイン方法の追加が可能です（例：代替電話の登録，予備のスマートフォンの登録）
![](./img/icon-exclamation.png)メールソフトで，IMAPプロトコルを設定している場合は，ご利用できなくなっております。
Microsoft365の多要素認証は，IMAPなど基本認証に対応しておりません。Microsoft365の，IMAPプロトコルによる認証は2022年10月1日に廃止されました。
Exchangeプロトコル，または OAuth2.0認証 での利用をお願いいたします。
[メールソフトの設定](./mail.html#setting)
![](./img/icon-exclamation.png)メールソフトで，アプリケーションパスワードを設定している場合も，多要素認証への移行となります。
上記のとおり，Exchangeプロトコル，または OAuth2.0認証 での利用をお願いいたします。  
#### To Setup Microsoft 365, multi-factor authentication (MFA)
To enhance the security of Microsoft 365, multi-factor authentication (MFA) will be applied when logging in from outside the university as a countermeasure against unauthorized logins.  
Please refer to the following manual and use one of the following methods to set up the initial settings.
##### Introduction of Microsoft 365 Multi-Factor Authentication (Initial Setup Manual)
To enhance the security of Microsoft 365, multi-factor authentication (MFA) will be applied when logging in from outside the university as a countermeasure against unauthorized logins.  
Please refer to the following manual and use one of the following methods to set up the initial settings.
Please note that when logging in from off-campus, you must be authorized by the authentication method (smartphone, landline phone, or computer) that you have initially set up. (e.g., when using Outlook or Teams on our University account from off-campus)
* [(1) Authentication by using both a personal computer and smartphone with the application](./mfa/MFA1-PC_and_Smartphone_English.pdf) (recommended)
* [(2) Authentication by using only a smartphone](./mfa/MFA2-Smartphone_only_English.pdf)
* [(3) Authentication by using both a personal computer and telephone (landline/smartphone)](./mfa/MFA3-PC_and_Telephone_English.pdf)
* [(4) Authentication by using only a personal computer](./mfa/MFA4-PC_only_English.pdf)
![](./img/icon-exclamation.png)NOTE:  
If you are using Windows PC, you may not be able to set up correctly with browsers except Edge.  
(1) When scanning QR codes, the QR code reader that comes with your smartphone will not be used.  
(1), (2) Connect your mobile device to the mobile phone line, not the On-Campus wireless LAN (INDIGO), and set it up.  
(3) Please do not register the phone number of the university. Your mobile phone number is recommended.  
(4) If you have registered on our university's computer, you will need to register an additional computer if you wish to use another computer, such as your laptop.  
For Mac OS X, use the Chrome browser and the Chrome extension  [Authenticator](https://authenticator.cc/).
##### If you want to check / change your information after setting
1. From the university Web page [portal.office.com](https://portal.office.com), connect to the university portal site and open the Microsoft Office home page.  
2. Click Account Manager at the top right of the screen. and Click "View Account".  
3. The My Account screen will be displayed. Click "Update Information" under Security Information.  
4. The security information screen is displayed.You can check and change the setting information from here.
### Webメール ：Outlook の使い方
Microsoft 365 の Outlookは，Webブラウザからアクセスする Webメールです。
Outlookの利用方法 を読む
Microsoft 365にサインインして，Outlookアプリを利用します。
![[1].](./img/number3_41.gif) Webブラウザを起動し，アドレスバーに下記のURLを入力して接続します。  
【URL】  
<https://portal.office.com/>
★Webブラウザは，最新版をご利用ください。  
![[1].](./img/number3_42.gif) サインインします。
 サインインには，Microsoft 365アカウント（ユーザID@naruto-u.ac.jp），パスワードを使用します。
 ★メールアドレス@naruto-u.ac.jp'ではありません。
![Sign in](./img/office365_signin.jpg) 
 ★初回起動時のみタイムゾーン設定画面が表示されますので、「大阪、札幌、東京」(Osaka, Sapporo, Tokyo) を選んでください。  
![[1].](./img/number3_43.gif) Outlookアプリを起動します。
 ![Top menu](./img/office365_top.jpg)
詳細は [Office 365 サインイン](./attached/Office365ログイン.pdf) をご覧ください。
####  注意事項
以下の場合，メールが一時的に利用できなくなることがあります。
* 1時間当たり3600通を超える受信メール
* 1通当たり500を超える受信者数への送信メール
* 1日当たり10,000を超える受信者数への送信メール
* 1分当たり30通を超えるメーラーからのSMTP送信メール
(2018年9月時点)
### メールソフトの設定
Exchange接続やIMAP接続を設定することで，メールソフトのメール/予定表/連絡先をOutlookと同期して利用できます。
#### Exchangeプロトコル利用
Exchangeプロトコルが利用できるメールソフトには，
Outlook（デスクトップアプリ）やMacメール(OS X)，
iPhone標準メールアプリやGmailアプリ（Android版）などがあります。
##### Exchangeプロトコルで設定する
ほとんどの場合，メールアドレスおよびユーザ名（ユーザID）とパスワードを入力するだけで自動的にサーバを検索し，設定を完了します。
【設定例】
* [Microsoft Outlook 2016](./attached/exchange-outlook2016.pdf)
* [Macメール(OS X バージョン10)](./attached/exchange-mac-mail10-new.pdf)
* [iPhone 標準メールアプリ（iOS 12.2）](./attached/iPhone-exchange.pdf)
* [Gmailアプリ Android (8.0)](./attached/GmailAndroid.pdf)  
#### IMAPプロトコル利用
##### ご注意 Microsoft365の，IMAPプロトコルによる認証は2022年10月1日に廃止されました。
![](./img/icon-exclamation.png)上記Exchangeプロトコルに対応したメールソフト もしくは OAuth2.0認証に対応したメールソフトをご利用下さい。  
OAuth2.0認証に対応したメールソフト　Mozilla Thunderbird　78.0 以降，など  
![](./img/icon-exclamation.png)ご注意 GmailのメールアプリはOAuth2.0に対応していません。
Thunderbirdの場合，「通常のパスワード認証」を「OAuth2」に変更して下さい。
##### ThunderbirdをOAuth2.0認証に設定する
ユーザ名には，ユーザID@naruto-u.ac.jp を指定してください。  
ユーザーID は学籍番号／教職員番号となります（メールアドレスではありません）。
##### Thunderbird OAuth2.0変更点
| 設定項目 | 受信サーバー | 送信サーバー |
| --- | --- | --- |
| プロトコル | IMAP | SMTP |
| サーバー | outlook.office365.com | smtp.office365.com |
| ポート番号 | 993 | 587 |
| SSL | SSL/TLS | STARTTLS |
| 認証方式 | 通常のパスワード認証 ⇒ OAuth2 | 通常のパスワード認証 ⇒ OAuth2 |
| ユーザー名 | ユーザID@naruto-u.ac.jp | ユーザID@naruto-u.ac.jp |
多要素認証の適用後，メールのパスワードを「アプリケーションパスワード」に変更を行って下さい。
［多要素認証マニュアル］の「※こんなときは」を参照して下さい。
大学ポータルサイト(portal.office.com)から
[アカウントを表示］⇒［セキュリティ情報］⇒［更新情報
＋サインイン方法の追加⇒アプリパスワード
（名前の例：Thunderbird）
アプリパスワードのパスワードをコピーして，Thunderbirdのパスワードを更新してください。
設定完了後，Microsoft365の認証画面（大学のユーザIDとパスワード）が表示されますので，ログインして下さい。
その後、Thunderbirdの ≡設定⇒プライバシーとセキュリティ⇒保存されているパスワード から
［プロバイダー］欄に表示されている
［imap://outlook.office365.com～］および
［smtp://smtp.office365.com～］を選択し［削除］します。
（［oauth://login.microsoft.online.com～］のみとします）
接続できない場合，Thunderbirdの ≡設定⇒一般 「接続設定」にてプロキシ設定を確認して下さい。
[○ Mozilla Thunderbird 設定情報](./attached/Thunderbird_OAuth2.pdf)
### スマートフォンで使用する
スマートフォンをご利用の場合，スマートフォン用Outlookアプリをご利用ください。  
【設定例】  
* [iPhone（iOS）の場合](./attached/Outlook-iPhone.pdf)  
* [Androidの場合](./attached/Outlook-Android.pdf)  
また，iPhoneの標準メールアプリ（iOS）や Gmailアプリ（Android版）も利用できます。（Exchangeプロトコルで設定）  
【設定例】  
* [iPhone 標準メールアプリ（iOS）の場合](./attached/iPhone-exchange.pdf)  
* [Gmailアプリ（Android版）の場合](./attached/GmailAndroid.pdf)  
いずれの場合も，パソコン用メールソフト(Outlook)と併用できます。
### メールエイリアス（別名）の登録
学生は，メールエイリアス（別名）を登録できます。
メールアドレス初期値（学籍番号@naruto-u.ac.jp）の，学籍番号部分を変更したアドレスを，登録できます。
登録できるのは 在学中に １回だけ です。
[Unicorn ID Manager（ユニコーン）](https://www.naruto-u.ac.jp/unicornidm/user/naruto/login) を開いてください
 ![[1].](./img/number3_41.gif) ユーザーIDでログイン
 ![[1].](./img/number3_42.gif) メールアドレス (alias) の入力欄へ、登録を希望するメールアドレス(@より前の部分)を入力  
![[1].](./img/number3_43.gif) [更新] ボタンで保存
 ![[1].](./img/number3_44.gif) ログアウト
 ・次に該当するメールアドレスは使用できません。
  -- 過去に登録されたメールアドレス
  -- 他の人が使用しているメールアドレス
  -- 本学の教育・研究・管理運営に支障のあるメールアドレス
  -- 公序良俗を害する恐れのあるメールアドレス
 ※メールアドレス初期値（学籍番号@naruto-u.ac.jp）でも受信できます。
 ※ユーザID（学籍番号）や Microsoft365アカウント（学籍番号@naruto-u.ac.jp）は変わりません。
### メールアカウントの追加
教職員の方は，教育研究・教務事務用にメールアカウントを追加作成できます。
[ユーザID申請書](./apply/userID_f.pdf) で申請してください。
申請書内の注意事項に沿ってご記入ください。
### メーリングリストの作成
教職員の方は，教育研究・教務事務用にメーリングリストを作成できます。
[メーリングリスト申請書](./apply/mailinglist_f.pdf) で申請してください。
申請書内の注意事項に沿ってご記入ください。
