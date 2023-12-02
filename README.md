Google Cloud Batchを利用するサンプル
====================

## 手順

### バッチコンテナ登録＆実行

1. Batch ジョブを実行するプロジェクトのAPIを有効にする
    - Batch API
    - Artifact Registry API
    - Cloud Build API
1. Artifact Registry リポジトリを作成する
1. Batchジョブスクリプトを作成する
1. 実行コンテナ用のDockerfileを作成する
1. Artifact Registryにコンテナを登録するビルド構成ファイルを作成する
1. gcloudコマンドを使用してコンテナをビルドする
1. gcloudコマンドを使用してバッチジョブ実行する

### バッチスケジュール実行

1. WorkflowsのAPIを有効にする
1. ジョブ起動・実行監視用ワークフロー作成する



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

### gcloudコマンドを使用してコンテナをビルドする

```bash
gcloud builds submit --config cloudbuild.yaml --project {projectId}
```

### バッチジョブ実行

```bash
gcloud batch jobs submit {jobName} --location asia-northeast1 --config batchjob.json
```

### ワークフロー作成

```bash
gcloud workflows deploy batch-python-job \
        --source=batch-workflow.yaml \
        --location=asia-northeast1 \
        --project {projectId}
```

## 参考情報

- [GCP Batchを使ってみる](https://engineer-boost.com/google-cloud/?p=355)
