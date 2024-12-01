# %%
"""Test for build-deb."""

from __future__ import annotations

import pytest

from repo_utilities.apt.build_deb import extract_homepage_desc


@pytest.mark.parametrize(
    ("cask_or_formula", "desc", "homepage"),
    [
        (
            "go",
            "Open source programming language to build simple/reliable/efficient software",  # noqa: E501
            "https://go.dev/",
        ),
        (
            "ollama",
            "Create, run, and share large language models (LLMs)",
            "https://ollama.com/",
        ),
    ],
)
def test_extract_homepage_desc(cask_or_formula: str, desc: str, homepage: str) -> None:
    """Test the extract_homepage_desc function."""
    extracted_desc, extracted_homepage = extract_homepage_desc(cask_or_formula)
    assert extracted_desc == desc
    assert extracted_homepage == homepage
