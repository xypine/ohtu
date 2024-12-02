use crate::Game;

const TENNIS_WINNING_SCORE: u8 = 4;
const TENNIS_TIEBRAKE_DIFF: i8 = 2;
pub struct TennisGame {
    score1: u8,
    score2: u8,
    _player1_name: String,
    _player2_name: String,
}


impl TennisGame {
    pub fn new() -> Self {
        Self::default()
    }
    fn endgame_score(&self) -> String {
        let score_difference = self.score1 as i8 - self.score2 as i8;

        let situation = match score_difference.abs() {
            ..TENNIS_TIEBRAKE_DIFF => "Advantage",
            _ => "Win for"
        };
        let player_in_advantage = match score_difference {
            0.. => self._player1_name.clone(),
            ..0 => self._player2_name.clone(),
        };

        format!("{situation} {player_in_advantage}")
    }
}
impl Default for TennisGame {
    fn default() -> Self {
        Self {
            _player1_name: "player1".to_owned(),
            _player2_name: "player2".to_owned(),
            score1: 0,
            score2: 0
        }
    }
}

impl Game for TennisGame {
    fn clear(&mut self) {
        self.score1 = 0;
        self.score2 = 0;
    }
    fn won_point(&mut self, player_name: &str) {
        match player_name {
            name if name == self._player1_name => self.score1 += 1,
            name if name == self._player2_name => self.score2 += 1,
            _ => panic!("Unknown player name") 
        }
    }
    fn get_score(&self) -> String {
        match (self.score1, self.score2) {
            (a, b) if a == b => a.as_score_tied(),
            (a, b) if a >= TENNIS_WINNING_SCORE || b >= TENNIS_WINNING_SCORE => {
                self.endgame_score()
            }
            _ => {
                let score1 = self.score1.as_score();
                let score2 = self.score2.as_score();
                format!("{score1}-{score2}")
            }
        }
    }
}

trait TennisScore {
    fn as_score(&self) -> String;
    fn as_score_tied(&self) -> String;
}
impl TennisScore for u8 {
    fn as_score(&self) -> String {
        match self {
            0 => "Love",
            1 => "Fifteen",
            2 => "Thirty",
            3 => "Forty",
            _ => "Game"
        }.to_owned()
    }
    fn as_score_tied(&self) -> String {
        if *self > 2 {
            return "Deuce".to_owned();
        }
        let score = self.as_score();
        format!("{score}-All")
    }
}
