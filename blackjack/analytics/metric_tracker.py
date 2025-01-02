class MetricTracker:
    """Class for tracking game metrics for analytics purposes."""

    def __init__(self):
        # Metrics
        self.wins = 0
        self.losses = 0
        self.pushes = 0
        self.insurance_wins = 0
        self.insurance_losses = 0
        self.gambler_blackjacks = 0
        self.dealer_blackjacks = 0

        # Bankroll over time
        self.bankroll_progression = []

        # Track win/loss results
        self.wins_losses = []

    def _increment_metric(self, metric):
        """Increment the desired metric (privately)."""
        if metric == 'turns':
            self.turns += 1
        elif metric == 'wins':
            self.wins += 1
            self.wins_losses.append('win')
        elif metric == 'losses':
            self.losses += 1
            self.wins_losses.append('loss')
        elif metric == 'pushes':
            self.pushes += 1
        elif metric == 'insurance wins':
            self.insurance_wins += 1
        elif metric == 'insurance losses':
            self.insurance_losses += 1
        elif metric == 'gambler blackjacks':
            self.gambler_blackjacks += 1
        elif metric == 'dealer blackjacks':
            self.dealer_blackjacks += 1
        else:
            raise ValueError(f"Unsupported metric: {metric}")

    def process_gambler_hand(self, hand):
        """Track metrics for a played GamblerHand"""
        # Blackjacks
        if hand.status == 'Blackjack':
            self._increment_metric('gambler blackjacks')

        # Outcomes
        if hand.outcome in ('Win', 'Even Money'):
            self._increment_metric('wins')
        elif hand.outcome == 'Loss':
            self._increment_metric('losses')
        elif hand.outcome == 'Push':
            self._increment_metric('pushes')
        elif hand.outcome == 'Insurance Win':
            self._increment_metric('insurance wins')
        else:
            raise ValueError(f"Unsupported hand outcome: {hand.outcome}")

        # Insurance Losses (side bet, separate from 'Outcomes')
        if hand.lost_insurance:
            self._increment_metric('insurance losses')

    def process_dealer_hand(self, hand):
        """Track metrics for a played DealerHand."""
        if hand.status == 'Blackjack':
            self._increment_metric('dealer blackjacks')

    def append_bankroll(self, bankroll):
        """Append a bankroll amount to the list of bankrolls tracked."""
        self.bankroll_progression.append(bankroll)

    def serialize_metrics(self):
        """Get a dictionary representation of tracked metrics."""
        return {
            'wins': self.wins,
            'losses': self.losses,
            'pushes': self.pushes,
            'insurance_wins': self.insurance_wins,
            'insurance_losses': self.insurance_losses,
            'gambler_blackjacks': self.gambler_blackjacks,
            'dealer_blackjacks': self.dealer_blackjacks,
            'bankroll_progression': self.bankroll_progression,
            'wins_losses': self.wins_losses
        }
