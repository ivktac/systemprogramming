граматиика { S -> KB, K -> aK, K -> e, B -> bBc, B -> e} контекстно-вільна, оскільки:

- права частина містить лише один нетермінал

- ліва частина містить лише один нетермінал

- правила мають вигляд A -> α, де α – це або термінал, або нетермінал і може бути пустим

1. aaaabcc

S -> KB, правило S -> KB
-> aKB, правило K -> aK
-> aaKB, правило K -> aK
-> aaaKB, правило K -> aK
-> aaaaKB, правило K -> aK
-> aaaaB, правило K -> e
-> aaaabBc, правило B -> bBc,
-> aaaabbBcc, правило B -> bBc,
-> aaaabbcc, правило B -> e

не належить

2. aabbcc

S -> KB, правило S -> KB
-> aKB, правило K -> aK
-> aaKB, правило K -> aK
-> aaB, правило K -> e
-> aabBc, правило B -> bBc,
-> aabbBcc, правило B -> bBc,
-> aabbcc, правило B -> e

належить

3. bca

S -> KB, правило S -> KB
-> B, правило K -> e
-> bBc, правило B -> bBc,
-> bc, правило B -> e

не належить

4. aaaabc

S -> KB, правило S -> KB
-> aKB, правило K -> aK
-> aaKB, правило K -> aK
-> aaaKB, правило K -> aK
-> aaaaKB, правило K -> aK
-> aaaaB, правило K -> e
-> aaaabBc, правило B -> bBc,
-> aaaabc, правило B -> e

5. abbbccc

S -> KB, правило S -> KB
-> aKB, правило K -> aK
-> aB, правило K -> e
-> abBc, правило B -> bBc,
-> abbBcc, правило B -> bBc,
-> abbbBccc, правило B -> bBc,
-> abbbccc, правило B -> e

підходить