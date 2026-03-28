from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Manages tournament registration, matches, and leaderboard."""

    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}
        self.matches: List[dict] = []

    def register_card(self, card: TournamentCard) -> str:
        """Register a card and return its assigned ID."""
        short = card.name.split()[-1].lower()
        count = sum(1 for cid in self.cards if cid.startswith(short))
        card_id = f"{short}_{(count + 1):03d}"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulate a match between two cards, update ratings."""
        if card1_id not in self.cards or card2_id not in self.cards:
            return {"error": "One or both card IDs not found"}

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)      # internally calls calculate_rating()
        loser.update_losses(1)     # internally calls calculate_rating()

        result = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }
        self.matches.append(result)
        return result

    def get_leaderboard(self) -> list:
        """Return cards sorted by rating, highest first."""
        sorted_cards = sorted(
            self.cards.items(),
            key=lambda item: item[1].rating,
            reverse=True
        )
        leaderboard = []
        rank = 1
        for card_id, card in sorted_cards:
            leaderboard.append({
                "rank": rank,
                "name": card.name,
                "rating": card.rating,
                "record": f"{card.wins}-{card.losses}"
            })
            rank += 1
        return leaderboard

    def generate_tournament_report(self) -> dict:
        """Generate full platform statistics."""
        ratings = [c.rating for c in self.cards.values()]
        avg_rating = sum(ratings) // len(ratings) if ratings else 0
        return {
            "total_cards": len(self.cards),
            "matches_played": len(self.matches),
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
