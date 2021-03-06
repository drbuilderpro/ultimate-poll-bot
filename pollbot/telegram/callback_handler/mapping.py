from pollbot.helper.enums import CallbackType

from .creation import (
    toggle_anonymity,
    change_poll_type,
    show_poll_type_keyboard,
    all_options_entered,
    toggle_results_visible,
    open_creation_datepicker,
    close_creation_datepicker,
    skip_description,
    cancel_creation,
    back_to_creation_init,
    open_init_anonymization_settings,
)
from .menu import (
    go_back,
    show_deletion_confirmation,
    show_close_confirmation,
    show_settings,
    show_vote_menu,
    show_menu,
)
from .management import (
    delete_poll,
    delete_poll_with_messages,
    close_poll,
    reopen_poll,
    reset_poll,
    clone_poll,
)
from .settings import (
    make_anonymous,
    show_anonymization_confirmation,
    show_styling_menu,
    expect_new_option,
    show_remove_options_menu,
    remove_option,
    toggle_allow_new_options,
    toggle_allow_sharing,
    open_new_option_datepicker,
    open_due_date_datepicker,
    open_language_picker,
    change_poll_language,
)
from .styling import (
    toggle_percentage,
    toggle_option_votes,
    toggle_date_format,
    toggle_summerization,
    set_option_order,
    set_user_order,
    toggle_compact_buttons,
    open_option_order_menu,
    increase_option_index,
    decrease_option_index,
)
from .datepicker import (
    pick_creation_date,
    pick_creation_weekday,
    pick_additional_date,
    pick_additional_weekday,
    pick_due_date,
    pick_external_date,
    set_next_month,
    set_previous_month,
)
from .external import (
    activate_notification,
    open_external_datepicker,
    open_external_menu,
    external_cancel,
)
from .vote import handle_vote

from .user import (
    change_user_language,
    init_poll,
    delete_all,
    delete_all_confirmation,
    delete_closed,
    delete_closed_confirmation,
    delete_user,
    list_polls,
    list_closed_polls,
    open_help,
    open_language_menu,
    open_main_menu,
    open_donation,
    open_user_settings,
    toggle_notification,
)
from .misc import (
    switch_help,
    show_option_name,
    ignore,
)
from .admin import (
    open_admin_settings,
    plot,
    update_all,
)


# Some callbacks should be synchronous, since they do database operations that
# lead to integrity/unique constraint errors when run asynchronously.
callback_mapping = {
    # Creation
    CallbackType.all_options_entered: all_options_entered,
    # Poll management
    CallbackType.delete: delete_poll,
    CallbackType.delete_poll_with_messages: delete_poll_with_messages,
    CallbackType.clone: clone_poll,
    # Settings
    CallbackType.settings_remove_option: remove_option,
    # Styling
    CallbackType.settings_increase_option_index: increase_option_index,
    CallbackType.settings_decrease_option_index: decrease_option_index,
    # User
    CallbackType.user_delete_all: delete_all,
    CallbackType.user_delete: delete_user,
    CallbackType.user_delete_closed: delete_closed,
    # Datepicker
    CallbackType.pick_creation_date: pick_creation_date,
    CallbackType.pick_creation_weekday: pick_creation_weekday,
    CallbackType.pick_additional_date: pick_additional_date,
    CallbackType.pick_additional_weekday: pick_additional_weekday,
    CallbackType.pick_external_date: pick_external_date,
}


