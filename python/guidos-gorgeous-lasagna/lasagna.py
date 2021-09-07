EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int the number of layers in the lasagne.
    :return: int the number of minutes it will take to prepare the lasagne.

    Function that takes the number of layers in the lasagna
    an argument and returns how many minutes it will take to prepare the lasagna.
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.

    :param number_of_layers: int the number of layers in the lasagne.
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int the total number of minutes that has been spent cooking.

    Function that takes the number of layers in the lasagna and the elapsed baking time
    arguments and returns how many minutes have been spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time