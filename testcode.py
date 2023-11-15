import unittest
from unittest.mock import patch
from  lhampygame import check_winner, update_user_score, update_computer_score, update_choice

class TestRockPaperScissorGame(unittest.TestCase):

    @patch('lhampygame.update_message')
    def test_check_winner_equal(self, mock_update_message):
        check_winner("rock", "rock")
        mock_update_message.assert_called_with("EQUAL!")

    @patch('lhampygame.update_user_score')
    def test_update_user_score(self, mock_update_user_score):
        update_user_score()
        mock_update_user_score.assert_called_once()

    @patch('lhampygame.update_computer_score')
    def test_update_computer_score(self, mock_update_computer_score):
        update_computer_score()
        mock_update_computer_score.assert_called_once()

    @patch('lhampygame.user_label')
    @patch('lhampygame.computer_label')
    def test_update_choice(self, mock_user_label, mock_computer_label):
        update_choice("rock")
        mock_user_label.configure.assert_called_with(image=mock_user_label["image"])
        mock_computer_label.configure.assert_called_with(image=mock_computer_label["image"])

if __name__ == '__main__':
  unittest.main()

