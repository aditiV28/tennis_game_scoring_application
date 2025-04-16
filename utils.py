from dataclasses import dataclass

#Constants
SCORE_TO_ANNOUNCEMENT_MAP = {
    0: "love",
    1: "fifteen",
    2: "thirty",
    3: "forty"
}
DEDUCE_THRESHOLD = 3

#Creating Custom Exceptions
class NegativeTennisScoreException(Exception):
    pass

class NoScoreAtStartOfGameException(Exception):
    pass

class WonByTooManyPointsException(Exception):
    pass

class InvalidNameException(Exception):
    pass

@dataclass
class Player:
    name: str 
    score: int 

#Helper functions

#When both players have the same score
def _is_draw(player_one_score: int, player_two_score:int) -> bool:
    return player_one_score == player_two_score 

#When both players have a tied score or have won atleast 3 points
def _is_deuce(player_one_score: int, player_two_score:int) -> bool:
    return (
        player_one_score >= DEDUCE_THRESHOLD and player_two_score >= DEDUCE_THRESHOLD 
        and player_one_score == player_two_score
    )

#When one player has won one point but hasn't won the game yet
def _is_advantage(player_one_score: int, player_two_score:int) -> bool:
    return (
        player_one_score >= DEDUCE_THRESHOLD and player_two_score >= DEDUCE_THRESHOLD 
        and abs(player_one_score - player_two_score) == 1
    )

#When one player has won the game
def _has_winner(player_one_score: int, player_two_score: int) -> bool:
    return (
        (player_one_score >= 4 or player_two_score >= 4 )
        and (player_one_score - player_two_score ) == 2
    )

#Score before which players reach deuce
def _pre_deuce_score(server: Player, receiver: Player) -> str:
    if _is_draw(server.score, receiver.score):
        return f"{SCORE_TO_ANNOUNCEMENT_MAP[server.score]} all"
    return (
        f"{SCORE_TO_ANNOUNCEMENT_MAP[server.score]} "
        f"{SCORE_TO_ANNOUNCEMENT_MAP[receiver.score]}"
    )

#Validate score
def _validate_scores(server: Player, receiver: Player) -> None:
    if server.score < 0 or receiver.score < 0:
        raise NegativeTennisScoreException("Scores cannot be negatiev")

    if server.score == receiver.score == 0:
        raise NoScoreAtStartOfGameException("No tennis scores are announced at the start of the game")
    
    if server.score > 4 and abs(server.score - receiver.score) > 2:
        raise WonByTooManyPointsException("Players cannot win by more than 2 points")

#Validate player name
def _validate_name(name: str) -> str:
    name = name.strip()

    if not name:
        raise InvalidNameException("Name cannot be empty")

    if not all(char.isalpha() or char.isspace() or char in "-'" for char in name):
        raise InvalidNameException("Name must only contain letters, spaces, hyphens and apostrophe")
    
    if len(name) > 25:
        raise InvalidNameException("Name is too long. Maximum 25 characters are allowed")

    return name


