---
title: Miino's log, the 1st day
date: 2023-03-02T16:12:35+09:00
draft: true
---

- [概要](#概要)
- [インストール](#インストール)
- [クイックスタートと細かな設定](#クイックスタートと細かな設定)
- [開発用サーバの起動](#開発用サーバの起動)
- [記事の追加](#記事の追加)
  - [基本](#基本)
  - [画像挿入](#画像挿入)
  - [外部リンク](#外部リンク)

## 概要

せっかくなので，`hugo` の設定作業ログを残すことにしました．
自分でサイトを作ってみたい，という方はお試しください．

---

## インストール

{{<exlink href="https://gohugo.io/getting-started/quick-start/" text="公式ドキュメント">}} に従って `hugo` をインストールします．

MacOS の場合，`brew` でインストールできます．

```shell
$ brew install hugo
```

## クイックスタートと細かな設定

一回設定したらあとから参照することはあまりなさそうなので，[別ページ](/logs/miino_logs_sub1) にまとめました．

## 開発用サーバの起動

```bash
$ hugo server -D
```

`-D` オプションはドラフト（下書き）も変換・表示する，というオプションです．

## 記事の追加

### 基本
`content` ディレクトリに Markdown[^1] や HTML を追加すれば，サイトに反映されます．
例えば，`content/posts` 直下に次の内容の `my-first-post.md` を配置します．

[^1]: {{<exlink href="https://gohugo.io/content-management/formats/#learn-markdown" text="Learn Markdown">}}
でお勉強しましょうね，と公式に書いてありました．

```markdown
---
title: "テスト投稿"
date: 2023-03-02T16:12:35+09:00
draft: true
---

# 導入

これは導入テストです．


```

すると，`localhost:1313/posts/my-first-post/` に Web ページが生成されます．

ファイルの書き始めに *Front matter* を入れておけば，色々と制御できます．
({{<exlink href="https://gohugo.io/content-management/front-matter/" text="Front matter の公式ドキュメント">}})

Front matter を含んだ Markdown テンプレートを生成したい場合には，下記コマンドを実行します．

```shell
$ hugo new posts/my-first-post.md
```

`draft: true` では，下書きのままなので，公開するぞというときには `false` にしましょう．

> #### 余談
> ##### ホットリロード
> 最近の開発用サーバはホットリロードを標準搭載しており，`Hugo` もその例から漏れないようです．
> 開発用サーバを起動中に Markdown ファイルを保存すると，コンパイルなどせずとも直ちに（開発環境上の） Web ページ反映されます．
> 便利です．
> ##### `_index.md`
> `Hugo` では，`_index.md` というファイルがインデックスページとして認識されるようです．
> ({{<exlink href="https://gohugo.io/content-management/organization/#index-pages-_indexmd" text="公式ドキュメント参照">}})


### 画像挿入
画像は `static/images` フォルダに保存します．
保存した画像は，例えば次のようにして参照できます．

```markdown
![alt text](/images/center.png "マウスオーバー！")
![リンク切れだよ](/images/sonna_file_naiyo.png)
```

出力結果：

![alt text](/images/center.png "マウスオーバー！")

![リンク切れだよ](/images/dummy.png)

### 外部リンク
外部リンクは新しいウィンドウで開いてもらいたい，ですよね？
一般的な Markdown には直接 HTML を書き込むこともできますが，`Hugo` の場合は
少し設定をいじる必要があります．
面倒なので，`shortcodes` という機能を使って実装してみましょう．

`/layouts` フォルダには何度でも使い回すようなテンプレートを保存します．
`shortcodes` もそこに保存するようです．
`/layouts/shortcodes` というフォルダを作り，フォルダ内に `exlink.html` というファイルを作成しましょう．
中には以下のように記述します．

```go
{{ if .IsNamedParams }}
<a href="{{ .Get "href" }}" target="_blank" rel="noopener noreferrer">{{ if .Get "text"}}{{ .Get "text" }}{{ else }}{{ .Get "href"}}{{ end }}</a>
{{ else }}
<a href="{{ .Get 0 }}" target="_blank" rel="noopener noreferrer">{{ .Get 0 }}</a>
{{ end }}
```

> `Hugo` は Golang で書かれている訳ですが，上記の記法は Go の
> `html/template` および `text/template` ライブラリに実装されているロジックだそうです．
> ({{<exlink href="https://gohugo.io/templates/introduction/#example-4-if--else" text="公式ドキュメント">}})

`shortcodes` の使い方は以下のとおり，ファイル名で呼び出します．
例の他にもいくつかパラメタの指定方法がありますが，割愛します．詳細は参考先をご確認ください．

```html
参考：{{</*exlink href="https://blog.foresta.me/posts/hugo_shortcode_for_external_link/" text="Hugoで外部リンクを開くためのshortcodeを作った話"*/>}}
```

参考：{{<exlink href="https://blog.foresta.me/posts/hugo_shortcode_for_external_link/" text="Hugoで外部リンクを開くためのshortcodeを作った話">}}