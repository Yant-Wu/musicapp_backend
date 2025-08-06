# Music App Backend

## 環境設置

### 1. 資料庫設置
- 下載並安裝 [PostgreSQL](https://www.postgresql.org/download/)
- 下載並安裝 [pgAdmin](https://www.pgadmin.org/download/) (可選，用於資料庫管理)

### 2. 啟動 PostgreSQL
- 啟動 PostgreSQL 服務
- 預設連接埠：5432 (本專案使用 8700)

### 3. 建立資料庫
使用 pgAdmin 或命令列建立資料庫：
```sql
CREATE DATABASE musicapp;
```

### 4. 安裝 Python 依賴套件
```bash
pip install -r requirements.txt
```

### 5. 啟動應用程式(用於測試開發的)
```bash
python -m uvicorn main:app --reload
```

## 資料庫連線設定
- 主機：localhost
- 連接埠：8700
- 資料庫名稱：musicapp
- 使用者名稱：postgres
- 密碼：postgres

## API 端點
- `POST /signup` - 使用者註冊

## 注意事項
- 確保 PostgreSQL 服務正在運行
- 確認資料庫連線設定正確
- 首次運行時會自動建立資料表
