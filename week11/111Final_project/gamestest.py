import pytest
import io
from unittest.mock import patch
import unittest
from games import generate_word
from games import get_hint
from games import guess_fiveth_word
from games import handle_match_choice
from games import select_item
from games import handle_run_choice
from games import handle_hide_choice
from games import ignore_it_choice
from games import go_up_and_see_choice
from games import enter_the_paradise
from games import return_to_original_place_choice
from games import interesting_road_choice
from games import the_path_that_looks_eerie_choice
from games import handle_check_it_out_choice
from games import handle_keep_running_choice

def test_generate_word():
    # Test generating a word of length 5 with complexity 0.5
    word = generate_word(5, 0.5)
    assert len(word) == 5
    assert len(set(word)) >= 3

    # Test generating a word of length 8 with complexity 0.6
    word = generate_word(9, 0.6)
    assert word is None

    # Test generating a word of length 3 with complexity 0.1
    word = generate_word(3, 0.1)
    assert word is None

def test_get_hint():
    # Test getting hint for a correct guess
    word = "orang"
    guess_word = "orang"
    hint = get_hint(word, guess_word)
    assert hint == "O R A N G "

    # Test getting hint for an incorrect guess
    word = "orang"
    guess_word = "apple"
    hint = get_hint(word, guess_word)
    assert hint == "a _ _ _ _ "

    # Test getting hint for a partially correct guess
    word = "orang"
    guess_word = "orege"
    hint = get_hint(word, guess_word)
    assert hint == "O R _ g _ "

class TestGuessColorWord(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correct_guess(self, mock_stdout):
        word = 'green'
        with patch('builtins.input', side_effect=['green']):
            guess_fiveth_word(len(word), complexity=0, max_guesses=1, time_limit=10)
        expected_output = f"Congratulations! It took you 1 guess(es).\n"
        # self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_guesses(self, mock_stdout):
        word = 'apple'
        with patch('builtins.input', side_effect=['blueo', 'yello']):
            guess_fiveth_word(len(word), complexity=0, max_guesses=2, time_limit=10)
        expected_output = f"Your hint is: _ _ _ _ _ \nYour hint is: _ _ _ _ _ \nSorry, you ran out of guesses. The word was '{word}'.\n"
        # self.assertEqual(mock_stdout.getvalue(), expected_output)

def test_select_item():
    with patch('builtins.input', side_effect=["match"]):
        assert select_item() == "match"
    with patch('builtins.input', side_effect=["flashlight"]):
        assert select_item() == "flashlight"

def test_handle_match_choice():
    with patch('builtins.input', side_effect=["run","go",""]):
    # Test the "run" choice
        assert handle_match_choice() == handle_run_choice()
    # Test the "hide" choice
    with patch('builtins.input', side_effect=["hide","stand",""]):
        assert handle_match_choice() == handle_hide_choice()

def test_handle_run_choice():
    # Test the "check it out" choice
    with patch('builtins.input', side_effect=["check it out","not check",""]):
        assert handle_run_choice() == handle_check_it_out_choice()
    # Test the "keep running" choice
    with patch('builtins.input', side_effect=["keep running","stay",""]):
        assert handle_run_choice() == handle_keep_running_choice()

def test_handle_check_it_out_choice():
    # Test the "stay" choice
    with patch('builtins.input', side_effect=["stay","action","go out"]):
        assert handle_check_it_out_choice() == ignore_it_choice()
    # Test the "follow" choice
    with patch('builtins.input', side_effect=["follow","stay",""]):
        assert handle_check_it_out_choice() == go_up_and_see_choice()

def test_handle_keep_running_choice():
    # Test the "go up" choice
    with patch('builtins.input', side_effect=["go up","go right",""]):
        assert handle_keep_running_choice() == go_up_and_see_choice()
    # Test the "ignore" choice
    with patch('builtins.input', side_effect=["ignore","check",""]):
        assert handle_keep_running_choice() == ignore_it_choice()

# # def test_go_up_and_see_choice():
# #     # Test the "enter" choice
# #     with patch('builtins.input', side_effect=["enter","outside",""]):
# #         assert go_up_and_see_choice() == enter_the_paradise()
# #     # Test the "return" choice
# #     with patch('builtins.input', side_effect=["return","go back",""]):
# #         assert go_up_and_see_choice() == return_to_original_place_choice()
# import turtle
# import time
# from unittest.mock import patch

# def test_go_up_and_see_choice():
#     # Initialize Turtle window
#     T = turtle.Turtle()
#     T.screen.setup(400, 400)
#     T.screen.tracer(0)
    
#     # Test the "enter" choice
#     with patch('builtins.input', side_effect=["enter","outside",""]):
#         assert go_up_and_see_choice() == enter_the_paradise()
    
#     # Reset Turtle window
#     T.screen.clear()
#     T.screen.tracer(1)
    
#     # Test the "return" choice
#     with patch('builtins.input', side_effect=["return","go back",""]):
#         assert go_up_and_see_choice() == return_to_original_place_choice()
        
#     T.screen.bye()  # close the turtle screen



def test_return_to_original_place_choice():
    # Test the "interesting" choice
    with patch('builtins.input', side_effect=["interesting","boring",""]):
        assert return_to_original_place_choice() == interesting_road_choice()
    # Test the "eerie" choice
    with patch('builtins.input', side_effect=["eerie","excite",""]):
        assert return_to_original_place_choice() == the_path_that_looks_eerie_choice()


pytest.main(["-v", "--tb=line", "-rN", __file__])