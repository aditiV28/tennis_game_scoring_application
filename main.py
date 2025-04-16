from utils import (
    Player,
    _is_deuce,
    _is_advantage,
    _has_winner,
    _pre_deuce_score,
    _validate_scores,
    _validate_name,
    InvalidNameException
)

#Scoring logic
def get_tennis_score(server: Player, receiver: Player) -> str:
    _validate_scores(server, receiver)

    if _is_deuce(server.score, receiver.score):
        return "deuce"

    if _is_advantage(server.score, receiver.score):
        leading = server if server.score > receiver.score else receiver
        return f"advantage {leading.name}"

    if _has_winner(server.score, receiver.score):
        winner = server if server.score > receiver.score else receiver
        return f"{winner.name} wins"

    return _pre_deuce_score(server, receiver)

#Score validation
def safe_int_input(score: str) -> int:
    while True:
        try:
            val = int(input(score))
            if val < 0:
                raise ValueError("Score must be non-negative")
            return val
        except ValueError as e:
            print(f"Invalid input: {e}")

#Name validation
def safe_str_input(name: str) -> str:
    while True:
        try:
            raw_input = input(name)
            return _validate_name(raw_input)
        except InvalidNameException as e:
            print(f"Invalid input for name: {e}")

def main():
    server_name = safe_str_input("Enter server name: ")
    server_score = safe_int_input("Enter server score: ")

    receiver_name = safe_str_input("Enter receiver name: ")
    receiver_score = safe_int_input("Enter receiver score: ")
    
    server = Player(name=server_name, score=server_score)
    receiver = Player(name=receiver_name, score=receiver_score)

    try:
        result = get_tennis_score(server, receiver)
        print(f"{server.name} vs {receiver.name} -> {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

    '''test_cases = [
        (Player("Serena", 2), Player("Venus", 0), "thirty love"),
        (Player("Serena", 3), Player("Venus", 3), "deuce"),
        (Player("Serena", 4), Player("Venus", 3), "advantage Serena"),
        (Player("Serena", 5), Player("Venus", 3), "Serena wins"),
        (Player("Serena", 1), Player("Venus", 1), "fifteen all"),
    ]

    for server, receiver, expected in test_cases:
        result = get_tennis_score(server, receiver)
        print(f"{server.name} vs {receiver.name} | Expected: {expected} | Got: {result}")'''