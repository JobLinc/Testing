from ..helper import User
from ..conftest import HomePage


def test_post_job(home_page: HomePage) -> None:
    """Test if you can post a job."""
    jobs_page = home_page.bottom_nav.navigate_to_jobs()
    jobs_page.get_all_jobs()
