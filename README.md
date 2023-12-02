Google Cloud Batchを利用するサンプル
====================

## 手順

1. Batch ジョブを実行するプロジェクトのAPIを有効にする
    - Batch API
    - Artifact Registry API
    - Cloud Build API
1. Artifact Registry リポジトリを作成する
1. Batchジョブスクリプトを作成する
1. 実行コンテナ用のDockerfileを作成する
1. Artifact Registryにコンテナを登録するビルド構成ファイルを作成する
1. gcloudコマンドを使用してコンテナをビルドする
    ```bash
    gcloud builds submit --config cloudbuild.yaml --project {projectId}
    ```

## 使い方

### venv

- activate
    ```fish
    # fishの場合
    source .venv/bin/activate.fish
    ```

- deactive
    ```bash
    deactivate
    ```

## 参考情報

- [GCP Batchを使ってみる](https://engineer-boost.com/google-cloud/?p=355)
