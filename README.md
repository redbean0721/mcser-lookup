# mcser-lookup
只需輸入起始和結束 IP 以及 PORT 即可掃描 IP 區間內所有 Minecraft 伺服器狀態

## 使用說明

> 運行環境 建議 `Python 3.8` 以上(含)

### 安裝依賴項
```bash
pip install -r requirements.txt
```

### 運行程式
```bash
python main.py
```

### 選項說明
- `Enter the starting IP`: 起始 IP
- `Enter the ending IP`: 結束 IP
- `Enter the port`: 伺服器 PORT
- `Enter delay time(ms)`: 最大延遲時間 (單位為毫秒 ms)

<br>

> ⚠️**重要提示: 目前只支持 *Minecraft Java* 版本使用, 暫不支持 Minecraft Bedrock 版本**