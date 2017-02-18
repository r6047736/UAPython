#!/bin/bash
#
# Run all of the tests for assignment 3 of cs250
#

# The first argument is the directory of the tatt repository (the directory containint tatt.sh)
TATT_HOME=${1}
# The second argument is a directory containing all of the problem solutions
SOLUTION_HOME=${2}

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pushd ${DIR} &> /dev/null

echo ""
echo "------- Testing todo -------"
${TATT_HOME}/tatt.sh -t ./todo -s ${SOLUTION_HOME}
echo ""

echo ""
echo "------- Testing star-wars -------"
${TATT_HOME}/tatt.sh -t ./star-wars -s ${SOLUTION_HOME}
echo ""

echo ""
echo "------- Testing 007 -------"
${TATT_HOME}/tatt.sh -t ./007 -s ${SOLUTION_HOME} 
echo ""

popd &> /dev/null

