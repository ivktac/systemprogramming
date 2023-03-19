EBNF

<word> :: = 's1'<meta>'a'<meta>
<meta> ::= "{" <LETTER> ", <DIGIT> "}"

<LETTER> := "a" | "b" | ... | "z" | "A" | ... | "Z"
<DIGIT> := "0" | "1" | "2" | ... | "9"