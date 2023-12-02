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
1. スケジュール実行するプロジェクトのAPIを有効にする
    - Cloud Scheduler API 
1. スケジュール登録


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
gcloud builds submit \
        --config cloudbuild.yaml \
        --project {projectId}
```

### バッチジョブ実行

```bash
gcloud batch jobs submit {jobName} \
    --location asia-northeast1 \
    --config batchjob.json
```

### ワークフロー作成

```bash
gcloud workflows deploy batch-python-job \
        --source=batch-workflow.yaml \
        --location=asia-northeast1 \
        --project {projectId}
```

### スケジュール登録

- 10分おきに実行する例

```bash
gcloud scheduler jobs create http {schedulerName} \
        --schedule="*/10 * * * *" \
        --uri="https://workflowexecutions.googleapis.com/v1/projects/{projectId}/locations/asia-northeast1/workflows/{workflowsName}/executions" \
        --message-body="{}" \
        --time-zone="Asia/Tokyo" \
        --location="asia-northeast1" \
        --oauth-service-account-email="[サービスアカウント]" \
        --project {projectId}
```

## 参考情報

- [GCP Batchを使ってみる①](https://engineer-boost.com/google-cloud/?p=355)
- [GCP Batchを使ってみる②](https://engineer-boost.com/google-cloud/?p=801)
- [GCP Batchを使ってみた](https://recruit.gmo.jp/engineer/jisedai/blog/gcp-batch/)
- [Google Cloud で "バッチ ジョブ" を実行する 2 つの方法](https://zenn.dev/google_cloud_jp/articles/c99697707e3b2c)

