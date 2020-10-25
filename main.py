"""
This python script will use various functions to provide predictive information about 2020 Presedential Winners
"""

from pprint import pprint

from getData import getPollData
from us_electoral import ec_result, state_raw2win

if __name__ == "__main__":
    # Fetch raw Poll results
    pollData = getPollData()
    # Convert raw results to a winner by state
    state_results = state_raw2win(pollData)
    # Print the processed results by state
    pprint(state_results)
    # Return the winner (First entry) from the ordered dict from the ec_result function
    winner2020 = next(iter(ec_result(state_results)))
    print("*" * 30)
    print("2020 US Presedential Winner predected to be: {}".format(winner2020))  # Print Poll Results by state
    print("*" * 30)
