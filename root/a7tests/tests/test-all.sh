#!/bin/bash
#
# Run all of the tests for assignment 5 of cs250
#

# The first argument is the directory of the tatt repository (the directory containint tatt.sh)
TATT_HOME=${1}
# The second argument is a directory containing all of the problem solutions
SOLUTION_HOME=${2}

echo ""
echo "------- Testing puter-1 -------"
${TATT_HOME}/tatt.sh -t ./puter-1 -s ${SOLUTION_HOME} -d -w
echo ""

popd &> /dev/null

