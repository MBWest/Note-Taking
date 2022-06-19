# If Statements

    if [ $# -ne 2 ]
    then
        echo "Error in $0 - Invalid Argument Count"
        echo "Syntax: $0 <push|pull> <Product Name>"
        exit
    fi