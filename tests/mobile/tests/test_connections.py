from ..pages.screens.home_page import HomePage


def test_remove_connection(home_page: HomePage):
    connections_page = home_page.sidebar.navigate_to_connections()

    initial_connections = connections_page.get_connections()
    assert initial_connections, "No connections found to remove"

    connection_to_remove = initial_connections[0]["name"]

    connections_page.remove_connection(connection_to_remove)

    updated_connections = connections_page.get_connections()

    assert connection_to_remove not in [
        conn["name"] for conn in updated_connections
    ], f"Connection '{connection_to_remove}' was not removed"
