# Phase 07: Integration Validation ★

## 審查進度

- [x] 07.1 相關規格已審查 — **簽名**: 2026-09-18 14:43
- [x] 07.2 交付物已審查 — **簽名**: 2026-09-18 14:43

## 目的 (What)

驗證前端（Phase 06）與後端（Phase 05）透過真實 HTTP 連線能正確協作。

**這不是「加一個檢查」— 這是正式的 Phase**，有完整的 2 步審查。

來源：從 CRM 專案 6 個整合問題中提煉的 architectural fix。
兩條獨立 track 各自通過測試 ≠ 合在一起能跑。

核心動作：前端關閉 MSW mock → rewrite proxy → 打真實後端 API。

**IMPL_IMPACT 感知**：若 Phase 05 或 Phase 06 有任何 Targeted Fix，Phase 07 自動觸發完整重驗（不可跳過）。Targeted Fix 改了前後端的局部，整合驗證確認局部修復沒有破壞全局。

**依賴**：Phase 05 + Phase 06 都必須在 `done/` 中。

## 相關規格

| # | 規格 | 來源 | 說明 |
|---|------|------|------|
| 1 | api.yml | Phase 04 | 契約 = 驗證基準 |
| 2 | Chrome Test Guard 測試計畫 | Phase 06 | 同一份測試計畫，換 real backend 重跑 |

## 交付物

carry-on Step 07.2 觸發時：

### 1. 啟動後端

```bash
# 方式 A: Docker
docker-compose up -d

# 方式 B: venv
source venv/bin/activate && uvicorn app.main:app --port 8000
```

健康檢查：`curl http://localhost:8000/health`

### 2. 前端環境切換

修改 `C:\Users\retailingdata\Desktop\ruby\HikePilot/frontend/.env.development`：
```
NEXT_PUBLIC_MOCK_API=false
BACKEND_URL=http://localhost:8000
```

### 3. 驗證矩陣（5 項）

詳見 `references/integration-matrix.md`。

| # | 驗證項目 | 方法 |
|---|---------|------|
| 1 | Response envelope 格式 | 打 API → 檢查 `{success, data/error}` 結構 |
| 2 | 欄位名一致性 | 前端 type vs 後端 response vs api.yml |
| 3 | Auth flow | login → cookie → authenticated request |
| 4 | Query params 完整性 | 前端傳參 vs 後端接參 |
| 5 | Error handling | 觸發 4xx/5xx → 前端正確顯示 |

### 4. Chrome E2E 重跑

用 Chrome E2E 重跑 Phase 06 的 Chrome Test Guard 測試計畫（real backend mode）。

### 5. 問題修正迴圈

發現問題 → 定位（前端 / 後端 / 契約）→ 修正 → 重跑 → 直到全部通過。

| # | 交付物 | 路徑 | 狀態 |
|---|--------|------|------|
| 07.1 | Chrome E2E 結果（real backend） | 全通過 | DONE |
| 07.2 | 驗證矩陣通過紀錄 | 4/5 通過，1 項無適用 endpoint（Query Params，本 API 無 GET 帶參數端點） | DONE |

### 驗收點

- [x] 後端啟動且健康檢查通過
- [x] 前端 `MOCK_API=false` 且 rewrite proxy 正確
- [x] 驗證矩陣 5 項全部通過（或標註不適用）
- [x] Chrome E2E real 模式全數通過

### 發現並修復的整合問題

1. **API base path 不一致**：前端假設 `/api/v1`，api.yml 與後端實際為 `/api`（無版本前綴）。
   統一為 `/api`（`.env.development`、`client.ts`、4 個 MSW handler）。
2. **後端未在真實啟動流程建立 DB session factory**：`app/main.py` 新增 `lifespan`，
   啟動時用 `settings.DATABASE_URL` 建立 engine 並呼叫 `set_session_factory`。
   Behave 測試（`TestClient` 未用 `with`）不受影響，15/15 場景仍全過。
3. **api.yml 契約缺口**：`GoogleLoginResponse` 從未定義 token 欄位，導致登入後無法通過真實
   JWT 驗證。api.yml 補上 `token`，後端簽發 JWT（`player_name`=user.id），前端登入頁改存
   真正回傳的 token，MSW mock 同步補上以維持雙模式一致。

次要觀察（非阻擋）：`route` 表 migration 的 enum 值為大寫（`MODERATE`/`OPEN`），
與 `erm.dbml` 標註的小寫不一致；目前無 API response 曝露此欄位，暫不影響外部契約。
