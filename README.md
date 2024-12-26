# 図書館システム

## プロジェクトの概要

### プロジェクトの内容

本プロジェクトは、とある小学生向け支援サービスの図書館の図書を管理するシステムです。

図書館スタッフが図書の登録、貸出、返却などを行える機能を提供します。

### プロジェクトの工程

- 開発開始 2024/10/01
- 設計 2024/10/01~2024/11/12
- 技術検証 2024/11/13~2024/11/22
- (実習参加のため一時休止 2024/11/25~2024/12/06)
- 開発 2024/12/09~2024/12/24
- テスト 2025/1/6~ (現在作業中)

## ◆ 開発環境

本プロジェクトは、Windowsのローカル環境で開発しました。

推奨ブラウザはGoogle Chromeです。

## ◆ 使用技術
- Python(Django 4)
- HTML/CSS、BootStrap
- SQLite3

## ◆ システム構成

## ◆ 設計図

### ER図
![図書館システム_データベースER図](https://github.com/user-attachments/assets/f52bd8b0-51c6-4973-8cc7-4ee99faf875e)

### ユースケース図
![図書館システム_ユースケース_v1](https://github.com/user-attachments/assets/e8cbdbbc-c3c1-47ba-aff8-84dca04b8c2c)

### システム概要図
![図書館システム概要_v1 1](https://github.com/user-attachments/assets/ce5d7d64-70b7-4efa-81ec-ec62dcdc50e5)

## ◆ 機能

### 管理者
- DjangoAdminを使ったデータ管理
  - 図書の登録、編集、削除
  - 生徒の登録、編集、削除
  - 新規スタッフの登録、編集、削除

### 図書館スタッフ
- スタッフ用管理画面からの各種処理
  - 図書の貸出処理
  - 図書の返却処理
  - 図書の貸出状況の閲覧
  - 延滞中生徒の閲覧

## ◆ デモ

### 図書を登録する流れ

1. DjangoAdminを開き、管理者ユーザーとしてログインします。
![image](https://github.com/user-attachments/assets/26bee8da-7d9c-4e55-a878-85589a0753e7)

2. 「Books」を選択します。
![image](https://github.com/user-attachments/assets/b1914c36-d566-417b-af56-d52e00295f0f)

3. 「Bookを追加」をクリックします。
![image](https://github.com/user-attachments/assets/05e203df-7c83-4af5-9624-0fdd8bc5e4fc)

4. フォームに情報を入力し、保存ボタンをクリックします。これで図書が登録できます。
![image](https://github.com/user-attachments/assets/9bd40a09-1aeb-4ae9-baa5-68e469f154e0)


### 図書貸し出しの流れ

1. システムを開き、スタッフとしてログインします。
![image](https://github.com/user-attachments/assets/a65a35a9-39a7-4231-b28a-1103faca5b78)

2. 「貸し出し」ボタンをクリックします。
![image](https://github.com/user-attachments/assets/f76f40ea-dafc-4e88-a0e7-9d0ef49c288a)

3. 生徒のIDと図書のIDを入力し、「貸出する」ボタンをクリックします。
![image](https://github.com/user-attachments/assets/dd072388-c8c7-4516-8907-dbef974ca5a0)

4. 貸出が完了しました。
![image](https://github.com/user-attachments/assets/6bad25b7-780b-45ea-afac-918435e7b7df)


### 図書返却の流れ

1. システムを開き、スタッフとしてログインします。
![image](https://github.com/user-attachments/assets/a65a35a9-39a7-4231-b28a-1103faca5b78)

2. スタッフとしてログインした後、「返却」ボタンをクリックします。
![image](https://github.com/user-attachments/assets/f76f40ea-dafc-4e88-a0e7-9d0ef49c288a)

3. 図書のIDを入力し、「返却する」をクリックします。
![image](https://github.com/user-attachments/assets/ad921946-c6f8-433b-b28f-fc866924cd68)

4. 返却が完了しました。
![image](https://github.com/user-attachments/assets/764b5e62-c781-4164-aeee-82eef917ee62)


### 延滞中生徒の確認

延滞中の生徒はトップ画面から一覧として表示されます。
![image](https://github.com/user-attachments/assets/affdbfdd-dc47-4e4b-86a8-96c8beec0f5b)

生徒一覧からも延滞中の生徒を閲覧できます。
![image](https://github.com/user-attachments/assets/a28ceacd-0510-400c-9043-bc728831a2e0)
