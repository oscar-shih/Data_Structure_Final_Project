RED='\033[1;31m'
GREEN='\033[1;32m'
NC='\033[0m' # No Color

echo "==evaluating correctness=="
for i in $(seq 1 5); do
    python3 parse_tree.py --input correctness/correct_${i}.txt --output pt_output_${i}.txt
    dline_py=$(diff pt_output_${i}.txt correct_ans_macOS/golden_${i}.txt |  wc | awk -F ' ' '{print $1}')
    if [ "${dline_py}" == "0" ] && [ -f pt_output_${i}.txt ] && [ -f correct_ans_macOS/golden_${i}.txt ] ; then
        echo -e "${GREEN}parse_tree.py is correct in test case: input_${i}.txt${NC}"
    else
        echo -e "${RED}parse_tree.py is incorrect in test case: input_${i}.txt${NC}"
    fi
done

for i in $(seq 1 5); do
    python3 dp.py --input correctness/correct_${i}.txt --output dp_output_${i}.txt
    dline_py=$(diff dp_output_${i}.txt correct_ans_macOS/golden_${i}.txt |  wc | awk -F ' ' '{print $1}')
    if [ "${dline_py}" == "0" ] && [ -f dp_output_${i}.txt ] && [ -f correct_ans_macOS/golden_${i}.txt ] ; then
        echo -e "${GREEN}dp.py is correct in test case: input_${i}.txt${NC}"
    else
        echo -e "${RED}dp.py is incorrect in test case: input_${i}.txt${NC}"
    fi
done

for i in $(seq 1 5); do
    python3 shunting_yard.py --input correctness/correct_${i}.txt --output sy_output_${i}.txt
    dline_py=$(diff sy_output_${i}.txt correct_ans_macOS/golden_${i}.txt |  wc | awk -F ' ' '{print $1}')
    if [ "${dline_py}" == "0" ] && [ -f sy_output_${i}.txt ] && [ -f correct_ans_macOS/golden_${i}.txt ] ; then
        echo -e "${GREEN}shunting_yard.py is correct in test case: input_${i}.txt${NC}"
    else
        echo -e "${RED}shunting_yard.py is incorrect in test case: input_${i}.txt${NC}"
    fi
done