import streamlit as st
import chess
import chess.svg

st.title("체스 겜빗 오프닝 가이드")

# 겜빗 데이터 (퀸스 겜빗 상세 확장 포함)
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
                "moves": "1. d4 d5 2. c4 dxc4 3. Nf3 Nf6 4. e3 e6 5. Bxc4 c5",
                "description": "퀸스 겜빗 수락 변형의 대표적인 메인라인"
            }
        },
        "Declined": {
            "Main Line": {
                "moves": "1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7",
                "description": "퀸스 겜빗 거절 변형의 기본 메인라인"
            },
            "Tarrasch Defense": {
                "moves": "1. d4 d5 2. c4 e6 3. Nc3 c5",
                "description": "퀸스 겜빗 거절 - 타라슈 변형"
            }
        }
    }
}

# Step 1~3 선택
gambit_type = st.selectbox("겜빗 종류 선택", list(gambits.keys()))
line_type = st.selectbox("라인 선택", list(gambits[gambit_type].keys()))
variation = st.selectbox("변형 선택", list(gambits[gambit_type][line_type].keys()))

info = gambits[gambit_type][line_type][variation]

st.subheader(f"{variation} ({line_type})")
st.write(info["description"])

def parse_moves(moves_str):
    parts = moves_str.split()
    moves = []
    for p in parts:
        if p.endswith('.'):
            continue
        moves.append(p)
    return moves

moves_list = parse_moves(info["moves"])

# 체스 보드 상태 저장용 세션 상태 변수 초기화
if "move_index" not in st.session_state:
    st.session_state.move_index = 0

col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("◀ 이전 수"):
        if st.session_state.move_index > 0:
            st.session_state.move_index -= 1

with col3:
    if st.button("다음 수 ▶"):
        if st.session_state.move_index < len(moves_list):
            st.session_state.move_index += 1

st.write(f"진행 수: {st.session_state.move_index} / {len(moves_list)}")

# 현재까지 수만큼 체스판 그리기
board = chess.Board()
for i in range(st.session_state.move_index):
    try:
        move = board.parse_san(moves_list[i])
        board.push(move)
    except:
        pass

svg_board = chess.svg.board(board=board, size=400)
st.components.v1.html(svg_board, height=420)
