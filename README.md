# gpt_playground
```bash
python3 -m venv .kvenv
source .kvenv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload

ngrok http 8000
```
