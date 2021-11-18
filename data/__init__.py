"""Read test or example data."""

from os.path import join as pjoin, dirname


DATA_DIR = pjoin(dirname(__file__))

TEST_FILES = {
    "issue_data": pjoin(DATA_DIR, "issue_data.json"),
    "expected_project_4_file": pjoin(DATA_DIR, "expected_project_4.md"),
    "expected_project_9_file": pjoin(DATA_DIR, "expected_project_9.md"),
}
