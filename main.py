import streamlit as st
from streamlit_chessboard import chessboard

st.title("체스 겜빗 오프닝 가이드")

# 겜빗 오프닝 계층 구조 (예시)
gambits = {
    "English Gambit": {
        "Trap Line": {
            "Fool's Mate Trap": {
                "moves": "1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 b6 8. cxd5 Nxd5 9. Bxe7 Qxe7 10. Nxd5 exd5",
                "description": "잉글리시 겜빗 트랩라인에서 백이 상대의 실수를 유도하는 트랩"
            },
            "Other Trap": {
                "moves": "1. d4 d5 2. c4 c6 3. Nc3 Nf6",
                "description": "잉글리시 겜빗의 다른 트랩"
            }
        },
        "Main Line": {
            "Classical": {
                "moves": "1. d4 d5 2. c4 e6",
                "description": "클래식한 잉글리시 겜빗 진행"
            }
        }
    },
    "Queen's Gambit": {
        "Accepted": {
            "Main Line": {
                "moves": "1. d4 d5 2. c4 dxc4",
                "description": "퀸스 겜빗 수락 변형"
            }
        },
        "Declined": {
            "Main Line": {
                "moves": "1. d4 d5 2. c4 e6",
                "description": "퀸스 겜빗 거절 변형"
            }
        }
    }
}

# 1단계: 겜빗 종류 선택
gambit_type = st.selectbox("겜빗 종류 선택", list(gambits.keys()))

# 2단계: 세부 라인 선택 (예: Trap Line, Main Line 등)
line_type = st.selectbox("라인 선택", list(gambits[gambit_type].keys()))

# 3단계: 세부 변형 선택
variation = st.selectbox("변형 선택", list(gambits[gambit_type][line_type].keys()))

# 선택된 변형 정보 가져오기
info = gambits[gambit_type][line_type][variation]

# 설명 출력
st.subheader(f"{variation} ({line_type})")
st.write(info["description"])
st.code(info["moves"])

# 체스판 위에 수순 표시
# streamlit-chessboard는 PGN 형식을 바로 지원하지 않으므로, moves를 PGN 변환 필요. 간단한 공백 기준 수순 리스트로 표시 가능.

# moves 문자열 -> 리스트 변환 (예: '1. d4 d5 2. c4 e6' -> ['d4','d5','c4','e6'])
def parse_moves(moves_str):
    parts = moves_str.split()
    moves = []
    for p in parts:
        if p.endswith('.'):
            continue
        moves.append(p)
    return moves

moves_list = parse_moves(info["moves"])

# 체스판 위에 현재 상태 표시
# streamlit-chessboard의 chessboard() 함수에 moves= 리스트 형태로 넘겨서 초기 위치 세팅 가능
chessboard(moves=moves_list)
