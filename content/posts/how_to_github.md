---
title: "Github によるサイト管理のすゝめ（CLI 版）"
date: 2023-03-06T11:19:09+09:00
tags: []
featured_image: "https://thurrott.s3.amazonaws.com/wp-content/uploads/sites/2/2023/01/GitHub.jpeg"
description: ""
draft: true
---

---
- [Github から clone もしくは pull](#github-から-clone-もしくは-pull)
- [作業ブランチの作成](#作業ブランチの作成)
- [記事作成・編集](#記事作成編集)
- [ローカルの main ブランチに作業ブランチをマージ](#ローカルの-main-ブランチに作業ブランチをマージ)
- [ローカルの main ブランチを Github に push](#ローカルの-main-ブランチを-github-に-push)
- [本番環境に pull](#本番環境に-pull)

---

# Github から clone もしくは pull
テストサイトのソースファイルを
{{<exlink href="https://github.com/Yuu-Miino-NUE/nue_official_web.git" text="Github">}}
にアップロードしました．

> git はバージョン管理プログラム
> Github は git リポジトリを Web にアップロードできるサービスです．

```shell
$ git clone --recursive https://github.com/Yuu-Miino-NUE/nue_official_web.git
```

サブモジュールも合わせて `clone` する場合には，`--recursive` オプションを付与します．

`clone` はイニシャルセットアップなので，二回目以降は必要ありません．

その代わりに，開発環境を最新の状態にするために，作業前には必ず `pull` しましょう．

```shell
$ git pull --all
```

# 作業ブランチの作成
複数人での作業を想定するため，編集を施す際にはブランチを切りましょう．
例えば，`feature/miino_logs` という名前のブランチを切る場合，下記のコマンドを実行します．

```shell
$ git branch feature/miino_logs         # ブランチ作成
$ git checkout feature/miino_logs       # ブランチへ移動

$ git checkout -b feature/miino_logs    # ブランチを作成してそこへ移動
```

ブランチをどう切るかは，組織によって予め取り決めておくのが基本のようです．
代表的な運用方法として，git flow や github flow などがあります．
両者を比較する記事は，多く存在します．例えば
{{<exlink href="https://www.geeksforgeeks.org/git-flow-vs-github-flow/" text="コチラ">}} など．

# 記事作成・編集
`hugo new <記事のパス>` で記事テンプレートを作成．

```shell
$ hugo new logs/miino_logs_20230306.md
```

あとはお好きなエディタで Markdown ファイルを修正します．
[別記事]({{<ref "how_to_write">}}) で執筆についていくらかまとめました．

小まめに `commit`（セーブ）した方が良いでしょう．

```shell
$ git commit -am '執筆：Github から clone'
```

コミットが貯れば，リモートにも `push` しておきましょう．

```shell
$ git push -u origin feature/miino_logs
```

> 二回目以降は `git push` のみでリモートにアップできます．

ローカル環境での記事確認は開発用サーバにて．

```shell
$ hugo server -D
```

`-D` は下書きも表示（コンパイル）するオプション．

# ローカルの main ブランチに作業ブランチをマージ
Github のデフォルトブランチは `main` です．
> `git` のデフォルトは `master` ですが，Github では `main` です．

`feature/miino_logs` での変更内容を `main` に統合（`merge`）します．
`merge` をする前にはかならず，ローカルの `main` ブランチを最新のものにしておきます．

```shell
$ git pull origin main
```

> 自分で切ったブランチを他の人も使っている，という場合には，
> `git pull --all` とした方が良いでしょう．

準備が整ったら，`main` ブランチにマージします．
`main` ブランチに移動（`checkout`）して，`feature/miino_logs` をマージします．

```shell
$ git checkout main
$ git merge feature/miino_logs
```

競合（`conflict`）がなければ，コメントを書いて統合完了です．

マージ後は作業ブランチを削除しましょう．

```shell
$ git branch -d feature/miino_logs      # ローカル
$ git push origin -d feature/miino_logs # リモート（Github）
```

# ローカルの main ブランチを Github に push
```shell
$ git push origin main
```

# 本番環境に pull
本番環境で最新の `main` ブランチを `pull` します．

```shell
$ git pull origin main
```

この行程は，Github Actions で自動化できます．
具体的には，「`main` ブランチが変更されれば，本番環境にデプロイする」という
プログラムを組めます．