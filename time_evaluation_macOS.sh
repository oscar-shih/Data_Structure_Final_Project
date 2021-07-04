RED='\033[1;31m'
GREEN='\033[1;32m'
NC='\033[0m' # No Color

echo "==evaluating time=="
for i in $(seq 1 5); do
    python3 parse_tree.py --input time_data/input_${i}.txt --output pt_time_output_${i}.txt
    echo -e "${GREEN}parse_tree.py time in test case: input_${i}.txt${NC}"
done

for i in $(seq 1 5); do
    python3 dp.py --input time_data/input_${i}.txt --output dp_time_output_${i}.txt
    echo -e "${GREEN}dp.py time in test case: input_${i}.txt${NC}"
done

for i in $(seq 1 5); do
    python3 shunting_yard.py --input time_data/input_${i}.txt --output sy_time_output_${i}.txt
    echo -e "${GREEN}shunting_yard.py time in test case: input_${i}.txt${NC}"
done