# writing-kit

WaTTsonの日本語長文執筆のためのガイドライン集。ブログ記事などのまとまった論を展開する文章や、議論の内容を箇条書きでまとめた文書を書くための、文体・論の進め方・表記の規約をまとめている。

## 構成

- `guidelines/`：スタイルガイドライン本体
    - `common_guideline.md`：全文書共通のガイド。箇条書き・散文のどちらで書くときも適用される。認識の帰属・命題/概念の扱い・修辞・論の進め方・読者の前提・引用出典・表記・Markdown
    - `style_article.md`：ブログやConfluenceなどの記事を、です・ます調の散文で書くためのスタイルガイド。文体・語り口の表現形・段落の作り方・つなぎの言い回し・本文中の箇条書きの運用
    - `style_academic.md`：論文のような硬めの論説文を、だ・である調の散文で書くためのスタイルガイド。構成は`style_article.md`と同じ
    - `style_bullet.md`：箇条書きを地の文とする文書のスタイルガイド。基本形式・認識の帰属・並び順とまとまり・ネスト・文献の書き方
- `skills/`：agent skill定義
    - `write/`：トピック・素材・議論の内容などから、guidelineに従って箇条書きまたは散文の文書を書く
    - `style-review/`：書いた文書（箇条書きまたは散文）を該当guidelineに照らしてレビューする

各skillは、トップレベルの `guidelines/` を、skillのディレクトリから見た `../../guidelines/` として読み込む。

## guidelineを直接参照する

`guidelines/` 配下のファイルを執筆時に手元で参照する。または、AIツール（Claude Code等）に読み込ませて執筆・レビュー補助に使う。何を書くときも `common_guideline.md` を土台にし、散文なら用途に応じて `style_article.md` / `style_academic.md` を、箇条書きなら `style_bullet.md` を重ねて使う。

## pluginとして使う

Claude CodeとCodexのどちらでも、pluginとして使える。repositoryをmarketplaceとして登録し、writing-kit pluginをインストールする。

Claude Codeの場合：

```
claude plugin marketplace add Watson496/writing-kit
claude plugin install writing-kit@writing-kit
```

Codexの場合：

```
codex plugin marketplace add Watson496/writing-kit
codex plugin add writing-kit@writing-kit
```

pluginから提供されるskillは、`writing-kit:write`、`writing-kit:style-review`という名前で利用できる。skillは、skill名または近い自然言語で起動する：

- 執筆：「文書にまとめて」「記事を書いて」「箇条書きの文書にして」「本文に起こして」「writing-kitで書いて」など
- style review：「文体チェックして」「style-review」「writing-kitのguidelineに照らしてレビューして」など

## release手順

Claude Code用のマニフェスト（`.claude-plugin/plugin.json`）とCodex用のマニフェスト（`.codex-plugin/plugin.json`）の両方の`version`を正とし、releaseのtag `vX.Y.Z` はそこから導出する。`version`を上げるPRをmainにmergeすると、`.github/workflows/release.yml`がtagとreleaseを作成する。

1. mainを最新にする

    ```
    git switch main
    git pull
    ```

2. [Semantic Versioning](https://semver.org/lang/ja/)に従い、直前のtag以降の変更から、patch / minor / majorのどれに当たるかを決める。1.0.0未満の間は、後方互換性のない変更でもminorを上げる

3. `version`を上げるPRを作る

    - 両方のマニフェストの`version`を同じ値に書き換える
    - ブランチ：`chore/release-vX.Y.Z`
    - commit / PRタイトル：`chore(release): vX.Y.Z`
    - PRの中身は`version`の更新のみとする
    - PR本文に、直前のtag以降の変更と、増分の根拠を書く

4. PRをmergeする。mergeすると、releaseのworkflowが`vX.Y.Z`のtagとreleaseを作成する。release noteは、直前のrelease以降にmergeされたPRから自動生成される

5. ActionsでReleaseのworkflowが成功したことと、Releasesページで`vX.Y.Z`のtagが`version`を上げたcommitを指していることを確認する
