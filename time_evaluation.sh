RED='\033[1;31m'
GREEN='\033[1;32m'
NC='\033[0m' # No Color

echo "==evaluating time=="
for i in $(seq 1 5); do
    python3 parse_tree.py --input time_data/input_${i}.txt --output pt_time_output_${i}.txt
    echo -e "${GREEN}parse_tree.py time in test case: input_${i}.txt${NC}"
done

# for i in $(seq 1 5); do
#     python3 parse_tree2.py --input time_data/input_${i}.txt --output pt2_time_output_${i}.txt
#     echo -e "${GREEN}parse_tree2.py time in test case: input_${i}.txt${NC}"
# done
for i in $(seq 1 5); do
    python3 shunting_yard.py --input time_data/input_${i}.txt --output sy_time_output_${i}.txt
    echo -e "${GREEN}shunting_yard.py time in test case: input_${i}.txt${NC}"
done

for i in $(seq 1 5); do
    # python3 shunting_yard.py --input time_data/input_${i}.txt --output sy_time_output_${i}.txt
    dline_py=$(diff sy_time_output_${i}.txt pt_time_output_${i}.txt |  wc | awk -F ' ' '{print $1}')
    if [ "${dline_py}" == "0" ] && [ -f sy_time_output_${i}.txt ] && [ -f pt_time_output_${i}.txt ] ; then
        echo -e "${GREEN}shunting_yard.py is same with parse_tree.py in test case: input_${i}.txt${NC}"
    else
        echo -e "${RED}shunting_yard.py is different from parse_tree.py in test case: input_${i}.txt${NC}"
    fi
done