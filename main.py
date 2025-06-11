import streamlit as st
import chess
import chess.svg

st.title("체스 겜빗 오프닝 가이드")

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

# 2단계: 세부 라인 선택
line_type = st.selectbox("라인 선택", list(gambits[gambit_type].keys()))

# 3단계: 세부 변형 선택
variation = st.selectbox("변형 선택", list(gambits[gambit_type][line_type].keys()))

# 선택된 변형 정보 가져오기
info = gambits[gambit_type][line_type][variation]

st.subheader(f"{variation} ({line_type})")
st.write(info["description"])
st.code(info["moves"])

def parse_moves(moves_str):
    parts = moves_str.split()
    moves = []
    for p in parts:
        if p.endswith('.'):
            continue
        moves.append(p)
    return moves

moves_list = parse_moves(info["moves"])

board = chess.Board()

# ▶▶▶ 겜빗 진행 순서 단계별 보여주기 추가

st.subheader("겜빗 진행 단계별")

for i in range(1, len(moves_list)+1):
    step_moves = moves_list[:i]
    board_tmp = chess.Board()
    for move_san in step_moves:
        try:
            move = board_tmp.parse_san(move_san)
            board_tmp.push(move)
        except:
            pass
    svg_partial = chess.svg.board(board=board_tmp, size=300)
    st.markdown(f"**Step {i}: {move_san}**")
    st.components.v1.html(svg_partial, height=320)

# 전체 수순 적용한 체스판 출력 (마지막)
svg_board = chess.svg.board(board=board, size=400)
for move_san in moves_list:
    try:
        move = board.parse_san(move_san)
        board.push(move)
    except:
        pass
st.subheader("최종 위치")
st.components.v1.html(svg_board, height=420)
