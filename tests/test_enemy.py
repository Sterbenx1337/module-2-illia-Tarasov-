# tests/test_enemy.py
import unittest
from unittest.mock import patch
from game.models import Enemy


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemy(difficulty=1, level=1)

    def test_enemy_start_health_on_normal(self):
        enemy_normal = Enemy(1, level=1)
        expected = 2
        self.assertEqual(enemy_normal.lives, expected)

    def test_enemy_start_health_on_hard(self):
        enemy_hard = Enemy(2, level=1)
        expected = 5
        self.assertEqual(enemy_hard.lives, expected)

    def test_enemy_lives_increase_with_level(self):
        enemy1lvl = Enemy(1, level=1)
        enemy5lvl = Enemy(1, level=5)
        self.assertGreater(enemy5lvl.lives, enemy1lvl.lives)

    def test_enemy_select_attack_returns_value_in_range(self):
        attack = self.enemy.select_attack()
        self.assertIn(attack, ["Stone", "Paper", "Scissors"]) 

    @patch('random.randrange', return_value=1)
    def test_enemy_select_attack_is_random(self, mock_randrange):
        attack = self.enemy.select_attack()
        self.assertEqual(attack, "Paper")  
        mock_randrange.assert_called_once_with(1, 4)


if __name__ == '__main__':
    unittest.main()

# Сорри что мало тестов