async_callback_mapping = {
    # Creation
    CallbackType.show_poll_type_keyboard: show_poll_type_keyboard,
    CallbackType.change_poll_type: change_poll_type,
    CallbackType.toggle_anonymity: toggle_anonymity,
    CallbackType.toggle_results_visible: toggle_results_visible,
    CallbackType.open_creation_datepicker: open_creation_datepicker,
    CallbackType.close_creation_datepicker: close_creation_datepicker,
    CallbackType.skip_description: skip_description,
    CallbackType.cancel_creation: cancel_creation,
    CallbackType.back_to_init: back_to_creation_init,
    CallbackType.anonymity_settings: open_init_anonymization_settings,
    # Voting
    CallbackType.vote: handle_vote,
    # Menu
    CallbackType.menu_back: go_back,
    CallbackType.menu_vote: show_vote_menu,
    CallbackType.menu_option: show_settings,
    CallbackType.menu_delete: show_deletion_confirmation,
    CallbackType.menu_show: show_menu,
    CallbackType.menu_close: show_close_confirmation,
    # Poll management
    CallbackType.close: close_poll,
    CallbackType.reopen: reopen_poll,
    CallbackType.reset: reset_poll,
    # Settings
    CallbackType.settings_anonymization_confirmation: show_anonymization_confirmation,
    CallbackType.settings_anonymization: make_anonymous,
    CallbackType.settings_show_styling: show_styling_menu,
    CallbackType.settings_new_option: expect_new_option,
    CallbackType.settings_show_remove_option_menu: show_remove_options_menu,
    CallbackType.settings_toggle_allow_new_options: toggle_allow_new_options,
    CallbackType.settings_toggle_allow_sharing: toggle_allow_sharing,
    CallbackType.settings_open_add_option_datepicker: open_new_option_datepicker,
    CallbackType.settings_open_due_date_datepicker: open_due_date_datepicker,
    CallbackType.settings_open_language_picker: open_language_picker,
    CallbackType.settings_change_poll_language: change_poll_language,
    # Styling
    CallbackType.settings_toggle_percentage: toggle_percentage,
    CallbackType.settings_toggle_option_votes: toggle_option_votes,
    CallbackType.settings_toggle_date_format: toggle_date_format,
    CallbackType.settings_toggle_summarization: toggle_summerization,
    CallbackType.settings_user_sorting: set_user_order,
    CallbackType.settings_option_sorting: set_option_order,
    CallbackType.settings_toggle_compact_buttons: toggle_compact_buttons,
    CallbackType.settings_open_option_order_menu: open_option_order_menu,
    # User
    CallbackType.init_poll: init_poll,
    CallbackType.user_menu: open_main_menu,
    CallbackType.user_settings: open_user_settings,
    CallbackType.user_language_menu: open_language_menu,
    CallbackType.user_change_language: change_user_language,
    CallbackType.user_toggle_notification: toggle_notification,
    CallbackType.user_list_polls: list_polls,
    CallbackType.user_list_closed_polls: list_closed_polls,
    CallbackType.open_help: open_help,
    CallbackType.donate: open_donation,
    CallbackType.user_delete_all_confirmation: delete_all_confirmation,
    CallbackType.user_delete_closed_confirmation: delete_closed_confirmation,
    # Admin
    CallbackType.admin_settings: open_admin_settings,
    CallbackType.admin_plot: plot,
    CallbackType.admin_update: update_all,
    # Datepicker
    CallbackType.pick_due_date: pick_due_date,
    CallbackType.next_month: set_next_month,
    CallbackType.previous_month: set_previous_month,
    # External
    CallbackType.activate_notification: activate_notification,
    CallbackType.external_open_datepicker: open_external_datepicker,
    CallbackType.external_open_menu: open_external_menu,
    CallbackType.external_cancel: external_cancel,
    # Misc
    CallbackType.switch_help: switch_help,
    CallbackType.show_option_name: show_option_name,
    # Ignore
    CallbackType.ignore: ignore,
}


def get_callback_mapping_regex():
    """Get a filter regex to match synchronous callbacks"""
    regex = ""
    for key, _ in callback_mapping.items():
        if regex != "":
            regex += "|"

        regex += f"^{key.value}:.*"

    return regex


def get_async_callback_mapping_regex():
    """Get a filter regex to match asynchronous callbacks"""
    regex = ""
    for key, _ in async_callback_mapping.items():
        if regex != "":
            regex += "|"

        regex += f"^{key.value}:.*"

    return regex
