from ..pages.screens.home_page import HomePage


def test_remove_invitation(home_page: HomePage):
    network_page = home_page.bottom_nav.navigate_to_my_network()

    initial_invitations = network_page.get_invitations()
    assert initial_invitations, "No invitations found to remove"

    invitation_to_remove = initial_invitations[0]["name"]

    network_page.remove_invitation(invitation_to_remove)

    updated_invitations = network_page.get_invitations()

    assert invitation_to_remove not in [
        inv["name"] for inv in updated_invitations
    ], f"Invitation '{invitation_to_remove}' was not removed"


def test_accept_invitation(home_page: HomePage):
    network_page = home_page.bottom_nav.navigate_to_my_network()

    initial_invitations = network_page.get_invitations()
    assert initial_invitations, "No invitations found to remove"

    invitation_to_accept = initial_invitations[0]["name"]

    network_page.accept_invitation(invitation_to_accept)

    updated_invitations = network_page.get_invitations()

    assert invitation_to_accept not in [
        inv["name"] for inv in updated_invitations
    ], f"Invitation '{invitation_to_accept}' was not accepted"
