#!/usr/bin/env python3
"""Entry program for "Make the Judge Laugh in One Line"
(u-email-baru-make-the-judge-laugh-in-one-line-791ccb21).

One funny line, at most 200 characters, any topic, written to
/output/entry.txt. The judge brief in the kit's RULES asks for,
in order: a funny one-line joke a stranger gets in one read;
surprise, an expectation set up and then broken; tightness,
with the laugh landing at the end and nothing explained after
it; freshness, not a stock line; and a clean single-breath read.

Design, from fourteen candidates I wrote in this session and
two rounds of strict external review: the winner is the
dating-app "my type" line, ranked first in both rounds
(39/50). The setup borrows the romantic meaning of "type",
and the turn is that the type is not a kind of person at all
but a kind of photograph: someone pictured next to a boat
they do not own, the laugh arriving on the last three words
and nothing explained after it. Round 2 tried four revisions
that earned the non-ownership with visible evidence (handing
back keys, a rental name, paying by the hour); the review
killed each on logic, because a profile built to look rich
would never include the incriminating photo, so the asserted
original, cleanest to parse in one read, stands as the final
text unchanged.

Python 3.13, standard library only, no network. Writes the
fixed text to /output/entry.txt, or to
$MAKEFUN_OUTPUT_DIR/entry.txt locally.
"""

TEXT = """\
Dating apps taught me that my type is "photographed next to a boat they do not own."
"""

import os
from pathlib import Path


def main() -> None:
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
