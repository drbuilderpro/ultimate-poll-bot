"""Get the different texts for polls and management."""
from pollbot.helper import poll_is_cumulative
from pollbot.helper.enums import (
    UserSorting,
    OptionSorting,
)


def get_sorted_votes(poll, votes):
    """Sort the votes depending on the poll's current settings."""
    def get_user_name(vote):
        """Get the name of user to sort votes."""
        return vote.user.name

    if poll.user_sorting == UserSorting.user_name.name:
        votes.sort(key=get_user_name)

    return votes


def get_sorted_options(poll, total_user_count=0):
    """Sort the options depending on the poll's current settings."""
    options = poll.options.copy()

    def get_option_name(option):
        """Get the name of the option."""
        return option.name

    def get_option_percentage(option):
        """Get the name of the option."""
        return calculate_percentage(option, total_user_count)

    if poll.option_sorting == OptionSorting.option_name.name:
        options.sort(key=get_option_name)

    elif poll.option_sorting == OptionSorting.option_percentage.name:
        options.sort(key=get_option_percentage, reverse=True)

    return options


def calculate_percentage(option, total_user_count):
    """Calculate the percentage for this option."""
    if poll_is_cumulative(option.poll):
        option_vote_count = sum([vote.vote_count for vote in option.votes])
        poll_vote_count = sum([vote.vote_count for vote in option.poll.votes])

        if poll_vote_count == 0:
            return 0

        percentage = round(option_vote_count/poll_vote_count * 100)

    else:
        if total_user_count == 0:
            percentage = 0
        else:
            percentage = round(len(option.votes)/total_user_count * 100)

    return percentage


# Import for easier re-export
from .poll import * # noqa
from .management import * # noqa
from .settings import * # noqa
