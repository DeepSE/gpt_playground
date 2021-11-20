# gpt_playground
카카오에서 공개한 https://huggingface.co/kakaobrain/kogpt 를 사용하여 간단히 issue에 글을 올리면 답장을 다는 방식으로 테스트 해볼수 있습니다. 결과들을 같이 볼수 있도록 하기 위해 깃헙 이슈 방식을 사용하였습니다. 

제목은 무시하고 본문만 prompt로 이용합니다.

![image](https://user-images.githubusercontent.com/901975/142714843-1cc785f0-b16e-4638-a010-27999799bb6d.png)

저의 연구실 학생에게 3090GPU 하나 빌려서 사용해서 응답이 좀 느리거나 불안정 할수 있습니다. 
공개해준 카카오에게 감사합니다.

### 간략 셋업
```bash
python3 -m venv .kvenv
source .kvenv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload

ngrok http 8000
```
### Contributions
코드 PR은 언제나 환영입니다.
