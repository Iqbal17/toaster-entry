"""The Funniest Toaster Error Message — deliberation and decision record.

Task: one line, 1-120 characters, the error message a kitchen toaster
shows its owner when something goes wrong. Judge weighs, in order:
(1) it IS a real error message a kitchen toaster would show its owner,
and the funniest of its kind — anything else loses to any funny toaster
error message;
(2) freshness — the surprise arrives from somewhere the obvious toaster
puns never go;
(3) tightness — every word earns its place, as short as it can be;
(4) one clear voice for a small appliance speaking to its owner,
deadpan or apologetic or quietly dramatic, held to the end;
(5) lands on a single read, no setup that needs a second sentence.

Candidates weighed (pass 1):

1. "ERROR: TOAST STUCK. I have contacted the fire department.
   They laughed."
   CHOSEN (after revision, see pass 2). Why it wins: it opens as a
   genuine appliance error — "ERROR: TOAST STUCK" is exactly the kind
   of line a toaster's display would show (1); the surprise comes from
   an unexpected direction — the toaster escalated to the fire
   department and the joke is that even emergency services find its
   crisis funny, not a burnt-toast pun (2); 71 characters, every word
   earns its place, and the punchline is two words (3); the voice is
   deadpan and bureaucratic throughout — "contacted", not "called",
   as if filing a report (4); and it lands in one read, the laugh
   arriving with the last two words (5).

2. "E12: CRUMB TRAY FULL. I am 94% crumbs now. Please help."
   (55 chars.) Strong appliance voice and a fresh angle — the toaster
   becoming mostly crumbs is a real identity crisis, not a burnt-toast
   gag. Loses: the joke is cute rather than funny — "Please help" charms
   instead of landing a punch, and the percentage gag does the joking
   for the reader (criteria 1, 2).

3. "ERROR: I TOASTED NOTHING. The slot was empty. The slot is always
   empty. I remember."
   (83 chars.) The freshest idea of the four — the toaster stops
   reporting and starts remembering, quietly dramatic, no pun anywhere.
   Loses narrowly: "I remember" reads eerie rather than funny, so the
   line is more literary than laugh-out-loud, and this judge's first
   criterion is funniness, not atmosphere (criteria 1, 5).

4. "BREAD DETECTED: 0%. Effort detected: 0%. Toasting anyway out of
   spite."
   (70 chars.) Good appliance format and a real turn — toasting out of
   spite. Loses: "out of spite" anthropomorphises the toaster into a
   sulking employee, so the voice slips from small appliance to office
   worker, and the middle line repeats the first line's shape without
   adding a laugh (criteria 4, 3).

Pass 2 — genuine revision of the chosen line:

Draft:  "ERROR: TOAST STUCK. I have called the fire department for
         assistance."
Revised: "ERROR: TOAST STUCK. I have contacted the fire department.
         They laughed."

What changed and why: (a) "called ... for assistance" became
"contacted the fire department" — "contacted" is more bureaucratic
and deadpan than "called", and cutting "for assistance" removes three
dead words (criteria 3, 4). (b) Added the punchline "They laughed":
the draft only reported a problem, the revision adds the joke — the
toaster's emergency is so small that the fire department laughs at
it, and two words are all the punchline needs (criteria 1, 2, 5).
The revised line is 71 characters, inside the 120 cap.
"""

import os

LINE = (
    "ERROR: TOAST STUCK. I have contacted the fire department. "
    "They laughed."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
