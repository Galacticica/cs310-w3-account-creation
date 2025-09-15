# CS310 - W3 Account Creation
By Reagan Zierke

## How did you store the values used later in the confirmation?
I stored them by declaring variables such as `$USERNAME`.

## How did you create the `username` value?
I utilized the translate (`tr`) function changing uppercase to lowercase and changing spaces to -.
`tr '[:upper:]' '[:lower:]' | tr ' ' '-'`