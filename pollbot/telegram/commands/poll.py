"""Poll related commands."""
from telegram.ext import run_async

from pollbot.helper.session import session_wrapper
from pollbot.helper.display.creation import get_init_text
from pollbot.telegram.keyboard import (
    get_init_keyboard,
    get_poll_list_keyboard,
)

from pollbot.models import Poll


@run_async
@session_wrapper(private=True)
def create_poll(bot, update, session, user):
    """Create a new poll."""
    # The previous unfinished poll will be removed
    if user.current_poll is not None and  \
            not user.current_poll.created and \
            not len(user.current_poll.votes) > 0:
        session.delete(user.current_poll)

    poll = Poll(user)
    user.current_poll = poll
    session.add(poll)
    session.commit()

    text = get_init_text(poll)
    keyboard = get_init_keyboard(poll)

    update.message.chat.send_message(text, parse_mode='markdown', reply_markup=keyboard)


@run_async
@session_wrapper(private=True)
def list_polls(bot, update, session, user):
    """Get a list of all active polls."""
    text = 'Click on any button to manage this specific poll.'
    polls = session.query(Poll) \
        .filter(Poll.user == user) \
        .filter(Poll.created.is_(True)) \
        .filter(Poll.closed.is_(False)) \
        .filter(Poll.deleted.is_(False)) \
        .all()

    if len(polls) == 0:
        return "You don't own any active polls."

    keyboard = get_poll_list_keyboard(polls)
    update.message.chat.send_message(text, reply_markup=keyboard)


@run_async
@session_wrapper(private=True)
def list_closed_polls(bot, update, session, user):
    """Get a list of all active polls."""
    text = 'Click on any button to manage this specific poll.'
    polls = session.query(Poll) \
        .filter(Poll.user == user) \
        .filter(Poll.created.is_(True)) \
        .filter(Poll.closed.is_(True)) \
        .filter(Poll.deleted.is_(False)) \
        .all()

    if len(polls) == 0:
        return "You don't own any closed polls."

    keyboard = get_poll_list_keyboard(polls)
    update.message.chat.send_message(text, reply_markup=keyboard)


@run_async
@session_wrapper(private=True)
def delete_all(bot, update, session, user):
    """Get a list of all active polls."""
    session.query(Poll) \
        .filter(Poll.user == user) \
        .update({'deleted': True})

    return "All polls have been deleted"
