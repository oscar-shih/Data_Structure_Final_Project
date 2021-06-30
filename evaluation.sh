RED='\033[1;31m'
GREEN='\033[1;32m'
NC='\033[0m' # No Color
echo "==evaluating correctness=="
for i in $(seq 1 2); do
    python shunting_yard.py --input test_data/input_${i}.txt --output test_data/output_${i}.txt
    dline_py=$(diff output_${i}.txt test_ans/golden_${i}.txt |  wc | awk -F ' ' '{print $1}')
    if [ "${dline_py}" == "0" ] && [ -f output_${i}.txt ] && [ -f test_ans/golden_${i}.txt ] ; then
        echo -e "${GREEN}shunting_yard.py is correct in test case: input_${i}.txt${NC}"
    else
        echo -e "${RED}shunting_yard.py is incorrect in test case: input_${i}.txt${NC}"
    fi
done
