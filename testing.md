# Testing

To use the python unittest module to use your homework:

1) Navigate to directory Learn_Python/HW
2) run `python -m unittest -v`
3) The -v will make it list each test individually. You should be able to review the tests in something like the following:
```
test_Card_beats (test_HW4.TestHW4_1) ... FAIL
test_Card_get_full_deck (test_HW4.TestHW4_1) ... ok
test_Card_get_int_value (test_HW4.TestHW4_1) ... ok
test_Card_init (test_HW4.TestHW4_1) ... ok
test_Card_is_red (test_HW4.TestHW4_1) ... FAIL
test_Card_matches (test_HW4.TestHW4_1) ... FAIL
test_count_suits (test_HW4.Test_HW4_2) ... ok
test_count_values (test_HW4.Test_HW4_2) ... FAIL
test_deal_cards (test_HW4.Test_HW4_2) ... FAIL
test_draw_cards (test_HW4.Test_HW4_2) ... FAIL
test_flush (test_HW4.Test_HW4_2) ... FAIL
test_straight (test_HW4.Test_HW4_2) ... FAIL
```
4) You will also get additional information about why tests fail. Use these to figure out why your implementations are failing.
```
======================================================================
FAIL: test_Card_is_red (test_HW4.TestHW4_1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bscaramella\Documents\Personal\Learn_Python\HW\test_HW4.py", line 41, in test_Card_is_red
    self.assertTrue(HW4_1.Card("Diamonds","4").is_red())
AssertionError: False is not true
```
5) To run a specific test alone, use `python -m unittest -v -k "[name of test]"`. For example: `python -m unittest -v -k "test_Card_is_red"