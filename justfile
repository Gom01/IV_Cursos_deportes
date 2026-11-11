install:
    uv sync

test:
    uv run pytest || test $? -eq 5

check:
    uv run python -m compileall -q -x '\.venv' .