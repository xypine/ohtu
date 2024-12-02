mod tennis;
pub use tennis::TennisGame;

pub trait Game {
    fn clear(&mut self);
    fn won_point(&mut self, player_name: &str);
    fn get_score(&self) -> String;
}
