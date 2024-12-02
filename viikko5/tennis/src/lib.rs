pub trait Game {
    fn clear(&mut self);
    fn won_point(&mut self, player_name: &str);
    fn get_score(&self) -> String;
}

#[derive(Default)]
pub struct TennisGame {
    score1: u8,
    score2: u8,
    _player1_name: String,
    _player2_name: String,
}

trait TennisScore {
    fn as_score(&self) -> String;
    fn as_score_tied(&self) -> String;
}
impl TennisScore for u8 {
    fn as_score(&self) -> String {
        match self {
            3 => "Forty",
            2 => "Thirty",
            1 => "Fifteen",
            _ => "Love",
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

impl TennisGame {
    pub fn new() -> Self {
        Self::default()
    }
}

impl Game for TennisGame {
    fn clear(&mut self) {
        self.score1 = 0;
        self.score2 = 0;
    }
    fn won_point(&mut self, player_name: &str) {
        if player_name == "player1" {
            self.score1 += 1;
        } else {
            self.score2 += 1;
        }
    }
    fn get_score(&self) -> String {
        match (self.score1, self.score2) {
            (a, b) if a == b => a.as_score_tied(),
            (a, b) if a >= 4 || b >= 4 => {
                let minus_result = self.score1 as i8 - self.score2 as i8;
                if minus_result == 1 {
                    return "Advantage player1".to_owned();
                } else if minus_result == -1i8 {
                    return "Advantage player2".to_owned();
                } else if minus_result >= 2 {
                    return "Win for player1".to_owned();
                }
                "Win for player2".to_owned()
            }
            _ => {
                let mut temp_score: u8;
                let mut score = String::new();
                for i in 1..3 {
                    if i == 1 {
                        temp_score = self.score1;
                    } else {
                        score.push_str("-");
                        temp_score = self.score2;
                    }
                    score.push_str(&temp_score.as_score());
                }
                return score;
            }
        }
    }
}
